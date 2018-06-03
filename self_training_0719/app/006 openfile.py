import os
__author__ = 'twlhgs'

print(os.getcwd())
os.chdir('D://audatex/prj/python/pycharm/self_training_0719/file')
print(os.getcwd())
if os.path.exists('sketch.txt'):
    file = open('sketch.txt')
    # print(file.readline(),end='')
    # print(file.readline(),end='')

    file.seek(0)
    for each_line in file:
        if not each_line.find(":") == -1:
            (role,speak) = each_line.split(":",1)
            print(role,end='')
            print(" said",end='')
            print(speak)
    file.close()
else:
    print("File not found")