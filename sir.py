'''
Server ip registry
'''

import socket
import threading
from zdbs.utils import get as db
import re 

sn = open("dn").read()
regex = f"^.*#(.*)$"

def status(code: int, *data):
    '''
    The status code groups are:
    10: OK
    2*: MALFORMED REQUEST
    30: NOT FOUND
    4*: SERVER ERROR
    '''
    delimiter = '\0'
    
    codes = {
        10: "OK",
        20: "MALFORMED REQUEST",
        21: "UNKNOWN COMMAND",
        22: "NOT ENOUGH PARTS",
        30: "DOMAIN NOT FOUND",
        31: "SIR SERVER NOT FOUND FOR SERVER"
        40: "SERVER ERROR",
        41: "TRIED TO SEND UNKNOWN CODE"
    }

    parsed_data = ""
    for d in data:
        parsed_data += '\0' + str(d)

    if code not in codes.keys():
        return f"41\0{codes[41]}{parsed_data}"

    return f"{code}\0{codes[code]}{parsed_data}"

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
        case "i":
            if re.search(regex,data).group(1) != sn
            #con = db.get()
            #con.cursor().execute("SELECT domain FROM domain WHERE ip = ?",(data,))

    ip = "127.0.0.1"
    return status(10, ip)

def main(port: int):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('127.0.0.1', port))
    sock.listen(5)

    while True:
        connection,address = sock.accept()
        try:
            threading.Thread(target=handle_client,args=(connection,address)).start()
        except Exception as e:
            print("Handle client failed: "+e)

if __name__ == "__main__":
    main(2526)
