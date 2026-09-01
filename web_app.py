import streamlit as st
import sqlite3
def connect():
    return sqlite3.connect("hiring.db")
def create_tables():
    con = connect()
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Students(
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        name TEXT,
        cgpa REAL,
        skills TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Companies(
        company_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        company_name TEXT
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Jobs(
        job_id INTEGER PRIMARY KEY AUTOINCREMENT,
        company_name TEXT,
        role TEXT,
        required_skills TEXT,
        min_cgpa REAL,
        openings INTEGER
    )
    """)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Applications(
        application_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_username TEXT,
        job_id INTEGER,
        status TEXT
    )
    """)
    con.commit()
    con.close()
create_tables()
def register(username, password, role):
    con = connect()
    cur = con.cursor()

    cur.execute(
        "SELECT * FROM Users WHERE username=?",
        (username,)
    )
    user = cur.fetchone()
    if user:
        con.close()
        return False
    cur.execute(
        "INSERT INTO Users(username,password,role) VALUES(?,?,?)",
        (username, password, role)
    )
    con.commit()
    con.close()
    return True
def login(username, password):
    con = connect()
    cur = con.cursor()
    cur.execute(
        """SELECT id, role FROM Users
           WHERE username=? AND password=?""",
        (username, password)
    )
    user = cur.fetchone()
    con.close()
    return user
def add_student(username, name, cgpa, skills):
    con = connect()
    cur = con.cursor()
    cur.execute(
        """INSERT INTO Students
           (username,name,cgpa,skills)
           VALUES(?,?,?,?)""",
        (username, name, cgpa, skills)
    )
    con.commit()
    con.close()
def add_company(username, company_name):
    con = connect()
    cur = con.cursor()
    cur.execute(
        """INSERT INTO Companies
           (username,company_name)
           VALUES(?,?)""",
        (username, company_name)
    )
    con.commit()
    con.close()
def post_job(company_name, role, skills, cgpa, openings):
    con = connect()
    cur = con.cursor()
    cur.execute(
        """INSERT INTO Jobs
           (company_name,role,required_skills,min_cgpa,openings)
           VALUES(?,?,?,?,?)""",
        (company_name, role, skills, cgpa, openings)
    )
    con.commit()
    con.close()
def apply_job(username, job_id):
    con = connect()
    cur = con.cursor()
    cur.execute(
        """SELECT * FROM Applications
           WHERE student_username=? AND job_id=?""",
        (username, job_id)
    )
    existing = cur.fetchone()
    if existing:
        con.close()
        return False
    cur.execute(
        """INSERT INTO Applications
           (student_username,job_id,status)
           VALUES(?,?,?)""",
        (username, job_id, "Applied")
    )
    con.commit()
    con.close()
    return True
st.set_page_config(
    page_title="Campus Hiring Platform",
    page_icon="🎓",
    layout="wide"
)
st.title("🎓 Internship & Campus Hiring Platform")
st.write("Connect Students with Companies")
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "role" not in st.session_state:
    st.session_state.role = ""
if not st.session_state.logged_in:
    menu = st.sidebar.selectbox(
        "Menu",
        ["Login", "Register"]
    )
    if menu == "Register":
        st.header("📝 User Registration")
        username = st.text_input("Username")
        password = st.text_input(
            "Password",
            type="password"
        )
        role = st.selectbox(
            "Select Role",
            ["student", "company"]
        )
        if st.button("Register"):
            if username == "" or password == "":
                st.warning("Please enter all details")
            else:
                result = register(
                    username,
                    password,
                    role
                )
                if result:
                    st.success(
                        "Registration successful!"
                    )
                else:
                    st.error(
                        "Username already exists!"
                    )
    else:
        st.header("🔐 User Login")
