from tkinter import *   # importing all of tkinters tools

# <=======================TOP NAVIGATION NAVIGATIONS======================>

# Navigating to the Register form page
def MemRegister():
    help_window.destroy()
    import registerform


# Navigating to the Search page
def Search():
    help_window.destroy()
    import search

# Navigating to the Fitness form page
def Fitness():
    help_window.destroy()
    import fitness

# Navigating to the Main screen page
def Home():
    help_window.destroy()
    import main


help_window = Tk()   # Creating the window
help_window.title('Help Page')  # Giving the title for the window
help_window.geometry('1260x890')    # Giving the window a size that includes width and height
help_window.config(bg='#0B5A81')    # Making the background into a royal blue using HEX numbers

# Assigning variables to define the window width and height:
screen_width = help_window.winfo_screenwidth()
screen_height = help_window.winfo_screenheight()
width = 1660
height = 1100
# Making the window non-adjustable
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
help_window.geometry('%dx%d+%d+%d' % (width, height, x, y))
help_window.resizable(0, 0)

# Font type and size
f = ('Times', 14)


# <=======================================================HOW TO USE APPLICATION DESCRIPTION:==============================================================>

# Homepage Frame 
Home_Frame = Frame(
    help_window,
    bd=2,
    relief=SOLID,
    width=720,
    height=300
)
Home_Frame.place(x=70, y=100)

# Top black box within Home Frame
Black_top_frame = Frame(
    Home_Frame,
    relief=SOLID,
    bg='#363232',
    width=716,
    height=25,
)
Black_top_frame.place(x=0, y=0)

# Homepage Label
home_page_label = Label(Home_Frame, text='HOME PAGE', bg='#363232', fg='white')
home_page_label.place(x=300, y=0)

# What will appear on the page
What_will_appear_label = Label(Home_Frame, text='What to expect:', font=('bold', 15))
What_will_appear_label.place(x=10, y=30)

# Home Option Description:
Home_page_description = Label(Home_Frame, text='* A greeting that welcomes you to the application and questions you on what you are selecting today')
Home_page_description.place(x=10, y=50)

Home_page_description1 = Label(Home_Frame, text='* Main Page showing 5 options that includes register, fitness, help, search and exit')
Home_page_description1.place(x=10, y=70)

# How it works: 
How_it_works = Label(Home_Frame, text='How it Works??', font=('bold', 15))
How_it_works.place(x=10, y=110)

Home_tutorial = Label(Home_Frame, text='* You can select one of the 5 options given to you.')
Home_tutorial.place(x=10, y=130)

Home_tutorial1 = Label(Home_Frame, text='* The options are: Register, Fitness, Help, Search and Exit')
Home_tutorial1.place(x=10, y=150)

Home_tutorial2 = Label(Home_Frame, text='* By clicking one option from the home page, you can navigate to more windows from the one you are/were/was in.')
Home_tutorial2.place(x=10, y=170)

# <========================================================REGISTER PAGE DESCRIPTION:==================================================================>

# Register Page Frame
Register_Page_Frame = Frame(
    help_window,                            
    bd=2,
    relief=SOLID,
    width=720,
    height=300
)

Register_Page_Frame.place(x=70, y=430)

# Top black box within Register Frame
Black_top_frame = Frame(
    Register_Page_Frame,
    relief=SOLID,
    bg='#363232',
    width=716,
    height=25,
)
Black_top_frame.place(x=0, y=0)


#  Member Register Page
Memregisterpage_text = Label(Register_Page_Frame, text='REGISTER PAGE', bg='#363232', fg='white')
Memregisterpage_text.place(x=295, y=0)

# What will appear on the page
What_will_appear_label = Label(Register_Page_Frame, text='What to expect:')
What_will_appear_label.place(x=10, y=30)

# Register Page Info Description:
registerpage_info = Label(Register_Page_Frame,
                          text='* When you clicked on the register button, it will direct you to the register page.')
registerpage_info.place(x=5, y=60)
registerpage1_info = Label(Register_Page_Frame,
                           text='* In the top frame, you will see a registration form that displays entry boxes, radio buttons and checkboxes.')
                           
registerpage1_info.place(x=5, y=80)
registerpage2_info = Label(Register_Page_Frame, text='* In the bottom frame, a total section is displayed where it shows caluclated cost when the calculate button is clicked')
registerpage2_info.place(x=5, y=100)

registerpage3_info = Label(Register_Page_Frame, text='* The View Button is located at the bottom of the page that is in between clear and calculate buttons.')
registerpage3_info.place(x=5, y=120)

