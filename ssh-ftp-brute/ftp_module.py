import ftplib

def ftp_login(ip_addr, port_num, username, password):

    ftp = ftplib.FTP(ip_addr)

    #ftp.connect(ip_addr, port = port_num)

    try:

        ftp.login(username, password)

        return True

    except:

        return False