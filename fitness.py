from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview

fitness_window = Tk()   # Creating the window
fitness_window.title('Fitness Page')    # Giving the title for the window
fitness_window.geometry('1380x1300')    # Giving the window a width and a height
fitness_window.config(bg='#0B5A81') # Making the background into a royal blue using HEX numbers


# <=======================TOP NAVIGATION NAVIGATIONS======================>

# Navigating to the Register Form page
def MemRegister():
    fitness_window.destroy()
    import registerform

# Navigating to the Search Page
def Search():
    fitness_window.destroy()
    import search

# Navigating to the Help Page
def HELP():
    fitness_window.destroy()
    import help

# Navigating to the Main Screen Page
def Home():
    fitness_window.destroy()
    import main


# <======================================IMAGES===========================================>

# Cardio Image:
img = PhotoImage(file='Cardio animation.png')
label = Label(fitness_window, image=img)
label.place(x=15, y=360)

# Pilates Image:
img2 = PhotoImage(file='Pilates animation.png')
label1 = Label(fitness_window, image=img2)
label1.place(x=475, y=360)

# Spin Class:
img3 = PhotoImage(file='Spin fitness animation.png')
label2 = Label(fitness_window, image=img3)
label2.place(x=935, y=360)

# Font type and size
f = ('Times', 14)

# Variables:
cardio_var = StringVar()
cardio_var.set('0')
pilates_var = StringVar()
pilates_var.set('0')
spin_var = StringVar()
spin_var.set('0')
Fitness_class_options = StringVar()
Fitness_class_options.set('')

# Grouping Variables
Fitness_class_options = cardio_var and pilates_var and spin_var

# <======================================DATABSE===========================================>

def Database():
    global conn, cursor
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()

# <======================================REGISTERING USERS AND DAVING INTO DATABASE===========================================>

def Register():
    Database()
    firstname = FirstnameEntry.get()
    lastname = LastnameEntry.get()
    FitnessClassType = Fitness_class_options.get()

    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    table_create_query = '''CREATE TABLE IF NOT EXISTS Fitness_Data (MemberID INTEGER PRIMARY KEY AUTOINCREMENT,firstname TEXT, lastname TEXT, FitnessClassType TEXT )'''


    conn.execute(table_create_query)

    data_insert_query = '''INSERT INTO Fitness_Data (firstname, lastname, FitnessClassType) VALUES (?, ?, ?)'''

    data_insert_tuple = (firstname, lastname, FitnessClassType)

    # Check if user already exists into the Database
    cursor.execute("SELECT * FROM Fitness_Data WHERE FitnessClassType = ?", (FitnessClassType,))
    existing_user = cursor.fetchone()

    if existing_user:
            messagebox.showerror("Fitness Class Error", " You already chose a class, please select another class")
    else:
    # Insert the user's information into the database
        cursor.execute("INSERT INTO Fitness_Data (firstname, lastname, FitnessClassType) VALUES (?, ?, ?)", (firstname, lastname, FitnessClassType))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully.")

    cursor.execute(data_insert_query, data_insert_tuple)
    conn.close()
   
    
# <======================================SEARCHING DATA IN DATABASE===========================================>

#function to search data
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SearchBox.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with 'where' clause(Can be id, firstname or or and lastname you're searching for)
        cursor=conn.execute("SELECT * FROM Fitness_Data WHERE MemberID LIKE ?", ('%' + str(SearchBox.get()) + '%',))
        cursor=conn.execute("SELECT * FROM Fitness_Data WHERE firstname LIKE ?", ('%' + str(SearchBox.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()

#Function for exiting the system
def Exit():
    O = messagebox.askyesno("Search Page", "Do you want to exit the app?")
    if O > 0:
        fitness_window.destroy()
    return

#Delete query for deleting the value
def Delete():
    if not tree.selection():
        msgg = messagebox.showwarning('', 'Please Select the data!', icon="warning")
    else:
        msgg = messagebox.askquestion('', 'Are You Sure You Want To Delete', icon="warning")
    if msgg == 'yes':
        curItem = tree.focus()
        contents = (tree.item(curItem))
        item = contents['values']
        tree.delete(curItem)
    connectn = sqlite3.connect("gym.db")
    cursor = connectn.cursor()
    cursor.execute("DELETE FROM `Fitness_Data` WHERE `MemberID` = %d" % item[0])
    connectn.commit()
    cursor.close()
    connectn.close()

DeleteButton = Button(fitness_window, text='Delete', font=('Calibri', 17, 'bold'), command=Delete,
fg="black", bg="#ed5e68").place(x=1150, y=1100)

 # Database Tale
 #==================================METHODS============================================
def populateView():
    Database()
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM Fitness_Data ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3]))
    cursor.close()
    conn.close()
Body = Frame(fitness_window)
Body.place(x=250, y=1000, width=850, height=230)
DisplayData = Button(fitness_window, text='Display All', font=('Calibri', 17, 'bold'), fg="black",  bg="#ed5e68",  command=populateView)
DisplayData.place(x=1150, y=1050)

 
#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Body, orient=VERTICAL)
scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
tree = Treeview(Body, columns=("Id", "Firstname", "Lastname", "FitnessClassType"), yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set, selectmode='extended')
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('Id', text="Id", anchor=W)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('FitnessClassType', text="FitnessClassType", anchor=W)


tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=300)
tree.column('#2', stretch=NO, minwidth=0, width=300)
tree.column('#3', stretch=NO, minwidth=0, width=300)
tree.column('#4', stretch=NO, minwidth=0, width=300)
tree.pack()


