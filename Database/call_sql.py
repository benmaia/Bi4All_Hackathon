import mysql.connector
from datetime import datetime
import numpy as np

db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Pokemon69!",
        database="room4all"
        )

cursor = db.cursor()

def get_all_rooms():
    cursor.execute("SELECT * FROM room")
    for x in cursor:
        print(x)

def remove_room(y):
    cursor.execute("DELETE FROM room WHERE id=%s", y)

def add_room(y):
    cursor.execute("INSERT IGNORE INTO room (capacity) VALUE (%s)", y)

def add_reservation(id_r, start, end, room):
    cursor.execute("INSERT INTO reservation VALUES({}, '{}', '{}', {})".format(id_r, start, end, room))

def remove_reservation(y):
    cursor.execute("DELETE FROM reservation WHERE id_reservation=%s", y)

#time = datetime(2022, 3, 25, 10, 0)
#ts = time.strftime("%Y-%m-%d %H:%M")
#end = datetime(2022, 3, 25, 11, 0)
#es = end.strftime("%Y-%m-%d %H:%M")
#add_reservation(1, ts, es, 3)
#remove_reservation([3])

def get_meetings():
    cursor.execute("SELECT * FROM reservation")
    for x in cursor:
        print(x)

get_meetings()

db.commit()
