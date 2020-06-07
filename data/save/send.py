import socket
import sys
from types import *
import struct
import time
import logging

with open('test.txt', 'r+') as filehandler:
    with open('send.txt','w') as filehandler2:
        filehandler2.write(''.join([fh.replace(" ","") for fh in filehandler]))

HOST = '127.0.0.1'    # The remote host
dest_port = 502       # The same port as used by the server
logging.basicConfig(filename='./fuzzer.log', filemode='a', level=logging.DEBUG, format='[%(asctime)s][%(levelname)s] %(message)s')

def create_connection(dest_ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        sys.stderr.write("[ERROR] %s\n" % msg[1])
        sys.exit(1)

    HOST = dest_ip
    try:
        sock.settimeout(0.5)
        sock.connect((HOST, dest_port))
    except socket.error as msg:
        logging.exception("Connection Failed!")
    else:
        logging.info("Connected to Server: %s" % dest_ip)

    return sock


def hexstr(s):
    return '-'.join('%02x' % ord(c) for c in s)



with open('send.txt','r') as filehandler2:
    for msg in filehandler2:
        strInput = msg
        dataSend = ""
        shortInput = ""
        cnt = 1
        sock = create_connection(HOST, dest_port)
        for chInput in strInput:
            shortInput += chInput
            if cnt%2 == 0:
                intInput = int(shortInput,16)
                dataSend += struct.pack(">B", intInput)
                shortInput = ""
            cnt += 1
        try:
            sock.send(dataSend)
            print('sent: %s' % hexstr(dataSend))
        except socket.error:
            sock.close()
            print('trying to create connection again')
            sock = create_connection(HOST, dest_port)
        try:
            dataRecv = sock.recv(1024)
            print (sys.stderr, 'received: %s' % hexstr(dataRecv))
        except socket.timeout:
            print('recv timed out!')
        except socket.error:
            sock.close()
            sock = create_connection(HOST, dest_port)

        sock.close()