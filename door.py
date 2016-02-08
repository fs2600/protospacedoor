#!/usr/bin/python3
#authorized =['0212394425','0213660857', '0857870596','0213548985','0217342905','0067305985']

import sqlite3 as sql
import sys
import time



def set(property, value):
    try:
        f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
        f.write(value)
        f.close()
    except:
        print("Error writing to: " + property + " value: " + value)


def setServo(angle):
    set("servo", str(angle))
    set("delayed", "0")
    set("mode", "servo")
    set("servo_max", "180")
    set("active", "1")

#create table for the db
# CREATE TABLE "users" (
#     "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#     "name" TEXT NOT NULL,
#     "keyfob" TEXT NOT NULL
# )


def authorized(id):
    con = sql.connect('protospacedoor.db')
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE keyfob = ?", (id,))
        row = cur.fetchone()
        print(row)
    con.close()
    if row != None:
        return True


def opendoor(seconds):
    setServo(180)
    time.sleep(seconds)
    setServo(90)


while True:
    id = input('id: ')
    if authorized(id):
        print('allowed')
        opendoor(5)

    else:
        print('**********invalid***********')
        print(id)
