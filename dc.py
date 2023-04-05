import os
import random
import string
import time
from os import system
import ctypes
import requests
import threading
import os

times = int(input('Timeout: '))
thr = int(input("Thread: "))
lists = str(input("Autoload proxy list?(y/n): "))
dead = 0
valid = 0
invalid = 0

pars_proxy = [
'https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt',
'https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
'https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt',
'https://advanced.name/freeproxy/636f77b0c6e9d',
'https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt', #Аня моя радость, моя любовь, и моя жизнь
'https://raw.githubusercontent.com/UptimerBot/proxy-list/main/proxies/http.txt',
'https://raw.githubusercontent.com/rx443/proxy-list/main/online/https.txt',
'https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt',
'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/zevtyardt/proxy-list/main/http.txt',
'https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt'
]

if lists == "y":
    print("Parsing...")
    for site in pars_proxy:
        try:
            proxys = requests.get(site).text
            my_file = open("proxy1.txt", "at")
            my_file.write(f"{proxys}\n")
            my_file.close()
            print(f"Good pars...")
        except:
            print(f"Error pars...")
    print("Deleting duplicates...")
    
    lines_set = set()
    with open(r"proxy1.txt", "r") as fin, open(r"proxy.txt", "w") as fout:
        for line in fin:
            if line not in lines_set:
                fout.write(line)
            lines_set.add(line)
    os.remove("proxy1.txt")
    
    file = open('proxy.txt').read().split('\n')
else:
    names = input("Name proxy file(https): ")
    file = open(names).read().split('\n')

def check(pro):
    https_proxy = f"http://{pro}"
    proxies = {"https": https_proxy}
    while True:
        global invalid
        global valid
        https_proxy = f"http://{pro}"
        proxies = {"https": https_proxy}
        keygen = ('').join(random.choices(string.ascii_letters + string.digits, k=16))
        code = "https://discord.gift/" + keygen
        url = f"https://discordapp.com/api/v6/entitlements/gift-codes/{keygen}?with_application=false&with_subscription_plan=true"
        try:
            response = requests.get(url, proxies=proxies)
            if response.status_code == 200:
                print(f'[Valid] {code}')
                valid = valid + 1
                with open("Codes.txt", "w") as file:
                    file.write(code)
                    
            elif response.status_code == 429:
                time.sleep(5)
                
            else:
                print(f'[Invalid] {code} Статус: {response.status_code}')
                invalid = invalid + 1
        except:
            global dead
            dead = dead + 1
            time.sleep(30)
        
        system("title " + f"Valid: {valid} Invalid: {invalid} Error: {dead}")
        if time != 0:
            time.sleep(int(times))
     
def thread():
    while file:
        proxy = file[0]
        file.remove(proxy)
        try:
            check(proxy)
        except Exception as e:
            print("Ошибка:", e)
     
for i in range(thr):
    t = threading.Thread(target=thread)
    t.start()