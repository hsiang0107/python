import os
import sean_fnc.print_fnc

__author__ = 'twlhgs'
man = []
other = []
os.chdir("D://audatex/prj/python/pycharm/self_training_0719/file")
print("current path: "+os.getcwd())
try:
    #data = open("sketch.txt")
    with open("sketch.txt") as data:
        for each_line in data:
            try:
                (role,speak) = each_line.split(":",1)
                speak = speak.strip()
                if role == "Man":
                    man.append(speak)
                else:
                    other.append(speak)
            except ValueError:
                pass
        # print("For Man's speak")
        # sean_fnc.print_fnc.print_list(man,True,1)
        # print("For Other speak")
        # sean_fnc.print_fnc.print_list(other,True,1)
except IOError as err:
    print("File not found"+str(err))

try:
    with open("log4.txt","a") as log:
        print("For Man's speak",file=log)
        sean_fnc.print_fnc.print_list(man,True,2,log)
        print("For Other speak",file=log)
        sean_fnc.print_fnc.print_list(other,True,2,log)
except IOError as err:
    print("Cannot write log file"+str(err))