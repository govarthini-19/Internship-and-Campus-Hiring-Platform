from db import connect
def add_student(user_id,name,cgpa,skills):
    con=connect()
    cur=con.cursor()
    cur.execut("""INSERT INTO Students(user_id,name,cgpa,skills)VALUES(?,?,?)""",(user_id,name,cgpa,skills))
    con.commit()
    con.close()
    print("Student profile Created!")

def get_student(user_id):
    con=connect()
    cur=con.cursor()
    cur.execute("SELECT *FROM Students WHERE user_id=?",(user_id,))
    data=cur.fetchone()
    con.close()
    return data
