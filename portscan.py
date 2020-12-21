
#By Luiz Viana      github.com/luizviana
#Run with python3 - rodar com python3

import os
import sys
import socket


class Colors(object):

    red = '\033[1;31m'
    green = '\033[1;32m'
    yellow = '\033[1;33m'
    cyan = '\033[1;36m'
    magenta = '\033[1;35m'

colors = Colors()

def scan(ip, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(1)
            code = client.connect_ex((ip, port))
            if code == 0:
                print(f"{colors.green}[+] {port} open")
    except Exception as e:
        print(f"{colors.red}[!] Error, something is wrong")
    except KeyboardInterrupt:
        print(f"\n{colors.red}[!] Program exited!\n")
        
def fastscan(ip):
    print(f"{colors.cyan}[*] Fast Scan in progress")
    ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    return scan(ip, ports)

def fullscan(ip):
    print(f"{colors.cyan}[*] Full Scan in progress")
    ports = range(1,65536)
    return scan(ip, ports)

def customscan(ip, arg_port_range):
    try:
        ports = []
        if "-" in arg_port_range:
            arg_port_range = arg_port_range.split("-")
            arg_port_range[0] = int(arg_port_range[0])
            arg_port_range[1] = int(arg_port_range[1])
            arg_port_range.sort()
            start = int(arg_port_range[0])
            end = int(arg_port_range[1])
            print(f"{colors.magenta}[-] Range Port: {arg_port_range[0]}-{arg_port_range[1]}")
            for port in range(start, end+1):
                ports.append(port)
            print(f"{colors.cyan}[*] Custom Scan in progress.")
            return scan(ip, ports)
        else:
            ports.append(int(arg_port_range))
            return scan(ip, ports)
    except:
        print(f"{colors.red}[!] Bad arguments")


def read_arguments():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print(f"""{colors.cyan}
## portscan python3 ##
Usage: python portscan.py <IP> <mode>
Fast mode usage: python portscan.py <ip> fast
Full mode usage: python portscan.py <ip> full
Custom mode usage: python portscan.py <ip> 80-1000""")
    else:
        ip = sys.argv[1]
        mode = sys.argv[2]
        return ip, mode

if __name__ == "__main__":
    try:
        os.system("clear")
    except:
        try:
            os.system("cls")
        except:
            pass
    args = read_arguments()
    if args:
        ip, mode = args
        if mode.lower() == 'fast':
            fastscan(ip)
        elif mode.lower() == 'full':
            fullscan(ip)
        else:
            customscan(ip, mode.lower())
