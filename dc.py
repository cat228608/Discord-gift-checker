import os
import random
import string
import time
from os import system
import ctypes
import requests
import threading

times = int(input('Timeout: '))
thr = int(input("Thread: "))
lists = str(input("Autoload proxy list?(y/n): "))
valid = 0
invalid = 0

if lists == "y":
    print("parsing...")
    try:
        proxys = requests.get("https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt").text
        my_file = open("proxy.txt", "at")
        my_file.write(f"{proxys}\n")
        my_file.close()
        print("Good pars...")
    except:
        print("Error num 1")
    try:
        proxys = requests.get("https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt").text
        my_file = open("proxy.txt", "at")
        my_file.write(f"{proxys}\n")
        my_file.close()
        print("Good pars...")
    except:
        print("Error num 2")
    try:
        proxys = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
        my_file = open("proxy.txt", "at")
        my_file.write(f"{proxys}\n")
        my_file.close()
        print("Good pars...")
    except:
        print("Error num 3")
    try:
        proxys = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt").text
        my_file = open("proxy.txt", "at")
        my_file.write(f"{proxys}\n")
        my_file.close()
        print("Good pars...")
    except:
        print("Error num 4")
    try:
        proxys = requests.get("https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt").text
        my_file = open("proxy.txt", "at")
        my_file.write(f"{proxys}")
        my_file.close()
        print("End pars")
    except:
        print("Error num 5")
    
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

            else:
                print(f'[Invalid] {code}')
                invalid = invalid + 1
        except:
            time.sleep(30)
        
        system("title " + f"Valid: {valid} Invalid: {invalid}")
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