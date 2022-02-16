import threading
import time
import random
import sys
import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    rs_port = int(sys.argv[1])
    # rs_port = 50007
    server_binding = ('localhost', rs_port)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    hns = []
    with open("./PROJI-DNSRS.txt", "r") as f:
        for line in f:
            c = line.split(" ")
            hns.append(c)
    while True:
        print ("[S]: Got a connection request from a client at {}".format(addr))

        # send a intro message to the client.
        msg= csockid.recv(1024)
        # msg = "Welcome to CS 352!"
        msg = msg.decode("utf-8");
        if msg == '':
            break
        ok = False
        for line in hns:
            if line[0] == msg:
                msg = ""
                for c in line:
                    msg +=c + " "
                ok = True
                break
        if ok:
            csockid.send(msg.encode('utf-8'))
        else :
            msg = ""
            for i in hns[-1]:
                msg += i + " "
            csockid.send(msg.encode('utf-8'))
        # Close the server socket
    ss.close()
    exit()

t1 = threading.Thread(name='server', target=server)
t1.start()
# server()