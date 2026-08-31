import sqlite3
DB="hiring.db"
def connect():
    return sqlite3.connect(DB)
def create_tables():
    con=connect()
    cur=con.cursor
    cur.execute("""CREATE TABLE IF NOT EXISTS Users(id INTEGER PRIMARY KEY AUTOINCREMENT,username TEXT UNIQUE,password TEXT,role TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS STUDENTS(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER,name TEXT,cgpa REAL,skills TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Companies(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER,name TEXT)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Jobs(id INTEGER PRIMARY KEY AUTOINCREMENT,company_id INTEGER,role TEXT,skils TEXT,min_cgpa REAL,openings INTEGER)""")
    cur.execute("""CREATE TABLE IF NOT EXISTS Application(id INTEGER PRIMARY KEY AUTOINCREMENT,student_id INTEGER,job-id INTEGER,status TEXT)""")
    con.commit()
    con.close()
