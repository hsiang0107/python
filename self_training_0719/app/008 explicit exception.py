import os
__author__ = 'twlhgs'

print(os.getcwd())
os.chdir('D://audatex/prj/python/pycharm/self_training_0719/file')
print(os.getcwd())
try:
    file = open('sketch.txt')
    file.seek(0)
    for each_line in file:
        try:
            (role,speak) = each_line.split(":",1)
            print(role,end='')
            print(" said",end='')
            print(speak)
        except ValueError:
            pass
    file.close()
except IOError:
    print("file not found")