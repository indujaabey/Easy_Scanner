from cmath import e
import imaplib

def imap_login(ip_addr, port_num, username, password):

    # Connect to host using SSL
    imap = imaplib.IMAP4(ip_addr)

    # Login to server

    try:

        imap.login(username, password)

        return True

    except:

        return False
        