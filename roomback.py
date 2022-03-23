# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    roomback.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jbuny-fe <jbuny-fe@student.42lisboa.com>   +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/03/23 18:31:10 by jbuny-fe          #+#    #+#              #
#    Updated: 2022/03/23 20:05:06 by jbuny-fe         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #


# pensar na possibilidade de acrescentar rooms

import toml
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
        self.room = {"sala a": [8, 9, 10, 11], "sala b": [4, 5, 6]}
        self.people = None
        self.timeInit = None
        self.timeEnd = None
        self.show_available()
        self.input_user()
        
    def input_user(self):
        request = str(input("Deseja reservar alguma sala (yes/no)? ")).lower()
        if request.lower() == "yes":
            self.input_reservation()
        elif request.lower() == "no":
            print("Have a nice day without a room ;)")
        else:
            print("Error - Input")
            self.__init__()

    def input_reservation(self):
        self.people = input("Quantas pessoas para a reunião: ")
        self.timeInit = int(input("Horário de início: "))
        self.timeEnd = input("Horário de termino: ")
        self.looking_for_room()

    def show_available(self):
        print("As salas disponíveis são:") # checkar se há disponíveis antes de imprimir
        try:
            with open ("rooms", 'r') as f:
                tk = toml.load(f)
                self.sala_a = list(tk["sala_a"])
                self.sala_b = list(tk["sala_b"])
                f.close()
                print(f"A sala a tem {self.sala_a} horários livres")
                print(f"A sala a tem {self.sala_b} horários livres")
        except:
            pass
            #with open("rooms", 'w') as f:
                #sala_a = [8, 9, 10, 11]
                #sala_b = [4, 5, 6]
                #f.write('sala_a = ' + str(int(sala_a)) + '\n')
                #f.write('sala_b = ' + str(int(sala_b)) + '\n')
                #f.close()

        for i in self.room:
            print(i, self.room[i])
    
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
        self.sala_a.remove(val)
        print(self.sala_a)
        with open("rooms", 'w') as f:
                f.write('sala_a = ' + str(self.sala_a) + '\n')
                f.write('sala_b = ' + str(self.sala_b) + '\n')
                f.close()
        print(f"O horário {val} da {key} foi reservado com sucesso")
        self.show_available()
         