# How it works: 
How_it_works2 = Label(Register_Page_Frame, text='How it Works??')
How_it_works2.place(x=10, y=160)

How_it_works_register_description = Label(Register_Page_Frame, text='* For the view button that is in the register page, the view button is used to give a user input summary')
How_it_works_register_description.place(x=10, y=180)

How_it_works_register_description2 = Label(Register_Page_Frame, text='* You will see fields to select and fill in and when you have filled in and selected optional fields,')
How_it_works_register_description2.place(x=10, y=205)

How_it_works_register_description3 = Label(Register_Page_Frame, text='hit register and your information you have submitted will be transmitted to the database for the search page.')
How_it_works_register_description3.place(x=10, y=225)

How_it_works_description4 = Label(Register_Page_Frame, text='* For the calculate button, the button is used to calculate selected cost and displyed in the total section')
How_it_works_description4.place(x=10, y=250)

# <========================================================SEARCH PAGE DESCRIPTION:==================================================================>

# Search Page Frame
Search_Frame = Frame(
    help_window,
    bd=2,
    relief=SOLID,
    width=720,
    height=300
)

# Top black box within Search Frame
Black_top_frame = Frame(
    Search_Frame,
    relief=SOLID,
    bg='#363232',
    width=716,
    height=25,
)
Black_top_frame.place(x=0, y=0)
Search_Frame.place(x=70, y=760)

# Search Page Label
SearchPageLabel = Label(Search_Frame, text='SEARCH PAGE', font=f, bg='#363232', fg='white')
SearchPageLabel.place(x=295, y=0)

# What will appear on the page
What_will_appear_label = Label(Search_Frame, text='What to expect:')
What_will_appear_label.place(x=10, y=30)

Search_Page_Description = Label(Search_Frame, text='* There will be a text box where you will be able to search for a user in the database ')
Search_Page_Description.place(x=10, y=60)
Search_Page_Description1 = Label(Search_Frame, text='along with a search button next to it.')
Search_Page_Description1.place(x=10, y=80)

Search_Page_Description2 = Label(Search_Frame, text='* Below the search box will be a database table where you can check registered users')
Search_Page_Description2.place(x=10, y=110)
Search_Page_Description3 = Label(Search_Frame, text=' without having to go into a database editor/application.')
Search_Page_Description3.place(x=6, y=130)

# How it works: 
How_it_works3 = Label(Search_Frame, text='How it Works??')
How_it_works3.place(x=10, y=170)

How_it_works_description = Label(Search_Frame, text='* In order for you to see the registered users,')
How_it_works_description.place(x=10,y=190)
How_it_works_description1 = Label(Search_Frame, text='you can press the display all button to diaplay all registered users')
How_it_works_description1.place(x=10, y=210)

How_it_works_description2 = Label(Search_Frame, text='* If you want to search one specific name, ')
How_it_works_description2.place(x=10, y=240)

How_it_works_description3 = Label(Search_Frame, text='you can enter a persons firstname and the database treeview will show the persons first name and more details.')
How_it_works_description3.place(x=10, y=260)
# <========================================================FITNESS PAGE DESCRIPTION:==================================================================>

# Fitness Page Frame
Fitness_Frame = Frame(
    help_window,
    bd=2,
    relief=SOLID,
    width=720,
    height=300
)

# Top black box within Fitness Page Frame
Black_top_frame = Frame(
    Fitness_Frame,
    relief=SOLID,
    bg='#363232',
    width=716,
    height=25,
)
Black_top_frame.place(x=0, y=0)
Fitness_Frame.place(x=900, y=100)

# Fitness Page Label
SearchPageLabel = Label(Fitness_Frame, text='FITNESS PAGE', font=f, bg='#363232', fg='white')
SearchPageLabel.place(x=295, y=0)

# What will appear on the page
What_will_appear_label = Label(Fitness_Frame, text='What to expect:')
What_will_appear_label.place(x=10, y=30)

fitness_description = Label(Fitness_Frame, text='* You will see three different types of fintess classess')
fitness_description.place(x=10, y=50)
fitness_description2 = Label(Fitness_Frame, text='* A Database treeviewer')
fitness_description2.place(x=10, y=70)
fitness_description3 = Label(Fitness_Frame, text='* A first and last name text boxes')
fitness_description3.place(x=10, y=90)

# How it works: 
How_it_works3 = Label(Fitness_Frame, text='How it Works??')
How_it_works3.place(x=10, y=130)

