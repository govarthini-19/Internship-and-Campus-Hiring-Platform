import streamlit as st
import sqlite3
def connect():
    return sqlite3.connect("hiring.db")
