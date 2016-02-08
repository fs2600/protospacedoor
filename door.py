#!/usr/bin/python3
#authorized =['0212394425','0213660857', '0857870596','0213548985','0217342905','0067305985']

import sqlite3 as sql
from peewee import *
import sys
import time

db = SqliteDatabase('protospacedoor2.db')

class User(Model):
    name = CharField()
    last_seen = CharField()

    class Meta:
        database = db

class Keyfob(Model):
    serial = CharField()
    owner = ForeignKeyField(User, related_name='keyfobs')

    class Meta:
        database = db

db.connect()

db.create_tables([User, Keyfob])

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

#setServo(10)

def authorized(id):
    key = Keyfob.select().where(Keyfob.serial == id).get()
    # con = sql.connect('protospacedoor.db')
    # with con:
    #     cur = con.cursor()
    #     cur.execute("SELECT * FROM users WHERE keyfob = ?", (id,))
    #     row = cur.fetchone()
    #     print(row)
    # con.close()
    print(key)
    print('++++++++++' + key.serial + '________________')
    if key != None:
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