How_it_works_fitness_descpription1 = Label(Fitness_Frame, text='* You fill out your first and last name, then you choose one of the three fitness classess provided.')
How_it_works_fitness_descpription1.place(x=10, y=150)
How_it_works_fitness_descpription2 = Label(Fitness_Frame, text='* Next you register your first name and last name including your fitness option')
How_it_works_fitness_descpription2.place(x=10, y=170)
How_it_works_fitness_descpription2_continuing = Label(Fitness_Frame, text='It will register you into the fitness database table')
How_it_works_fitness_descpription2_continuing.place(x=10, y=190)
How_it_works_fitness_descpription3 = Label(Fitness_Frame, text='* To see the registered data in the treeviewer, you can press the display all button')
How_it_works_fitness_descpription3.place(x=10, y=210)
How_it_works_fitness_descpription3 = Label(Fitness_Frame, text='* If you are looking for a specific name, type in that persons first name in the search box')
How_it_works_fitness_descpription3.place(x=10, y=230)

# <========================================================BULTIN SQLITE3 DATABASE VIEWER DESCRIPTION:==================================================================>

# SQLite3 Database Viewer Frame
SQLite_Builtin_Viewer_Frame = Frame(
    help_window,
    bd=2,
    relief=SOLID,
    width=720,
    height=300
)

# Top black box within SQLite3 Database Viewer frame
Black_top_frame = Frame(
    SQLite_Builtin_Viewer_Frame,
    relief=SOLID,
    bg='#363232',
    width=716,
    height=25,
)
Black_top_frame.place(x=0, y=0)
SQLite_Builtin_Viewer_Frame.place(x=900, y=430)

# BuiltIn SQLite Viewer Label
SearchPageLabel = Label(SQLite_Builtin_Viewer_Frame, text='BUILT-IN SQLITE3 DATABASE VIEWER', font=f, bg='#363232', fg='white')
SearchPageLabel.place(x=230, y=0)

SQlite3_description = Label(SQLite_Builtin_Viewer_Frame, text='What to expect?:')
SQlite3_description.place(x=10, y=30)

SQlite3_description1 = Label(SQLite_Builtin_Viewer_Frame, text='* In visual studio code, it shows you your database table. The icon is pink and should have a file format .db')
SQlite3_description1.place(x=10, y=60)

# How to get it: 
How_to_get_it = Label(SQLite_Builtin_Viewer_Frame, text='How to install it:')
How_to_get_it.place(x=10, y=90)

tutorial1 = Label(SQLite_Builtin_Viewer_Frame, text='* In Visual Studio Code, go to Extensions, search SQLite Viewer')
tutorial1.place(x=10, y=110)

tutorial2 = Label(SQLite_Builtin_Viewer_Frame, text='* You should see the SQLite Viewer that has a light blue database icon with a dark blue feather')
tutorial2.place(x=10, y=130)

tutorial3 = Label(SQLite_Builtin_Viewer_Frame, text='* The owner is Florian Klampfer who is verified and has a 5 star rating ')
tutorial3.place(x=10, y=150)

tutorial4 = Label(SQLite_Builtin_Viewer_Frame, text='* Once you have installed the Sqlite Viewer for Visual Studio Code, attempt to open a database when you ')
tutorial4.place(x=10, y=170)

tutorial5 = Label(SQLite_Builtin_Viewer_Frame, text='have filled the fitness class contents')
tutorial5.place(x=10, y=190)

tutorial6 = Label(SQLite_Builtin_Viewer_Frame, text='* One you registered your information, you should see a pink database icon in explorer on your left hand side.')
tutorial6.place(x=10, y=210)

tutorial7 = Label(SQLite_Builtin_Viewer_Frame, text='The file is in a database format thats called .db ')
tutorial7.place(x=10, y=230)

# <========================================================TOP NAVIAGTION BUTTONS:==================================================================>

# Home Button
HomeButton = Button(help_window, text='Home',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Home, width=20, height=1)
HomeButton.place(x=40, y=0.5)

# Search Button
SearchButton = Button(help_window, text='Search',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Search, width=20, height=1)
SearchButton.place(x=460, y=0.5)

# Fitness Button
FinessButton = Button(help_window, text='Fitness',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Fitness, width=20, height=1)
FinessButton.place(x=900, y=0.5)

# Register form Button
RegisterFormButton = Button(help_window, text='Register',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=MemRegister, width=20, height=1)
RegisterFormButton.place(x=1350, y=0.5)

help_window.mainloop()