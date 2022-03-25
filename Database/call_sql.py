import mysql.connector
from datetime import datetime

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
    cursor.execute("INSERT IGNORE INTO room VALUES (5, %s)", y)

def datetime_reservation(start):
    res = ' '.join(map(str, start))
    print(res)

"""
def add_id(y):
    cursor.execute("INSERT IGNORE INTO room4all.reservation (id_reservations) VALUE (4)", )

def add_start(time):
    cursor.execute("INSERT IGNORE INTO room4all.reservation (start) VALUE (%s)", time)

def add_end(time):
    cursor.execute("INSERT IGNORE INTO room4all.reservation (end) VALUE (%s)", time)

def add_room(y):
    cursor.execute("INSERT IGNORE INTO room4all.reservation (id_room) VALUE (%s)", y)
    for x in cursor:
        print(x)


def add_reserve(x, y, time, end):
    add_id([x])
    add_start([time])
    add_end([end])
    add_room([y])
    for z in cursor:
        print(z)
"""

def add_reservation(start):
    cursor.execute("INSERT IGNORE INTO reservation values (0, %s, 2022-03-25, 2)", start)
    #for x in cursor:
     #   print(x)

def remove_reservation(y):
    cursor.execute("DELETE FROM reservation WHERE id_room=%s", y)
    #for x in cursor:
     #   print(x)

time = datetime(2022, 3, 25, 10, 0)
end = datetime(2022, 3, 25, 11, 0)

remove_reservation([2])

def get_meetings():
    cursor.execute("SELECT * FROM reservation")
    for x in cursor:
        print(x)

get_meetings()

db.commit()
