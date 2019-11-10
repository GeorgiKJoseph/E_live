import serial
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("db - Connection failed")
    return conn
try:
    ser = serial.Serial('/dev/ttyACM1',9800,timeout=1)
    try:
        database = r"/home/georgi/Documents/e_live/db.sqlite3"
        conn = create_connection(database)
    except Error as e:
        print(e)
    print("Connected")
    a = ser.read()
    while True:
        a = ser.read()
        value = a.decode("utf-8")
        if value == 'O':
            cur = conn.cursor()
            cur.execute("UPDATE el_webI_component_status SET status = true WHERE cid_id = 1")
            conn.commit()
            print("ON")
        elif value == 'F':
            cur = conn.cursor()
            cur.execute("UPDATE el_webI_component_status SET status = false WHERE cid_id = 1")
            conn.commit()
            print("OFF")
    conn.close()
except :
    print("Connection error")


