'''
Serial port input format

{"InfoType":"StatusInfo","BoardNo":"1","DeviceNo":1,"Status":true}
{"InfoType":"PowerInfo","BoardNo":"1","AmpsRMS":1.056869}
'''

import serial
import time
import json
import sqlite3
from sqlite3 import Error
import environment as env

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


# Storing status logs into logs/devicestatus.log
def log_status(boardNo, deviceNo, status):
    f = open("logs/devicestatus.log", "a")
    instant = str(time.ctime())
    inp_string = instant+', board: '+boardNo+', dev: '+str(deviceNo)+', status: '+status+'\n'
    f.write(inp_string)
    f.close()
    print(inp_string)


# Storing energy logs into logs/energymeter.log
def log_energy(boardNo, AmpsRMS):
    f = open("logs/energymeter.log", "a")
    instant = str(time.ctime())
    inp_string = instant+', board: '+boardNo+',AmpsRMS: '+AmpsRMS+'\n'
    f.write(inp_string)
    f.close()
    print(inp_string)


# Update device status into database
def updateStatus(conn,BoardNo, DeviceNo, status):
    cur = conn.cursor()
    #
    # By default BoardNo and DeviceNo is set to 1,
    # Change it to corresponding variables in production
    if status == 'On':
        cmd = "UPDATE el_webI_component_data SET status = 1 WHERE deviceNo = "+DeviceNo+" AND boardNo_id = "+BoardNo+" ;"
    else:
        cmd = "UPDATE el_webI_component_data SET status = 0 WHERE deviceNo = "+DeviceNo+" AND boardNo_id = "+BoardNo+" ;"
    cur.execute(cmd)
    conn.commit()


# Update power info into database
def updatePower(conn,BoardNo,AmpsRMS):
    cur = conn.cursor()
    cmd = 'UPDATE el_webI_board SET instant_power='+  str(AmpsRMS * 220) + ' WHERE boardNo = 1;'
    cur.execute(cmd)
    conn.commit()


# Main
if __name__ == "__main__":
    # Connecting to Serial port
    try:
        print("Connecting to " + env.getSerialPort())
        ser = serial.Serial(env.getSerialPort(),19200,timeout=1)
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

    while True:
        #
        # Loops until a valid input is recieved
        inp_validity = True
        while inp_validity:
            a = ser.readline()
            value = a.decode("utf-8")
            try:
                info = json.loads(value)
                inp_validity = False
            except:
                print("Miss: incomplete JSON")
        #
        # Logs device data to logs/...
        if info.get("InfoType") == 'PowerInfo':
            log_energy(info["BoardNo"], str(info["AmpsRMS"]))

        elif info.get("InfoType") == 'StatusInfo':
            if info["Status"]:
                status = 'On'
            else:
                status = 'Off'
            log_status(info["BoardNo"],info["DeviceNo"],status)
        #
        # Updating Device status & Energy info to Database
        if info.get("InfoType") == 'PowerInfo':
            updatePower(conn,info["BoardNo"],info["AmpsRMS"])
        elif info.get("InfoType") == 'StatusInfo':
            updateStatus(conn,info["BoardNo"],str(info["DeviceNo"]),status)

    conn.close()
