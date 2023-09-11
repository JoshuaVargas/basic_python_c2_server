import socket

#define client config function
def session_handler():
    print(f'[+] Connecting to {host_ip}...')
    sock.connect((host_ip, host_port))
    print(f'Connected to {host_ip}.')
    sock.close()

#declare socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#setting up host ip and port
host_ip = '127.0.0.1'
host_port = 2222

session_handler()


