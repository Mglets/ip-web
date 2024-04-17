import socket
F = '\033[1;32m'
Z = '\033[1;31m'
A = '\033[2;34m'  
X = '\033[1;33m'
B = '\x1b[38;5;208m'
M = '\x1b[1;37m'
url = input(f"[#]{X}Enter the URL: {M} ")
print(f"{A}_" *60)
try:
    Ip = socket.gethostbyname(url)
    print(f'{B}IP address For(ᎷΌᎪᏃ ՏᎪᎻᎬᎬΝ)  [{M}{url}{M}] is | {F} {Ip}')
except socket.gaierror:
    print(f'{Z}Error Getting IP')
