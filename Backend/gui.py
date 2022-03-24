from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar 



root = Tk()

def room4all():
    root.title("Informações - Termo de Penhora")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Label - Input
    led = ttk.Label(mainframe, text='Tipo de Sala: ')
    led1 = ttk.Label(mainframe, text="Dia: ")
    led2 = ttk.Label(mainframe, text="Horário de Início: ")
    led3 = ttk.Label(mainframe, text="Horário de Término: ")
    #led4 = ttk.Label(mainframe, text="Número do CRI: ")

    ed = ttk.Entry(mainframe, textvariable=1)
    ed1 = ttk.Entry(mainframe,)
    ed2 = ttk.Entry(mainframe,)
    ed3 = ttk.Entry(mainframe,)
    #ed4 = ttk.Entry(mainframe,)

    led.grid(row=0, column=0, sticky=W)
    led1.grid(row=1, column=0, sticky=W)
    led2.grid(row=2, column=0, sticky=W)
    led3.grid(row=3, column=0, sticky=W)
    #led4.grid(row=4, column=0, sticky=W)
    ed.grid(row=0, column=1, sticky=W)
    ed1.grid(row=1, column=1, sticky=W)
    ed2.grid(row=2, column=1, sticky=W)
    ed3.grid(row=3, column=1, sticky=W)
    #ed4.grid(row=4, column=1, sticky=W)
    

    def room():
        room_type = ed.get()
        date = ed1.get()
        time_init = ed2.get()
        time_end = ed3.get()
        #CRI = ed4.get()
        print(room_type, date, time_init, time_end)
        root.quit()
        return room_type, date, time_init, time_end

    def exit():
        root.quit()


    bt = ttk.Button(mainframe, text="Reservar", command=room)
    bt.grid(row=5, column=1)
    bt1 = ttk.Button(mainframe, text="Ver salsas", command=exit)
    bt1.grid(row=9, column=1)

    ed5 = ttk.Label(mainframe, text="Qualquer mensagem para o usuário")
    ed5.grid(row=7, columnspan=2)

    root.bind('<Return>', ttk.Button)

    root.mainloop()
    return imovel()
root.quit()

room4all()
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color
#from tkcalendar import Calendar

root = Tk()

def room4all():
    root.title("Informações - Termo de Penhora")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Label - Input
    led = ttk.Label(mainframe, text='Tipo de Sala: ')
    led1 = ttk.Label(mainframe, text="Dia: ")
    led2 = ttk.Label(mainframe, text="Horário de Início: ")
    led3 = ttk.Label(mainframe, text="Horário de Término: ")
    #led4 = ttk.Label(mainframe, text="Número do CRI: ")
    
    text = StringVar(mainframe)
    text.set('Choices')
    rooms = ['Smart - 3 pessoas', 'Standar - 6 pessoas', 'Super - 8 pessoas']
    ed = ttk.OptionMenu(mainframe, text, *rooms)
    
    textd = StringVar(mainframe)
    textd.set('Dias')
    dates = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
    ed1 = ttk.OptionMenu(mainframe, textd, *dates)
    
    text2 = StringVar(mainframe)
    text2.set('Horas')
    rooms2 = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '13:00', '14:00', '15:00', '16:00', '17:30', '18:00', '19:30', '20:00', '21:00'  ]
    ed2 = ttk.OptionMenu(mainframe, text2, *rooms2)
    
    text3 = StringVar(mainframe)
    text3.set('Horas')
    rooms3 = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '13:00', '14:00', '15:00', '16:00', '17:30', '18:00', '19:30', '20:00', '21:00'  ]
    ed3 = ttk.OptionMenu(mainframe, text3, *rooms3)
    #ed4 = ttk.Entry(mainframe,)
    
    led.grid(row=0, column=0, sticky=W)
    led1.grid(row=1, column=0, sticky=W)
    led2.grid(row=2, column=0, sticky=W)
    led3.grid(row=3, column=0, sticky=W)
    #led4.grid(row=4, column=0, sticky=W)
    ed.grid(row=0, column=1, sticky=W)
    ed1.grid(row=1, column=1, sticky=W)
    ed2.grid(row=2, column=1, sticky=W)
    ed3.grid(row=3, column=1, sticky=W)
    #ed4.grid(row=4, column=1, sticky=W)
    

    def room():
        room_type = text.get()
        date = textd.get()
        time_init = text2.get()
        time_end = text3.get()
        #CRI = ed4.get()
        print(room_type, date, time_init, time_end)
        #root.quit()
        return room_type, date, time_init, time_end

    def exit():
        root.quit()


    bt = ttk.Button(mainframe, text="Reservar", command=room)
    bt.grid(row=5, column=1)
    bt1 = ttk.Button(mainframe, text="Ver salsas", command=exit)
    bt1.grid(row=9, column=1)

    ed5 = ttk.Label(mainframe, text="Qualquer mensagem para o usuário")
    ed5.grid(row=7, columnspan=2)

    root.bind('<Return>', ttk.Button)

    root.mainloop()
    return imovel()
root.quit()

