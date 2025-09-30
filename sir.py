'''
Server ip registry
'''

import socket
import threading
import re 
from utils import *

sn = open("sn").read()
regex = f"^(.*)#(.*)$"

def handle_client(connection,address):
    recv = connection.recv(1024).decode()
    connection.send(handle_request(recv).encode())

def handle_request(request):
    parts = request.split("\0")
    if len(parts) != 2:
        return status(22,*parts)
    cmd = parts[0]
    data = parts[1]
    if cmd not in ("i","d"):
        return status(21,cmd)
    match cmd:
        case "i" | "d":
            n = re.search(regex,data)

            if n.group(2).strip().replace("\n","") != sn.strip().replace("\n",""):
                server = get_server(n.group(2))
                if server == None:
                    return status(31,data)
                return status(11,server)
            if cmd == "i":
                result = get_ip(n.group(1))
            else:
                result = get_domain(n.group(1))
            if result == None:
                return status(30,data)
            return status(10,result)
        case _:
            return status(40)

def main(port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port))
    sock.listen(5)

    while True:
        connection,address = sock.accept()
        try:
            threading.Thread(target=handle_client,args=(connection,address)).start()
        except Exception as e:
            print("Handle client failed: "+e)

if __name__ == "__main__":
    main(2526)
