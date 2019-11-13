import serial
import sqlite3
from sqlite3 import Error

db_up_limit = 0
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("db - Connection failed")
    return conn
try:
    ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
    try:
        database = r"/home/georgi/Documents/e_live/db.sqlite3"
        conn = create_connection(database)
    except Error as e:
        print(e)
    print("Connected")
    a = ser.readline()
    while True:
        a = ser.readline()
        value = a.decode("utf-8")
        if value == 'O\n':
            cur = conn.cursor()
            cur.execute("UPDATE el_webI_component_status SET status = true WHERE cid_id = 1")
            conn.commit()
            print("ON")
        elif value == 'F\n':
            cur = conn.cursor()
            cur.execute("UPDATE el_webI_component_status SET status = false WHERE cid_id = 1")
            conn.commit()
            print("OFF")
        else:  
            db_up_limit +=1         
            try:
                if db_up_limit >= 4:
                    cur = conn.cursor()
                    v = float(value)
                    comd = 'UPDATE el_webI_component_status SET current='+  str(v) + ' WHERE cid_id = 1;'
                    cur.execute(comd)
                    conn.commit()
                    db_up_limit=0
            except:
                pass
    conn.close()
except :
    print("Connection error")


