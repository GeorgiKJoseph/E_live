import serial
import sqlite3
from sqlite3 import Error
import environment as env

db_up_limit = 0
# Base directory address
BASE_DIR = env.getBaseDir()

# Connects to the Database
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except:
        print("db - Connection failed")
    return conn

# Main
if __name__ == "__main__":
    # Connecting to Serial port
    try:
        print("Connecting to " + env.getSerialPort())
        ser = serial.Serial(env.getSerialPort(),9600,timeout=1)
        print("Connected")
    except:
        print("Unable to connect, Check connection...")
        exit()

    # Connecting to Database
    try:
        print("Waiting for database connection")
        database = BASE_DIR + "/e_live/db.sqlite3"
        conn = create_connection(database)
        print("Connection established...")
    except Error as e:
        print("Connection error...")
        print(e)
        exit()

    a = ser.readline()
    while True:
        a = ser.readline()
        value = a.decode("utf-8")
        if value == 'O\n':
            cur = conn.cursor()
            cur.execute("UPDATE el_webI_component_status SET status = 1 WHERE cid_id = 1;")
            conn.commit()
            print("ON")
        elif value == 'F\n':
            cur = conn.cursor()
            cur.execute("UPDATE el_webI_component_status SET status = 0 WHERE cid_id = 1;")
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



