from roomback import *
from gui import *
import os 
import threading
def say():
    os.system('say -v Joana "Bem vindo ao rumefóral"')
threading.Thread(target=say).start()
values = gui()
values.room4all()




#e1 = RoomsManagement()
#e1.new_schedule(date, room_type)
