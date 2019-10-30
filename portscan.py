#By Luiz Viana      github.com/luizviana
import sys
import socket


def scan(ip, ports):
    try:
        for port in ports:
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.settimeout(0.05)
            code = client.connect_ex((ip, port))
            if code == 0:
                print("[+] {} open".format(port))
    except:
        print("Error, something is wrong")
    finally:
        print("\ndone!!!")

        
def fastscan(ip):
    print("Fast Scan in progress")
    ports = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
    return scan(ip, ports)


def fullscan(ip):
    print("Full Scan in progress")
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
            print("range: {}-{}".format(arg_port_range[0], arg_port_range[1]))
            for port in range(start, end+1):
                ports.append(port)
                
            print("Custom Scan in progress.")
            return scan(ip, ports)
        else:
            ports.append(int(arg_port_range))
            return scan(ip, ports)
    except:
        print("Bad arguments")



def ler_argumentos():
    if len(sys.argv) == 1 or len(sys.argv) > 3:
        print("## portscan python3 ##")
        print("Usage: python portscan.py <IP> <mode>\n")
        print("Fast mode usage: python portscan.py <ip> fast")
        print("Full mode usage: python portscan.py <ip> full")
        print("Custom mode usage: python portscan.py <ip> 80-1000")
    else:
        ip = sys.argv[1]
        mode = sys.argv[2]
        return ip, mode


if __name__ == "__main__":
    args = ler_argumentos()
    if args:
        ip, mode = args
        if mode == 'fast':
            fastscan(ip)
        elif mode == 'full':
            fullscan(ip)
        else:
            customscan(ip, mode)
