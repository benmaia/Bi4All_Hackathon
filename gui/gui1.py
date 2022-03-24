from cProfile import label
from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color
from tkcalendar import Calendar

root = Tk()

def room4all():
    root.title("room4all")
    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    def calendar_page():
        calendarpage = Toplevel(root)
        calendarpage.title("Calendar")
        calframe = ttk.Frame(calendarpage, padding="3 3 12 12")
        calframe.grid(column=0, row=0, sticky=(N, W, E, S))
        calendarpage.columnconfigure(0, weight=1)
        calendarpage.rowconfigure(0, weight=1)
        cal = Calendar(calendarpage, selectmode = 'day')
        cal.grid(row=0,column=0)
        def grad_date():
            ed1.config(text = cal.get_date())
            calendarpage.destroy()
        confirm_date = ttk.Button(calendarpage, text="Confirmar", command=grad_date)
        confirm_date.grid(row=1, column=0, pady=10)

    # Label - Input
    led = ttk.Label(mainframe, text='Tipo de Sala: ')
    led1 = ttk.Label(mainframe, text="Dia: ")
    led2 = ttk.Label(mainframe, text="Horário de Início: ")
    led3 = ttk.Label(mainframe, text="Horário de Término: ")
    #led4 = ttk.Label(mainframe, text="Número do CRI: ")
    
    text = StringVar(mainframe)
    text.set('Choices')
    roomSs = ['Smart - 3 pessoas', 'Standar - 6 pessoas', 'Super - 8 pessoas']
    ed = ttk.OptionMenu(mainframe, text, *roomSs)
    ed1 = ttk.Button(mainframe, text="Click Here!", command=calendar_page)
    text2 = StringVar(mainframe)
    text2.set('Start Hour')
    StartHour = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00','12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00']
    ed2 = ttk.OptionMenu(mainframe, text2, *StartHour)
    EndHour = ['09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '12:30', '13:00', '13:30', '14:00', '14:30', '15:00', '15:30', '16:00', '16:30', '17:00', '17:30', '18:00', '18:30', '19:00', '19:30', '20:00', '20:30', '21:00']
    text3 = StringVar(mainframe)
    text3.set('End Hour')
    ed3 = ttk.OptionMenu(mainframe, text3, *EndHour)
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
    return room4all()
root.quit()

room4all()
