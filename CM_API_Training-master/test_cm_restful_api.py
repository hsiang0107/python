from cm_restful_api import *
import base64

cm_server = 'https://10.1.175.16:443'
application_id = '3489AD50-E078-4AD7-8F68-F95C67576C63'
api_key = 'FD6A17BA-4343-4302-85D2-593DBFF312F0'

# Get registered server
# Get TWT
api_path = '/WebApp/XWS/V1/ServerResource/ProductServers'
query_string = '?host_name=TW-OSCE03'
api_url = cm_server + api_path + query_string
# jw_token = get_jwt(application_id, api_key, 'GET', api_path + query_string, '', '')
# Get server list
# res = get_registered_server(jw_token, api_url)


# Add UDSO file
udso_api_path = '/WebApp/XWS/V1/SuspiciousObjectResource/FileUDSO'
udso_file = {
    'file_name': 'my_udso',
    'file_content_base64_string': base64.b64encode('test'.encode('utf-8')).decode('utf-8'),
    'file_scan_action': 'LOG',
    'note': 'api testing'
}
request_body = json.dumps(udso_file)
# Get TWT
jw_token = get_jwt(application_id, api_key, 'PUT', udso_api_path, '', request_body)
res = add_file_UDSO(jw_token, cm_server + udso_api_path, request_body)
print(res.json())