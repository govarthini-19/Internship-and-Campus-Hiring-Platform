from db import connect
def add_company(user_id,name):
    con=connect()
    cur=con.cursor()
    cur.execute("INSERT INTO Companies(user_id,name)VALUES(?,?)",(user_id,name))
    con.commit()
    con.close()
    print("Company Profile Created!")

def get_company(user_id):
    con=connect()
    cur=con.cursor()
    cur.execute("SELECT * FROM Companies WHERE user_id?",(user_id,))
    data=cur.fetchone()
    con.close()
    return data
