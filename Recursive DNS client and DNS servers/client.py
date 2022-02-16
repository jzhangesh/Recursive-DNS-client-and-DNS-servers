import sys
import threading
import time
import random
import socket
def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()

    # Define the port on which you want to connect to the server
    host_name = sys.argv[1]
    rs_port = int(sys.argv[2])
    ts_port = int(sys.argv[3])
    # rs_port = 50007
    # ts_port = 50008
    # host_name = 'localhost'
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    # server_binding = (localhost_addr, port)
    # server_binding = ('localhost', rs_port)
    # cs.connect(server_binding)
    str_list = []
    with open("./PROJI-HNS.txt") as file_obj:
        for content in file_obj:
            str_list.append(content.rstrip().lower())
    get_list = []
    server_binding = (host_name, rs_port)
    cs.connect(server_binding)
    okcs2 = True
    for data in str_list:

        # cs.send(bytes(data, encoding="utf8"))
        cs.send(data.encode('utf-8'))
        # Receive data from the server
        data_from_server = cs.recv(1024)
        msg = data_from_server.decode('utf-8')
        if "NS" in msg:
            if okcs2:
                c = msg.split(" ")
                server = (c[0], ts_port)
                cs2.connect(server)
            okcs2 = False
            # cs2.send(bytes(data, encoding="utf8"));
            cs2.send(data.encode('utf-8'))
            # Receive data from the server
            data_from_server = cs2.recv(1024)
            msg = data_from_server.decode('utf-8')
        print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))
        get_list.append(msg)
    with open('./RESOLVED.txt', 'w') as f:
        for data in get_list:
            f.writelines(data.lstrip(" ").rstrip(" "))
    # close the client socket
    #cs.close()

    exit()

t2 = threading.Thread(name='client', target=client)
t2.start()