# <========================================CARDIO LABELS======================================================>
# Cardio Option:
CardioButton = Radiobutton(fitness_window, variable=Fitness_class_options, text='Cardio', value='Cardio Class Thursday 3 pm - 5pm', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
CardioButton.place(x=170, y=630)

# Day: Thursday Label
CardioThursday = Label(fitness_window, text='Day: Thursday', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
CardioThursday.place(x=160, y=670)

# Time: Cardio Time Label
CardioTime = Label(fitness_window, text='Time: 3 pm - 5pm', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
CardioTime.place(x=150, y=710)

# <===========================================PILATES LABELS===============================================>
# PILATES:
# Pilates Option:
PilatesButton = Radiobutton(fitness_window, text='Pilates', variable=Fitness_class_options, value='Pilates Class Friday 9 am - 11 am', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
PilatesButton.place(x=630, y=630)

# Friday Label
PilatesFriday = Label(fitness_window, text='Day: Friday', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
PilatesFriday.place(x=625, y=670)

# Pilates Time
PilatesTime = Label(fitness_window, text='Time: 9 am - 11 am', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
PilatesTime.place(x=600, y=710)

# <==========================================FIRSTNAME LABEL AND ENTRY================================================>

FirstNameLabel = Label(fitness_window, text='First Name', font=('bold', 20),  bg='#0B5A81', fg='white')
FirstNameLabel.place(x=370, y=180)
FirstnameEntry = Entry(fitness_window)
FirstnameEntry.place(x=490, y=180)

# <==========================================LASTNAME LABEL AND ENTRY================================================>
LastNameLabel = Label(fitness_window, text='Last Name', font=('bold', 20),  bg='#0B5A81', fg='white')
LastNameLabel.place(x=790, y=180)
LastnameEntry = Entry(fitness_window)
LastnameEntry.place(x=900, y=180)

# <==========================================SPIN RADIO BUTTON OPTION================================================>
# Spin Option:
SpinButton = Radiobutton(fitness_window, text='Spin', variable=Fitness_class_options, value='Spin Class Monday 2 pm - 4pm', bg='#0B5A81', fg='white',font=('Calibri', 17, 'bold'))
SpinButton.place(x=1100, y=630)

# Monday
SpinMonday = Label(fitness_window, text='Day: Monday', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
SpinMonday.place(x=1090, y=670)

# Spin Time
SpinTime = Label(fitness_window, text='Time: 2 pm - 4pm', bg='#0B5A81', fg='white', font=('Calibri', 17, 'bold'))
SpinTime.place(x=1075, y=710)

# <==========================================REGISTER BUTTON================================================>

# Register Button:
RegisterButton = Button(fitness_window, text='Register', font=('Calibri', 17, 'bold'), command=Register, width=8, height=1, fg="black", bg="#ed5e68")
RegisterButton.place(x=600, y=790)

# <==========================================SEARCH SECTION================================================>
# Search Box
SearchBox = Entry(fitness_window)
SearchBox.place(x=570, y=950)

# Search Button
SearchButton = Button(fitness_window, text='Search',font=('Calibri', 17, 'bold'), command=SearchRecord, fg="black", bg="#ed5e68") 
SearchButton.place(x=1150, y=1000)

# Search Label
SearchLabel = Label(fitness_window, text='Search by First Name', font=('Calibri', 17, 'bold'),  bg='#0B5A81', fg='white',)
SearchLabel.place(x=580, y=900)



# <=======================TOP NAVIGATION NAVIGATIONS======================>
# Home Button
HomeButton = Button(fitness_window, text='Home',font=('Calibri', 17, 'bold'),fg="black", bg="#ed5e68", command=Home, width=20, height=1)
HomeButton.place(x=10, y=0.5)

# Search Button
SearchButton = Button(fitness_window, text='Search',font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=Search, width=20, height=1)
SearchButton.place(x=390, y=0.5)

# Help Button
HelpButton = Button(fitness_window, text='Help',font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=HELP, width=20, height=1)
HelpButton.place(x=750, y=0.5)

# Register Button
RegisterButton = Button(fitness_window, text='Register Form',font=('Calibri', 17, 'bold'), fg="black", bg="#ed5e68", command=MemRegister, width=20, height=1)
RegisterButton.place(x=1095, y=0.5)

fitness_window.mainloop()
