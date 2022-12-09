from ipaddress import ip_address
import nmap
import sys
import pyfiglet
import socket
import datetime
import os

scanner = nmap.PortScanner()
print("----------------------------------------------")

print("Please enter the type of scan you want to run\n   1)TCP SYN scan\n   2)UDP Scan\n   3)TCP ACK scan\n   4)TCP FIN scan\n   5)TCP Connect scan\n   6)Service Scan\n   7)port Scan\n ")

print("----------------------------------------------")

resp = input("Enter Your Choice:")
if resp == '1' : 
        ip_addr = input("please enter the IP: ")
        print("The ip you entered: ", ip_addr)
        type(ip_addr)

        port = input("please enter port/port-range: ")
        print("Port/port-range you entered: ", port)
        type(port)

        print("nmap version: ", scanner.nmap_version())
        scanner.scan(ip_addr, port, '-v -sS')
        print(scanner.scaninfo())
        print("Ip status: ", scanner[ip_addr].state())
        print(scanner[ip_addr].all_protocols())
        print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '2' :

    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sU')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['udp'].keys())

elif resp == '3' :

    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sA')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '4' :
    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sF')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '5' :

    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sT')
    print(scanner.scaninfo())
    print("Ip status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open ports: ", scanner[ip_addr]['tcp'].keys())

elif resp == '6' :

    ip_addr = input("please enter the IP: ")
    print("The ip you entered: ", ip_addr)
    type(ip_addr)

    port = input("please enter port/port-range: ")
    print("Port/port-range you entered: ", port)
    type(port)

    print("nmap version: ", scanner.nmap_version())
    scanner.scan(ip_addr, port, '-v -sS')
    print(scanner.scaninfo())
    print("Ip status: ", scanner.csv())
        


    #new portion
elif resp == '7' :
        
    ip_addr1 = input("please enter the IP: ")
    target = socket.gethostbyname(ip_addr1)  # translate hostname to IPv4
        

    start = int(input("Enter the starting port number: "))
    end = int(input("Enter the ending port number: "))
        
    try:
        for port in range(start, end):  # max range of port is from 0 to 65535
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))  # returns an error indicator
            if result == 0:
                print("Port {} is open".format(port))
            s.close()

    except  KeyboardInterrupt:
        print("\n Exiting Program....")
        sys.exit()
        
    except socket.gaierror:
        print("\n Hostname Could Not Be Resolved !!!!")
        sys.exit()
        
    except socket.error:
        print("\n Server not responding !!!!")
        sys.exit()
