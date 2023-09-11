import socket

#define server config function
def listener_handler():
    sock.bind((host_ip, host_port))
    print('[+] Awaiting client connection...')
    sock.listen()
    remote_target, remote_ip = sock.accept()
    print(f'[+] Connection recieved from {remote_ip[0]}.')
    remote_target.close()

#declare socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#setting up host ip and port
host_ip = '127.0.0.1'
host_port = 2222

listener_handler()