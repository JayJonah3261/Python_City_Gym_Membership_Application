from tkinter import *
from tkinter import font


def MemRegister():
    login_window.destroy()
    import registerform


def Search():
    login_window.destroy()
    import search


def Fitness():
    login_window.destroy()
    import fitness


def HELP():
    login_window.destroy()
    import help


# GUI Part
login_window = Tk()
login_window.title('Home Page')
login_window.geometry('601x400')
login_window.config(bg='#0B5A81')

# Font type and size
f = ('Times', 15,)

# Background Image
#img = PhotoImage(file='Gym home background.png')
#label = Label(login_window, image=img)
#label.place(x=0, y=0)

heading = Label(login_window, text='Welcome to City Gym Fitness',font= ("Times New Roman", 40, "bold"), bg='#0B5A81', fg='white')
heading.place(x=10, y=5)

heading2 = Label(login_window, text='What would you like to select today?', font=("Georgia", 20, "bold"), bg='#0B5A81', fg='white')
heading2.place(x=180, y=110)

RegisterButton = Button(login_window, text='Register',font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=MemRegister)
RegisterButton.place(x=370, y=170)

FitnessButton = Button(login_window, text='Fitness',font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=Fitness)
FitnessButton.place(x=390, y=210)

SearchButton = Button(login_window, text='Search',font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=Search)
SearchButton.place(x=410, y=250)

HelpButton = Button(login_window, text='Help', font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=HELP)
HelpButton.place(x=430, y=290)

ExitButton = Button(login_window, text='Exit',font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=exit)
ExitButton.place(x=450, y=330)

login_window.mainloop()

#Arial (corresponds to Helvetica), Courier New (Courier), Comic Sans MS, Fixedsys, MS Sans Serif, MS Serif, Symbol, System, Times New Roman (Times), and Verdana
