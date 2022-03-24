from ast import Str
import toml
import os
import json
# pensar na possibilidade de acrescentar rooms



class Employee():
    def __init__(self, login, password):
        self.__login = input("login: ")
        self.__password = input("senha: ")

class Room():
    def __init__(self):
        self.capacity = None
        self.schedule_availability = []

class RoomsManagement():

    def __init__(self):
        #self.room = {"sala a": [8, 9, 10, 11], "sala b": [4, 5, 6]}
        self.people = None
        self.timeInit = None
        self.timeEnd = None
        #self.show_available()
        #self.input_user()
        

    def show_available(self):
        print("As salas disponíveis são:") # checkar se há disponíveis antes de imprimir
        try:
            os.chdir("schedules")
            with open ("schedule.txt", 'r') as s:
                lines = s.readlines()
                for line in lines:
                    if line.replace(" ", "") != "":
                        line2 = json.loads(line)
                        print(line2)
                s.close()
            os.chdir("..")
        except Exception as e:
            print(e)
            #with open("rooms", 'w') as f:
                #sala_a = [8, 9, 10, 11]
                #sala_b = [4, 5, 6]
                #f.write('sala_a = ' + str(int(sala_a)) + '\n')
                #f.write('sala_b = ' + str(int(sala_b)) + '\n')
                #f.close()

    
    def looking_for_room(self):
        j = 0
        for i in self.room.values():
            for n in i:
                if n == self.timeInit:
                    key = self.get_key(n)
                    book = input(f"A {key} está disponível para o horário {n}. Deseja reservá-la (yes/no)? ").lower()
                    if book == "yes":
                        self.book_room(key, n)
                        return
                    else:
                        return self.__init__
            print("horário indisponível")
            j += 1
    
    def get_key(self, val):
        for key, value in self.room.items():
            for n in value:
                if n == val:
                    return key
    
    def book_room(self, key, val):
        # for key, value in self.room.items():
        #     for n in value:
        #         if n == val:
        #             value.remove(n)
        #write retirando o horário selecionado
        pass

    
    def new_schedule(self, date, room, time_init, time_end):
        try:
            os.chdir("schedules")
            f = open(f"schedule.txt", 'a')
            #f.write(f"room: {room}, date: {date}, time init: {time_init}, time end: {time_end}\n")
            dict = {"room": room, "date" : date, "time_init" : time_init, "time_end" : time_end}
            f.write(json.dumps(dict)+ "\n")
            f.close()
            os.chdir("..")
        except:
            print("Could not enter directory, please try again later.")
            


        

        