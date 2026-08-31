from db import connect
def register(username,password,role):
    con=connect()
    cur=con.cursor()
    cur.execute("SELECT* FROM Users WHERE username=?",(username,))
    user=cur.fetchone()
    if user:
        print("Username is Already Exists!")
    else:
        cur.execute("INSERT INTO Users(username,password,role)VALUES(?,?,?)",(username,password,role))
        con.commit()
        print("Registration Successful!")
    con.close()

def login(username,password):
    con=connect()
    cur=con.cursor()
    cur.execute("SELECT id,rolebFROM Users WHERE username=? AND password=?",(username,password))
    user=cur.fetchone()
    if user:
        print("Login Successful!")
        print("Role:",user[1])
    else:
        print("INvalid username or password!")
    con.close()
    return user
