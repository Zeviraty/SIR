from zdbs.utils import get as db

def get_server(name: str): 
    return db().cursor().execute("SELECT ip FROM server WHERE name = ?",(name,)).fetchone()

def get_domain(ip: str):
    return db().cursor().execute("SELECT domain FROM domain WHERE ip = ?",(ip,)).fetchone()

def get_ip(domain: str):
    return db().cursor().execute("SELECT ip FROM domain WHERE domain = ?",(domain,)).fetchone()

def add_domain(name:str, ip:str, owner: str):
    con = db()
    cur = db().cursor()
    cur.execute("INSERT INTO domain (?,?,?)",(name,owner,ip))
    con.commit()
    con.close()

def add_server(name:str, ip:str):
    con = db()
    cur = db().cursor()
    cur.execute("INSERT INTO server (?,?)",(name,ip))
    con.commit()
    con.close()

def remove_domain(name:str):
    con = db()
    cur = db().cursor()
    cur.execute("DELETE FROM domain WHERE name = ?",(name,))
    con.commit()
    con.close()

def remove_server(name:str):
    con = db()
    cur = db().cursor()
    cur.execute("DELETE FROM server WHERE name = ?",(name,))
    con.commit()
    con.close()

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
        11: "SIR REDIRECT",
        20: "MALFORMED REQUEST",
        21: "UNKNOWN COMMAND",
        22: "NOT ENOUGH PARTS",
        30: "SERVER NOT FOUND",
        31: "SIR SERVER NOT FOUND FOR SERVER",
        40: "SERVER ERROR",
        41: "TRIED TO SEND UNKNOWN CODE"
    }

    parsed_data = ""
    for d in data:
        parsed_data += '\0' + str(d)

    if code not in codes.keys():
        return f"41\0{codes[41]}{parsed_data}"

    return f"{code}\0{codes[code]}{parsed_data}"
