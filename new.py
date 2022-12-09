#!/usr/bin/python3

''' This is a comment '''
#This is a comment


from tabulate import tabulate
import array as arr
from ipaddress import ip_address
import nmap
import sys
import pyfiglet
import socket
import datetime
import os

#import termcolor


ascii_banner = pyfiglet.figlet_format("EASY SCANNER")
print(ascii_banner)


scanner = nmap.PortScanner()
#print("Welcome, this is a Simple Scanning Tool")

ascii_banner2 = pyfiglet.figlet_format("Easiest Scanner In The World", font = "digital")
print(ascii_banner2)

print("----------------------------------------------")

print("Please enter the type of scan you want to run\n   1) Port Scanner\n   2) Sub Domain Scanner\n   3) Word Press Website Scanner\n   4) SQL Injection Scanner\n   5) Bruteforce Folder\n   6) Header checker\n   7) XSS Scanner\n   8) Clickjaking Scanner\n   9) Reconnaissance\n   10)Payload Generator\n   11)SSH/FTP Bruteforce")

print("----------------------------------------------")

resp = 1

while  resp !=0 :
    
    
    resp = input("Enter Your Choice:")
    
    if resp == '1' : 
        os.system("python port_scanner/sql.py")

    

    elif resp == '2' :
        opt1=input("\nWebsite name : ")
        os.system("python domain_scanner/1.py "+opt1)
        print(" ")
        
    elif resp == '3' :
        os.system("python wp/wpscanner.py ")
        print(" ")


    elif resp == '4' :
        os.system("python sqlscanner/scan.py ")
        print(" ")
    #new if
    elif resp == '5' :
        os.system("python Bruteforce_path/brute.py ")
        print(" ")

    elif resp == '6' :
        opt1 = input("\nWebsite name : ")
        no = input("Number of parameters to be used: ")
        if int(no) == 0:
               os.system("python Headerchecker/shcheck.py " + opt1) 
               sys.exit()
        parameters = ["ff","-i", "-x", "-p", "-c"]  #add here
        print("------------------------------------------")
        print("Score will be shown for each parameter")
        mydata = [
            ["-i", "1"],
            ["-x", "2"],
            ["-p", "3"],
            ["-c", "4"]  
        ]
        head = ["Parameter", "Score"]
 

        print(tabulate(mydata, headers=head, tablefmt="grid"))

        #i- 1 , x - 2, p - 3, c - 4
        
        lst = []
        
        count = 0
        while int(no) > count:
            k = input("Enter Score: ")
            if int(k) == 3:
                prt_nu = input("Enter Port Number: ")
            if int(k) == 4:
                ck_value = input("Enter Cookie Value: ")
            #add here for parameters with values


            lst.append(k)
            
            count = count + 1
        
        
        if int(no) == 1:
            opt2 = lst[0]
            for x in lst:
                if int(x) == 1:
                    opt2 = "-i"
                elif int(x) == 2:
                    opt2= "-x"
                elif int(x) == 3:
                    opt2= "-p" + prt_nu
                elif int(x) == 4:
                    opt2= "-c" + ck_value

                #add here

            os.system("python Headerchecker/shcheck.py " + opt1 + " " + opt2) 
        elif int(no) == 2:
            
                #for opt 2
            if int(lst[0]) == 1 :
                opt2 = "-i"
            elif int(lst[0]) == 2 :
                opt2= "-x"
            elif int(lst[0]) == 3 :
                opt2= "-p" + prt_nu
            elif int(lst[0]) == 4 :
                opt2= "-c" + ck_value
            
                
                #for opt 3
            if int(lst[1]) == 1 :
                opt3 = "-i"
            elif int(lst[1]) == 2 :
                opt3= "-x"
            elif int(lst[1]) == 3 :
                opt3= "-p" + prt_nu
            elif int(lst[1]) == 4 :
                opt3= "-c" + ck_value
            #add here

            os.system("python Headerchecker/shcheck.py " + opt1 + " " +opt2 + " " + opt3) 

        elif int(no) == 3:
                #for opt 2
            if int(lst[0]) == 1 :
                opt2 = "-i"
            elif int(lst[0]) == 2 :
                opt2= "-x"
            elif int(lst[0]) == 3 :
                opt2= "-p" + prt_nu
            elif int(lst[0]) == 4 :
                opt2= "-c" + ck_value
                
                #for opt 3
            if int(lst[1]) == 1 :
                opt3 = "-i"
            elif int(lst[1]) == 2 :
                opt3= "-x"
            elif int(lst[1]) == 3 :
                opt3= "-p" + prt_nu
            elif int(lst[1]) == 4 :
                opt3= "-c" + ck_value
            
            #for opt 4
            if int(lst[2]) == 1 :
                opt4 = "-i"
            elif int(lst[2]) == 2 :
                opt4= "-x"
            elif int(lst[2]) == 3 :
                opt4= "-p" + prt_nu
            elif int(lst[2]) == 4 :
                opt4= "-c" + ck_value
            
            os.system("python Headerchecker/shcheck.py " + opt1 + " " + opt2 + " " + opt3 + " " + opt4) 

            
        elif int(no) == 4:
                #for opt 2
            if int(lst[0]) == 1 :
                opt2 = "-i"
            elif int(lst[0]) == 2 :
                opt2= "-x"
            elif int(lst[0]) == 3 :
                opt2= "-p" + prt_nu
            elif int(lst[0]) == 4 :
                opt2= "-c" + ck_value
                
                #for opt 3
            if int(lst[1]) == 1 :
                opt3 = "-i"
            elif int(lst[1]) == 2 :
                opt3= "-x"
            elif int(lst[1]) == 3 :
                opt3= "-p" + prt_nu
            elif int(lst[1]) == 4 :
                opt3= "-c" + ck_value
            
            #for opt 4
            if int(lst[2]) == 1 :
                opt4 = "-i"
            elif int(lst[2]) == 2 :
                opt4= "-x"
            elif int(lst[2]) == 3 :
                opt4= "-p" + prt_nu
            elif int(lst[2]) == 4 :
                opt4= "-c" + ck_value

            #for opt 5
            if int(lst[3]) == 1 :
                opt5 = "-i"
            elif int(lst[3]) == 2 :
                opt5= "-x"
            elif int(lst[3]) == 3 :
                opt5= "-p" + prt_nu
            elif int(lst[3]) == 4 :
                opt5= "-c" + ck_value
            
            os.system("python Headerchecker/shcheck.py " + opt1 + " " + opt2 + " " + opt3 + " " + opt4 + " " + opt5) 
       
        
        print(" ")

    elif resp == '7' :
        opt4="-u"
        opt5="--payload-level"
        opt6="7"
        opt7="--method"
        opt10="--cookie"
        opt3=input("\nWebsite name : ")
        usr=input(" 1.Normal scan\n 2.Enter custom payload\n 3.Method\n 4.Enter cookie value\n")
        
        if usr == '1':
            os.system("python XSS_scanner/scan.py "+opt4+opt3)
            print(" ")
        elif usr == '2':
            os.system("python XSS_scanner/scan.py "+opt4+opt3+" "+opt5+" "+opt6)
            print(" ")
        elif usr == '3':
            opt9=input("0:GET\n 1:POST\n 2:GET and POST(Default)")
            os.system("python XSS_scanner/scan.py "+opt4+opt3+" "+opt7+" "+opt9)
            print(" ")
        elif (usr =='23' or usr =='32'):
            opt9=input("0:GET\n 1:POST\n 2:GET and POST(Defaut)")
            os.system("python XSS_scanner/scan.py "+opt4+opt3+" "+opt5+" "+opt6+" "+opt7+" "+opt9)
            print(" ")
        elif usr == '4':
            opt11=input("Enter cookie value(e.g {'ID':'1094200543'}):")
            os.system("python XSS_scanner/scan.py "+opt4+opt3+" "+opt10+" "+opt11)
            print(" ")
        
    elif resp == '8' :
            website=input("Enter website name:")
            os.system("python clickjacking/clickjacking.py "+" "+"-v"+" "+"-d"+website)
            print(" ")

    elif resp == '9' :
            os.system("python reconnaissance/reconnaissance.py ")
            print(" ")

    elif resp == '10' :
            opt1=("-d")
            opt2=("-p")
            ip1=input("Input LHOST: ")
            port1=input("Input LPORT: ")
            os.system("python payload_gen/payload.py " + " " + opt1 + " "+ip1 + " " + opt2 + " " + port1 )
            print(" ")

    elif resp == '11' :
            mode1=input("ssh/ftp: ")
            mode2=input("Enter the ip: ")
            mode3=input("Enter the port number: ")
            mode4=input("Enter the path of users payload file: ")
            mode5=input("Enter the path of password payload file: ")
            
            os.system("python ssh-ftp-brute/brutus.py" +" " + "-m" + " " + mode1 +" "+"-t"+" "+mode2+" "+"-p"+" "+mode3+" "+"-U"+" "+mode4+" "+"-P"+" "+mode5 )
            print(" ")


    #new if


    else: 
        print("Invalid")

    prgo = input("Do You Wish To do another scan('1' for yes and '7' for No)?")   
    if prgo == '1' :
        print("----------------------------------------------")

        print("Please enter the type of scan you want to run\n   1) Port Scanner\n   2) Sub Domain Scanner\n   3) Word Press Website Scanner\n   4) SQL Injection Scanner\n   5) Bruteforce Folder\n   6) Header checker\n   7) XSS Scanner\n   8) Clickjaking Scanner\n   9) Reconnaissance\n   10)Payload Generator\n   11)SSH/FTP Bruteforce")

        print("----------------------------------------------")
        continue
    else : 
        break

    
    


exit()