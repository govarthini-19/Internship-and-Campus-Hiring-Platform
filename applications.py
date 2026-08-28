from db import connect
def apply(student_id,job_id):
    con=connect()
    cur=con.cursor()
    cur.execute("""INSERT INTO Applications(student_id,job_id,status)VALUE(?,?,?)""",(student_id,job_id,"Applied"))
    con.commit()
    con.close()
    print("Application Submitted!")
def view_application(student_id):
    con=connect()
    cur=con.cursor()
    cur.execute("""SELECT Applications.id,job.role,companies.name,Application.status FROM Applications JOIN Jobs ON APplications.job_id=Jobs.id Join Companies ON Jobs.company_id=Companies.id
    WHERE Applications.student_id=?""",(student_id,))
    data=cur.fetechall()
    con.close()
    return data
