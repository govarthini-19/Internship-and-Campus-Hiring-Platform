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
