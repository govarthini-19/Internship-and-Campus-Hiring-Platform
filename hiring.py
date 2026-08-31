from db import connect
from matching import calculate_score,eligible
def shortlist(job_id):
    con=connect()
    cur=con.cursor()
    cur.execute("SELECT skills,min_cgpa FROM  Jbs WHERE id=?",(job_id,))
    job=cur.fetchone()
    if not job:
        print("Job not Found!")
        con.close()
        return
    required,minimum=job
    cur.execute("""SELECT Students.id,Students.name,Students.skills FROM Students""")
    students=cur.fetchall()
    result=[]
    for s in students:
        if eligible(s[3],required,s[2],minimum):
            score=calculate_score(s[3],required,s[2])
            result.append((s[0],s[1],score))
    result.sort(key=lambda x:x[2],reverse=True)
    print("\n----SHORTLIST")
    for student in result:
        print(
            "ID:", student[0],
            "Name:", student[1],
            "Score:", round(student[2], 2)
        )
    con.close()
