import socket
import threading
from colorama import init, Fore, Back, Style

init()
# Sunucu detayları
host = "0.0.0.0"
port = 8855

# Yeni istemci bağlantısı kabul edildiğinde çağrılacak fonksiyon
def handle_client(baglantı, client_address):
    print(f"Bağlantı kabul edildi: {client_address}")

    while True:
        try:
            command = input("İstemciye gönderilecek komut: ")
            baglantı.send(command.encode("utf-8"))
            
            # İstemciden gelen yanıtı al
            response = baglantı.recv(1024).decode("utf-8")
            print(f"{client_address} adresinden gelen yanıt:  { response}")
            
            
            if command.lower() == "exit":
                break
        except:
            break

    print(f"Bağlantı kesildi: {client_address}")
    baglantı.close()

# Sunucu soketi oluşturma
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)
print("Sunucu dinleniyor...")

# Bağlantıyı kabul etme
client_socket, client_address = server_socket.accept()
client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
client_thread.start()
