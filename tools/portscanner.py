import socket
import termcolor
import threading


def scan(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5)
        sock.connect((target, port))
        print("[+] Port Opened " + str(port))
        sock.close()
    except:
        pass


def scan_ports(target, ports):
    print('\n' + ' Starting Scan For ' + str(target))
    for port in ports:
        threading.Thread(target=scan, args=(target, port)).start()


targets = input("[*] Enter Targets To Scan(split them by ,): ")
ports = range(1, int(input("[*] Enter How Many Ports You Want To Scan: "))+1)
if ',' in targets:
    print(termcolor.colored(("[*] Scanning Multiple Targets"), 'green'))
    for ip_addr in targets.split(','):
        scan_ports(ip_addr.strip(' '), ports)
else:
    scan_ports(targets, ports)
