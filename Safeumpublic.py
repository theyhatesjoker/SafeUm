import requests
import random
import requests
import json
import pyfiglet
import sys
import time
import os
import uuid
import webbrowser
import fake_useragent



Ab = '\033[1;92m'
aB = '\033[1;91m'
AB = '\033[1;96m'
aBbs = '\033[1;93m'
AbBs = '\033[1;95m'
A_bSa = '\033[1;31m'
a_bSa = '\033[1;32m'
faB_s = '\033[2;32m'
a_aB_s = '\033[2;39m'
Ba_bS = '\033[2;36m'
Ya_Bs = '\033[1;34m'
S_aBs = '\033[1;33m'
ab = pyfiglet.figlet_format("SafeUm")
print(a_bSa + ab)


def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)


to(
    f"\033[31;m TOOL >> \033[1;36mACCOUNT CREATOR\n\033[1;31m DEVELOPER >>\033[1;33m @Theyhates_joker\n\033[31;m")
print('')
print('\033[32;m')

from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []


def work():
    global failed, success, retry
    username = choice('qwertyuiooasdfghjklzxcvpbnm') + ''.join(choices(list('qwertyuioasdfghjklzxcvbnpm1234567890'), k=16))
    try:
        con = create_connection("wss://195.13.182.213/Auth",
                                header={"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.213",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2024-04-11 11:00:00", "url": "wss://51.79.208.190/Auth"},
                                sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps(
            {"action":"Register","subaction":"Desktop","locale":"en_GB","gmt":"+05","password":{"m1x":"bfe8736a2d0d60d2f650b15adec2c5526fc606cd7a537f13c910b4b3bd61ec4b","m1y":"f7bcdc14fe0f17961c5861894b4943c445285960463a4cc9021cbf1b1687c1dd","m2":"0fb27fb496e50e0676946334ef17719d62657bc000434bc575f7f8b3d053d1aa","iv":"6ffd51d70264b8d2a5e78ae8e3ae0a62","message":"3db3f7f46d13f3d479d8c632a3a68b5057fac130ee8bbec4f73fbb01156acb2875425f568d5c8e71e0e16c500e4937f81c25257bc702f794fc5cfc393f65988521bfd130f46c535d2590fafd091dd1b2"},"magicword":{"m1x":"89df3cf590420f4a08190919bc34e68e121294b048430ec5bdbd5459dc1d099a","m1y":"913d4bb2d4d68cf74427422ba96a3a45238e61eebfc7e276ecec9961627fcce5","m2":"0a3a719c63c3156c20be5ce4edcb5150e2fe9394247617598a4a8a48a5469a2a","iv":"960b6904f39156bcb249379648b690c6","message":"cfa8992ec47f2431b17e7cbb9c5cf442"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 23106RN0DA","softwareversion":"1.1.0.1548","nickname":"jhdh299snnaabi","os":"AND","deviceuid":"63e6d773ee99664d","devicepushuid":"*eaUWw7kOQriJL-QUuwEu6u:APA91bFAEp8KNAkuZ9lQc5k9y1SaOaa7p7s5zjiqhtFm0qISEF4O049gS24L9VBvwIBGzFA57EZFcVKNVll66AMBaEJ5qqEP2DuJU-7wrnChZSZtWA0pd-8VRPerIKyHYM7ieHzVH4LF","osversion":"and_13.0.0","id":"212993450"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            b = accounts.append(username + ':aaaa')
            print(b)
            with open('SafeUM.txt', 'a') as f:
                f.write(username + ":aaaa | TG : @Theyhates_joker\n")

        else:
            failed += 1
    except:
        retry += 1


start = ThreadPoolExecutor(max_workers=1000)


while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(
        failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))
    hh = str(failed) + str(success) + str(retry)
    if int(success) >= 900:
        fuck()
        print("Created Accounts Successfully")
        
    
    if int(success) > int(0):
        z = "\n".join(accounts)
        
        print("CREATED ACCOUNTS>>\n", z)
        

    os.system('clear')
