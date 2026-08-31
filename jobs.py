from db import connect
def add_job(company_id,role,skills,cgpa,openings):
    con=connect()
    cur=con.cursor()
    cur.execute("""INSERT INTO Jobs(company_id,role,skills,cgpa,openings)VALUES(?,?,?,?,?)""",(company_id,role,skills,cgpa,openings))
    con.commit()
    con.close()
    print("Job Posted Successfully!")

def view_jobs():
    con=connect()
    cur=con.cursor()
    cur.execute("""SELECT jobs.id,Companies.name,Jobs.role,Jobs.skill,Jobs.min_cgpa,Job.oppenings FROM Jobs JOIN Companies ON Jobs.company_id=ompanies.id""")
    jobs=cur.fetchall()
    con.close()
    return jobs
