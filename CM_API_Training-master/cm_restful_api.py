import jwt
import hashlib
import requests
import time
import codecs
import json


def get_jwt(app_id, private_key, http_method, raw_url, header, request_body, algorithm='HS256', version='V1'):
    string_for_hash = http_method.upper() + '|' + raw_url.lower() + '|' + header + '|' + request_body
    hash_obj = hashlib.sha256(string_for_hash.encode('utf-8'))
    hash_byte = hash_obj.digest()
    base64_byte = codecs.encode(hash_byte, 'base64')
    hash_string = base64_byte.decode('utf-8')
    hash_string = hash_string[:-1]

    issue_time = time.time()
    payload = {
        'appid': app_id,
        'iat': issue_time,
        'version': version,
        'checksum': hash_string
    }
    token = jwt.encode(payload, private_key, algorithm=algorithm).decode('utf-8')
    return token


def get_registered_server(token, endpoint):
    header = {
        'Authorization': 'Bearer ' + token
    }
    response = requests.get(endpoint, headers=header, verify=False)
    return response

def add_file_UDSO(token, endpoint, udso_file):
    header = {
        'Authorization': 'Bearer ' + token
    }
    request_body = udso_file
    response = requests.put(endpoint, headers=header, data=request_body, verify=False)
    return response