GNU nano 7.1                           yaparr.py
#!/usr/bin/env python3

import os

while True:
       os.system("pkg install figlet")
       os.system("clear")
       os.system("figlet şuayip")
       print("""
şuayip yapar hacker araci

1) site hakkinda genel bilgi
2) hizli port tarama
3) versiyon bilgisi
Q) çikiç

""")
       islemno =input("islem numarasini giriniz: ")

       if islemno=="1":
              hedefip= input("hedef siteyi giriniz: ")
              os.system("whois "+hedefip)
       elif islemno=="2":
              hedefip= input("hedef siteyi giriniz: ")
              os.system("nmap "+hedefip)
       elif islemno=="3":
              hedefip= input("hedef siteyi girinzi: ")
              os.system("nmap -sV "+hedefip)
       elif islemno=="q" or islemno=="q":
              quit()
       else:
              print("hatali be kardeşim")
