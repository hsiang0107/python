import os
import sean_fnc.print_fnc
__author__ = 'twlhgs'
man = []
other = []
os.chdir("D://audatex/prj/python/pycharm/self_training_0719/file")
print("current path: "+os.getcwd())
try:
    data = open("sketch.txt")
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
    print("For Man's speak")
    sean_fnc.print_fnc.print_list(man,True,1)
    print("For Other speak")
    sean_fnc.print_fnc.print_list(other,True,1)
except IOError as err:
    print("File not found"+str(err))
finally:
    if "data" in locals():
        data.close()

try:
    log = open("log3.txt","a")
    print("For Man's speak",file=log)
    print(man,file=log)
    print("For Other speak",file=log)
    print(other,file=log)
except IOError as err:
    print("Cannot write log file"+str(err))
finally:
    log.close()
