from tkinter import *
from tkinter import ttk
from turtle import bgcolor, color
from roomback import *
from tkcalendar import Calendar

root = Tk()

class gui():
    def __init__(self):
        self.room_type = None
        self.date = None
        self.time_init = None
        self.time_end = None
        self.lista = []

    def room4all(self):
        root.title("Informações - Termo de Penhora")
        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        self.e1 = RoomsManagement()
        # Label - Input
        self.led = ttk.Label(mainframe, text='Tipo de Sala: ')
        self.led1 = ttk.Label(mainframe, text="Dia: ")
        self.led2 = ttk.Label(mainframe, text="Horário de Início: ")
        self.led3 = ttk.Label(mainframe, text="Horário de Término: ")
        #led4 = ttk.Label(mainframe, text="Número do CRI: ")
        
        self.text = StringVar(mainframe)
        self.text.set('Choices')
        self.rooms = ['Smart (3 pessoas)', 'Standar (6 pessoas)', 'Super (8 pessoas)']
        self.ed = ttk.OptionMenu(mainframe, self.text, *self.rooms)
        
        self.ed1 = ttk.Button(mainframe, text="Click Here!", command=self.calendar_page)
        
        self.text2 = StringVar(mainframe)
        self.text2.set('Horas')
        self.rooms2 = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '13:00', '14:00', '15:00', '16:00', '17:30', '18:00', '19:30', '20:00', '21:00'  ]
        self.ed2 = ttk.OptionMenu(mainframe, self.text2, *self.rooms2)
        
        self.text3 = StringVar(mainframe)
        self.text3.set('Horas')
        self.rooms3 = ['09:00', '09:30', '10:00', '10:30', '11:00', '11:30', '12:00', '13:00', '14:00', '15:00', '16:00', '17:30', '18:00', '19:30', '20:00', '21:00'  ]
        self.ed3 = ttk.OptionMenu(mainframe, self.text3, *self.rooms3)
        #ed4 = ttk.Entry(mainframe,)
        
        self.led.grid(row=0, column=0, sticky=W)
        self.led1.grid(row=1, column=0, sticky=W)
        self.led2.grid(row=2, column=0, sticky=W)
        self.led3.grid(row=3, column=0, sticky=W)
        #led4.grid(row=4, column=0, sticky=W)
        self.ed.grid(row=0, column=1, sticky=W)
        self.ed1.grid(row=1, column=1, sticky=W)
        self.ed2.grid(row=2, column=1, sticky=W)
        self.ed3.grid(row=3, column=1, sticky=W)
        #ed4.grid(row=4, column=1, sticky=W)

        def exit():
            self.e1.show_available()
            #root.quit()

        self.bt = ttk.Button(mainframe, text="Reservar", command=self.room)
        self.bt.grid(row=5, column=1)
        self.bt1 = ttk.Button(mainframe, text="Ver salsas", command=exit)
        self.bt1.grid(row=9, column=1)

        self.ed5 = ttk.Label(mainframe, text="Qualquer mensagem para o usuário")
        self.ed5.grid(row=7, columnspan=2)
        
        root.bind('<Return>', ttk.Button)

        root.mainloop()
        return self.lista
    root.quit()

    def room(self):
        self.room_type = self.text.get()
        self.date = self.textd.get()
        self.time_init = self.text2.get()
        self.time_end = self.text3.get()
        self.lista = [self.room_type, self.date, self.time_init, self.time_end]
        #e1 = RoomsManagement()
        self.e1.new_schedule(self.date, self.room_type, self.time_init, self.time_end)
        return self.lista

    def calendar_page(self):
        self.calendarpage = Toplevel(root)
        self.calendarpage.title("Calendar")
        self.calframe = ttk.Frame(self.calendarpage, padding="3 3 12 12")
        self.calframe.grid(column=0, row=0, sticky=(N, W, E, S))
        self.calendarpage.columnconfigure(0, weight=1)
        self.calendarpage.rowconfigure(0, weight=1)
        self.cal = Calendar(self.calendarpage, selectmode = 'day')
        self.cal.grid(row=0,column=0)
        self.print_date = ttk.Label(self.calendarpage, text='')
        self.print_date.grid(row=2, column=0, pady=10)
        def grad_date():
    	    self.print_date.config(text = self.cal.get_date())
        #confirm_date = ttk.Button(self.calendarpage, text="Confirmar", command=grad_date)
       # self.confirm_date.grid(row=1, column=0, pady=10)

