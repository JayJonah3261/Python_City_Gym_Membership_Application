from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter.ttk import Treeview


search_window = Tk()    # Creating the window
search_window.title('Search Page')  # Giving the title for the window
search_window.config(bg='#0B5A81')  # Making the background into a royal blue using HEX numbers

# Assigning variables to define the window width and height:
screen_width = search_window.winfo_screenwidth()    
screen_height = search_window.winfo_screenheight()
width = 1170
height = 560
# Making the window non-adjustable
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
search_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
search_window.resizable(0, 0)

# <=======================TOP NAVIGATION NAVIGATIONS======================>

# Navigating to the Register Form page
def MemRegister():
    search_window.destroy()
    import registerform

# Navigating to the Main Screen Page
def Home():
    search_window.destroy()
    import main

# Navigating to the Help Page
def Help():
    search_window.destroy()
    import help

# Navigating to the Fitness Form Page
def Fitness():
    search_window.destroy()
    import fitness

# <========================DATABASE=======================>
# Connecting to the Database
def Database():
    global conn, cursor
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()

# Defining a function to search the data in the database
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SearchBox.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with 'where' clause(Can be id, firstname or or and lastname you're searching for)
        cursor=conn.execute("SELECT * FROM User_Registration WHERE MemberID LIKE ?", ('%' + str(SearchBox.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        

#Function for exiting the application
def Exit():
    O = messagebox.askyesno("Search Page", "Do you want to exit the app?")
    if O > 0:
        search_window.destroy()
    return

#Delete selected row in the treeview connected to the database
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
    cursor.execute("DELETE FROM `User_Registration` WHERE `MemberID` = %d" % item[0])
    connectn.commit()
    cursor.close()
    connectn.close()

 # Database Tabe creation
 #==================================TREEVIEW============================================
def populateView():
    Database()
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM User_Registration ORDER BY `lastname` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], data[10], data[11]))
    cursor.close()
    conn.close()
Body = Frame(search_window)
Body.place(x=100, y=250, width=850, height=190)
 
# DIsplay All button to display registered data from the database
btn_display = Button(width=10,font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", text="Display All", command=populateView)
btn_display.place(x=970, y=290)
 
 
#==================================LIST WIDGET========================================
scrollbary = Scrollbar(Body, orient=VERTICAL)
scrollbarx = Scrollbar(Body, orient=HORIZONTAL)
tree = Treeview(Body, columns=("Id", "Firstname", "Lastname", "Address", "PhoneNumber", "BaseMembershipCost", "ExtraCosts", "TotalDiscount", "NetMembershipCost", "RegularPaymentAmount", "FrequencyOfPayment", "MethodOfPayment"), yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set, selectmode='extended')
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

#  Treeview Headings
tree.heading('Id', text="Id", anchor=W)
tree.heading('Firstname', text="Firstname", anchor=W)
tree.heading('Lastname', text="Lastname", anchor=W)
tree.heading('Address', text="Address", anchor=W)
tree.heading('PhoneNumber', text="PhoneNumber", anchor=W)
tree.heading('BaseMembershipCost', text="BaseMembershipCost", anchor=W)
tree.heading('ExtraCosts', text="ExtraCosts", anchor=W)
tree.heading('TotalDiscount', text="TotalDiscount", anchor=W)
tree.heading('NetMembershipCost', text="NetMembershipCost", anchor=W)
tree.heading('RegularPaymentAmount', text="RegularPaymentAmount", anchor=W)
tree.heading('FrequencyOfPayment', text="FrequencyOfPayment", anchor=W)
tree.heading('MethodOfPayment', text="MethodOfPayment", anchor=W)

# Treeview columns
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=80)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=90)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=30)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=80)
tree.column('#8', stretch=NO, minwidth=0, width=120)
tree.column('#9', stretch=NO, minwidth=0, width=90)
tree.column('#10', stretch=NO, minwidth=0, width=80)
tree.column('#11', stretch=NO, minwidth=0, width=30)
tree.pack()

# <=========================================================================================>


# Search Number Text
SearchNumberLabel = Label(search_window, text='Input a number',font=('bold', 20), bg="#0B5A81", fg="white")
SearchNumberLabel.place(x=300, y=150)

# Search Bar
SearchBox = Entry(search_window)
SearchBox.place(x=300, y=200)

# Search Button
SearchButton = Button(search_window, text='Search',font=('Calibri', 16, 'bold'), fg="black", bg="#ed5e68", command=SearchRecord)
SearchButton.place(x=520, y=200)

# Delete Button
DeleteButton = Button(search_window, text='Delete', font=('Calibri', 17, 'bold'), command=Delete,
fg="black", bg="#ed5e68").place(x=970, y=340)

# Exit Button
Exit_Button = Button(search_window, text='Exit System', font=('Calibri', 17, 'bold'), command=Exit,
fg="black", bg="#026b54").place(x=490, y=500)

# <=========================TOP NAVIGATION BUTTONS===================================>

# Home Button
HomeButton = Button(search_window, text='Home',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Home, width=20, height=1)
HomeButton.place(x=10, y=0.5)

# Help Button
HelpButton = Button(search_window, text='Help',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Help, width=20, height=1)
HelpButton.place(x=300, y=0.5)

# Register Button
RegisterButton = Button(search_window, text='Register',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=MemRegister, width=20, height=1)
RegisterButton.place(x=590, y=0.5)

# Fitness Button
FitnessCLassButton = Button(search_window, text='Fitness',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Fitness, width=20, height=1)
FitnessCLassButton.place(x=910, y=0.5)

search_window.mainloop()
