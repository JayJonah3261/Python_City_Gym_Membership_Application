from tkinter import *
from tkinter import messagebox
import sqlite3


ws = Tk()   # Creating the window
ws.title('Registration Form')   # Giving the title for the window
ws.config(bg='#0B5A81')    # Making the background into a royal blue using HEX numbers
ws.geometry('960x1040') # Making the window geometry

# Assigning variables to define the window width and height:
screen_width = ws.winfo_screenwidth()
screen_height = ws.winfo_screenheight()
width = 950
height = 1100
# Making the window non-adjustable
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
ws.geometry('%dx%d+%d+%d' % (width, height, x, y))
ws.resizable(0, 0)

# <=======================TOP NAVIGATION NAVIGATIONS======================>

# Navigating to the Main screen page
def Home():
    ws.destroy()
    import main


# Navigating to the Search Page
def Search():
    ws.destroy()
    import search

# Navigating to the Fitness Form Page
def Fitness():
    ws.destroy()
    import fitness


# Navigating to the Help Page
def HELP():
    ws.destroy()
    import help


# Font type and size
f = ('Times', 16)
# <===================================================MEMBERSHIP DETAILS RADIO BUTTONS========================================================>

# Creating a Membership Details Variable 
Membership_Details_var = StringVar()
Membership_Details_var.set('0')

# Basic Var
Membership_Details_Basic_var = IntVar()
# Membership_Details_Basic_var.set('0')

# Regular Var
Membership_Details_Regular_var = IntVar()
# Membership_Details_Regular_var.set('0')

# Premium Var
Membership_Details_Premium_var = IntVar()
# Membership_Details_Premium_var.set('0')

# Grouping Membership Details Variables
Membership_Details_var = Membership_Details_Basic_var and Membership_Details_Regular_var and Membership_Details_Premium_var

# <===================================================DURATION DETAILS RADIO BUTTONS========================================================>

# Creating a Membership Details Variable
Membership_Duration_var = StringVar()
Membership_Duration_var.set('0')

# 3 months Variable
threemonths_var = StringVar()
threemonths_var.set('0')

# 12 months Variable
twelvemonths_var = StringVar()
twelvemonths_var.set('0')

# 24 months Variable
twentyfourmonths_var = StringVar()
twentyfourmonths_var.set('0')

# Grouping Membership Duration Variables

Membership_Duration_var = threemonths_var and twentyfourmonths_var and twelvemonths_var

# <===================================================EXTRAS CHECKBOXES========================================================>

# Extras Variables (Checkboxes)
# 24/7 Access Varriable
twenty_four_seven_var = IntVar()

# Personal Trainer Variable
Personal_trainer_var = IntVar()

# Diet Consultation Variable
Diet_Consultation_var = IntVar()

# Online Access Videos Variable
Online_Access_Videos_var = IntVar()

# Grouping Extras variables

Extras_var = int(twenty_four_seven_var.get()) and int(Personal_trainer_var.get()) and int(
    Diet_Consultation_var.get()) and int(Online_Access_Videos_var.get())

# <===================================================PAYMENT OPTIONS RADIOBUTTONS========================================================>


# Membership Payment Options Variable
Membership_Payment_Options_var = StringVar()
Membership_Payment_Options_var.set('0')

# Direct Debit Variable
DirectDebit_option_var = StringVar()
DirectDebit_option_var.set('0')

# Other Option Variabe
Other_option = StringVar()
Other_option.set('0')

# Grouping Membership Payment Options Variables
Membership_Payment_Options_var = DirectDebit_option_var and Other_option

# <===================================================PAYMENT FREQUENCY RADIOBUTTONS========================================================>


# Membership Payment Frequency
Membership_Payment_Frequency_var = StringVar()
Membership_Payment_Frequency_var.set('0')

# Weekly Variable
Weekly_option_var = StringVar()
Weekly_option_var.set('0')

# Monthly Variable
Monthly_option_var = IntVar()

# Grouping Membership Payment Frequency Variables
Membership_Payment_Frequency_var = Weekly_option_var and Monthly_option_var

# # <===================================================TOP AND BOTTOM FRAMES========================================================>
# Top Frame(User Information input field)
top_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    padx=50,
    pady=100,

)

# Bottom Frame (Total section)
bottom_frame = Frame(
    ws,
    bd=2,
    bg='#CCCCCC',
    relief=SOLID,
    pady=10,
    padx=55,
)

# Form Heading
Label(
    ws,
    text='Registration Form',
    bg='#CCCCCC',
    font=("Impact",40), fg='#06689c'
).place(x=360, y=60)

# First Name Label
Label(
    top_frame,
    text="First Name",
    bg='#CCCCCC',
    font=f
).grid(row=0, column=0, sticky=W, pady=10)

# Last Name Label
Label(
    top_frame,
    text="Last Name",
    bg='#CCCCCC',
    font=f
).grid(row=1, column=0, sticky=W, pady=10)

# Address Label
Label(
    top_frame,
    text="Address",
    bg='#CCCCCC',
    font=f
).grid(row=2, column=0, sticky=W, pady=10)

# Phone Number Label
Label(
    top_frame,
    text="Phone Number",
    bg='#CCCCCC',
    font=f
).grid(row=3, column=0, sticky=W, pady=10)

# Membership Type Label
Label(
    top_frame,
    text="Membership Type:",
    bg='#CCCCCC',
    font=f
).grid(row=4, column=0, sticky=W, pady=10)

# Duration Label
Label(
    top_frame,
    text='Duration',
    bg='#CCCCCC',
    font=f
).grid(row=5, column=0, sticky=W, pady=10)

# Extras Label
Label(
    top_frame,
    text='Extras',
    bg='#CCCCCC',
    font=f
).grid(row=6, column=0, sticky=W, pady=10)

# Payment Frequency Label
Label(
    top_frame,
    text='Payment Frequency',
    bg='#CCCCCC',
    font=f
).grid(row=7, column=0, sticky=W, pady=10)

# Payment Options Label
Label(
    top_frame,
    text='Payment Options',
    bg='#CCCCCC',
    font=f
).grid(row=8, column=0, sticky=W, pady=10)


# <====================================================CALCULATING COSTS=====================================================>
# Defining Different types of Costs and Calculations:
# Membership Type Cost Total Calculation:
def Membershiptotal():
    MembershipCostTotal.set(
        int(Membership_Details_Regular_var.get() or (
                Membership_Details_Basic_var.get() or (Membership_Details_Premium_var.get()))))


# Extra Charges Total Calculation:
def XtraCharges():
    ExtraCharges.set(
        int(twenty_four_seven_var.get()) + int(Diet_Consultation_var.get()) + int(Personal_trainer_var.get()) + int(
            Online_Access_Videos_var.get()))


# Discount Total Calculation:
def DiscountTotal():
    discount1 = twelvemonths_var.get() or twentyfourmonths_var.get()
    discount2 = Membership_Details_Basic_var.get() or Membership_Details_Regular_var.get() or Membership_Details_Premium_var.get() / 100
    TotalDiscount.set(int(discount1) + 1 * discount2)


# Net Total Calculation:
def net_total():
    membershipcost = Membership_Details_Basic_var.get() or Membership_Details_Regular_var.get() or Membership_Details_Premium_var.get()
    extracharges = int(twenty_four_seven_var.get()) + int(Diet_Consultation_var.get()) + int(
        Personal_trainer_var.get()) + int(
        Online_Access_Videos_var.get())
    discount1 = twelvemonths_var.get() or twentyfourmonths_var.get()
    discount2 = Membership_Details_Basic_var.get() or Membership_Details_Regular_var.get() or Membership_Details_Premium_var.get() / 100
    totaldiscount = int(discount1) + 1 * int(discount2)
    NetTotal.set(
        int(membershipcost) + int(extracharges) - int(totaldiscount))


# Payment Total Calculation:
def PaymentAmountTotal():
    membershipcost = Membership_Details_Basic_var.get() or Membership_Details_Regular_var.get() or Membership_Details_Premium_var.get()
    extracharges = int(twenty_four_seven_var.get()) + int(Diet_Consultation_var.get()) + int(
        Personal_trainer_var.get()) + int(
        Online_Access_Videos_var.get())
    discount1 = twelvemonths_var.get() or twentyfourmonths_var.get()
    discount2 = Membership_Details_Basic_var.get() or Membership_Details_Regular_var.get() or Membership_Details_Premium_var.get() / 100
    totaldiscount = int(discount1) + 1 * int(discount2)
    nettotal = membershipcost + extracharges - totaldiscount
    PaymentAmount.set(nettotal * Monthly_option_var.get())


# <===================================================GATHERING ALL FUNCTIONS CONTAINING DIFFERENT CALCULATIONS========================================================>
# Defining function to gather all the calculated cost functions from above:
def CalculateCost():
    Membershiptotal()
    XtraCharges()
    DiscountTotal()
    net_total()
    PaymentAmountTotal()


# <==============================================================BOTTOM FRAME============================================================>
# Total Frame(Bottom Frame)

# Total Label
Label(
    bottom_frame,
    text='TOTAL',
    bg='#CCCCCC',
    font=f
).place(x=230, y=10)

# Membership Cost Total Label
Label(
    bottom_frame,
    text='Membership Cost Total',
    bg='#CCCCCC',
    font=f
).grid(row=10, column=0, sticky=W, pady=10)

# Membership Label
Label(
    bottom_frame,
    text='Membership',
    bg='#CCCCCC',
    font=f,
).grid(row=11, column=0, sticky=W, pady=10)

# Membership Cost Total '0' Label
MembershipCostTotal = IntVar()
Label(
    bottom_frame,
    textvariable=MembershipCostTotal,
    bg='#CCCCCC',
    font=f,
).grid(row=12, column=0, sticky=W, pady=10)

# Extra Charges Label
Label(
    bottom_frame,
    text='Extra Charges*',
    bg='#CCCCCC',
    font=f,
).grid(row=10, column=1, sticky=W, pady=10)

# Extras Label
Label(
    bottom_frame,
    text='Extras',
    bg='#CCCCCC',
    font=f,
).grid(row=11, column=1, sticky=W, pady=10)

# Extra Charges '0' Label
ExtraCharges = IntVar()
Label(
    bottom_frame,
    textvariable=ExtraCharges,
    bg='#CCCCCC',
    font=f,
).grid(row=12, column=1, sticky=W, pady=10)

# Total Discount Label
Label(
    bottom_frame,
    text='Total Discount',
    bg='#CCCCCC',
    font=f,
).grid(row=10, column=2, sticky=W, pady=10)

# Frequency Label
Label(
    bottom_frame,
    text='Frequency',
    bg='#CCCCCC',
    font=f,
).grid(row=11, column=2, sticky=W, pady=10)

# Total Discount '0' Label
TotalDiscount = IntVar()
Label(
    bottom_frame,
    textvariable=TotalDiscount,
    bg='#CCCCCC',
    font=f,
).grid(row=12, column=2, sticky=W, pady=10)

# Payment Amount Label
Label(
    bottom_frame,
    text='Payment Amount',
    bg='#CCCCCC',
    font=f,
).grid(row=10, column=3, sticky=W, pady=10)

# Payment Amount '0' Label
PaymentAmount = IntVar()
Label(
    bottom_frame,
    textvariable=PaymentAmount,
    bg='#CCCCCC',
    font=f,
).grid(row=12, column=3, sticky=W, pady=10)

# Net Total Label
Label(
    bottom_frame,
    text='Net Total',
    bg='#CCCCCC',
    font=f,
).grid(row=10, column=4, sticky=W, pady=10)

# Net Total '0'
NetTotal = IntVar()
Label(
    bottom_frame,
    textvariable=NetTotal,
    bg='#CCCCCC',
    font=f,
).grid(row=12, column=4, sticky=W, pady=10)

# Discount benefit Labels

# First Beneficial 12months
Label(
    top_frame,
    text='* Sign up for a 12-month contract to receive a $2 per week discount on any membership type',
    bg='#CCCCCC',
    font=f,
).place(x=10, y=570)

# Space inbetween the beneficial information
Label(
    top_frame,
    bg='#CCCCCC',
    text='',

).grid(row=9, column=0, pady=4)

# Second Beneficial 24months
Label(
    top_frame,
    text='**Sign up for 24 month to receive a $5 per week discount on any membership type',
    bg='#CCCCCC',
    font=f,
).place(x=10, y=600)

# Space inbetween the beneficial information
Label(
    top_frame,
    text='***For Direct Debit, there is a 1% discount on the base membership cost',
    bg='#CCCCCC',
    font=f,
).place(x=10, y=630)

# Duration star
Label(
    top_frame,
    text='*',
    bg='#CCCCCC',
    font=(f, 20)
).place(x=60, y=280)

# <------------------------------------------------------------------------------------------------>
# MEMBERSHIP DETAILS FRAME:
membership_type_frame = LabelFrame(
    top_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)
# <-----------------------------------ENTRY BOXES------------------------------------------------>
register_firstname = Entry(
    top_frame,
    font=f
)

register_lastname = Entry(
    top_frame,
    font=f
)
register_address = Entry(
    top_frame,
    font=f
)


# Making Phone Number only numeric
def PhoneNumberValidation(u_input):
    return u_input.isdigit()


my_valid = ws.register(PhoneNumberValidation)
register_phonenumber = Entry(
    top_frame,
    validate='key',
    validatecommand=(my_valid, '%S'),
    font=f
)
# <------------------------------------------------------------------------------------------------>
# MEMBERSHIP DETAILS
# Basic Radio Button:
Basic_rb = Radiobutton(
    membership_type_frame,
    text='Basic',
    bg='#CCCCCC',
    variable=Membership_Details_var,
    value=10,
    font=('Times', 14),

)

# Regular RadioButton:
Regular_rb = Radiobutton(
    membership_type_frame,
    text='Regular',
    bg='#CCCCCC',
    variable=Membership_Details_var,
    value=15,
    font=('Times', 14),

)

# Premium RadiButton:
Premium_rb = Radiobutton(
    membership_type_frame,
    text='Premium',
    bg='#CCCCCC',
    variable=Membership_Details_var,
    value=20,
    font=('Times', 14)
)
# <------------------------------------------------------------------------------------------------>
# DURATION FRAME
# Duration Section:
duration_type_frame = LabelFrame(
    top_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

# 3 months RadioButton:
ThreeMonths_rb = Radiobutton(
    duration_type_frame,
    text='3 months',
    bg='#CCCCCC',
    variable=Membership_Duration_var,
    value=1,
    font=('Times', 14),

)

# 12 months RadioButton:
TwelveMonths_rb = Radiobutton(
    duration_type_frame,
    text='12 months',
    bg='#CCCCCC',
    variable=Membership_Duration_var,
    value=2,
    font=('Times', 14)
)

# 24 months RadioButton:
TwentyFourMonths_rb = Radiobutton(
    duration_type_frame,
    text='24 months',
    bg='#CCCCCC',
    variable=Membership_Duration_var,
    value=5,
    font=('Times', 14)
)
# <------------------------------------------------------------------------------------------------>
# EXTRAS FRAME
extras_types_frame = LabelFrame(
    top_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

# 24/7 Access Checkbox:
twenty_four_seven_access_chk = Checkbutton(
    extras_types_frame,
    text='24/7 Access',
    bg='#CCCCCC',
    variable=twenty_four_seven_var,
    font=('Times', 14),
    onvalue=1,
    offvalue=None
)

# Personal Trainer Checkbox:
Personal_trainer_chk = Checkbutton(
    extras_types_frame,
    text='Personal Trainer',
    bg='#CCCCCC',
    variable=Personal_trainer_var,
    font=('Times', 14),
    onvalue=20,
    offvalue=None
)

# Diet Consultation Checkbox:
Diet_Consultation_chk = Checkbutton(
    extras_types_frame,
    text='Diet Consultation',
    bg='#CCCCCC',
    variable=Diet_Consultation_var,
    font=('Times', 14),
    onvalue=20,
    offvalue=None
)

# Online Access Videos Checkbox:
Online_Access_Videos_chk = Checkbutton(
    extras_types_frame,
    text='Online Access Videos',
    bg='#CCCCCC',
    variable=Online_Access_Videos_var,
    font=('Times', 14),
    onvalue=2,
    offvalue=None
)
# <------------------------------------------------------------------------------------------------>

# PAYMENT FREQUENCY
payment_frequency_frame = LabelFrame(
    top_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

# Weekly RadioButton:
Weekly_rb = Radiobutton(
    payment_frequency_frame,
    text='Weekly',
    bg='#CCCCCC',
    variable=Membership_Payment_Frequency_var,
    value=1,
    font=('Times', 14)
)

# Monthly RadioButton:
Monthly_rb = Radiobutton(
    payment_frequency_frame,
    text='Monthly',
    bg='#CCCCCC',
    variable=Membership_Payment_Frequency_var,
    value=4,
    font=('Times', 14)
)
# <------------------------------------------------------------------------------------------------>
# PAYMENT OPTIONS
payment_options_frame = LabelFrame(
    top_frame,
    bg='#CCCCCC',
    padx=10,
    pady=10,
)

# DirectDebit RadioButton:
Direct_Debit = Radiobutton(
    payment_options_frame,
    text='Direct Debit',
    bg='#CCCCCC',
    variable=Membership_Payment_Options_var,
    value=0.01,
    font=('Times', 14)
)

# Other RadioButton:
Other_btn = Radiobutton(
    payment_options_frame,
    text='Other',
    bg='#CCCCCC',
    variable=Membership_Payment_Options_var,
    value=1,
    font=('Times', 14)
)

# <------------------------------------------------------------------------------------------------>


# Entries, radioboxes and checkboxes
register_firstname.grid(row=0, column=1, pady=10, padx=20)
register_lastname.grid(row=1, column=1, pady=10, padx=20)
register_phonenumber.grid(row=3, column=1, pady=10, padx=20)
register_address.grid(row=2, column=1, pady=10, padx=20)
top_frame.pack(pady=50)
bottom_frame.place(x=159, y=860)

# Frames
membership_type_frame.grid(row=4, column=1, pady=10, padx=20)
duration_type_frame.grid(row=5, column=1, pady=10, padx=20)
extras_types_frame.grid(row=6, column=1, pady=10, padx=20)
payment_frequency_frame.grid(row=7, column=1, pady=10, padx=20)
payment_options_frame.grid(row=8, column=1, pady=10, padx=20)

# Radio Buttons Appear!:
Basic_rb.pack(expand=True, side=LEFT)
Regular_rb.pack(expand=True, side=LEFT)
Premium_rb.pack(expand=True, side=LEFT)
ThreeMonths_rb.pack(expand=True, side=LEFT)
TwelveMonths_rb.pack(expand=True, side=LEFT)
TwentyFourMonths_rb.pack(expand=True, side=LEFT)
Weekly_rb.pack(expand=True, side=LEFT)
Monthly_rb.pack(expand=True, side=LEFT)
Direct_Debit.pack(expand=True, side=LEFT)
Other_btn.pack(expand=True, side=LEFT)

# Checkboxes Appear!
twenty_four_seven_access_chk.pack(expand=True, side=LEFT)
Personal_trainer_chk.pack(expand=True, side=LEFT)
Diet_Consultation_chk.pack(expand=True, side=LEFT)
Online_Access_Videos_chk.pack(expand=True, side=LEFT)


# Clear Buttons:
# Form Clear Button:
# Defining form clear function:
def form_clear():
    register_firstname.delete(0, 'end')
    register_lastname.delete(0, 'end')
    register_address.delete(0, 'end')
    register_phonenumber.delete(0, 'end')
    Entry()
    Basic_rb.deselect()
    Regular_rb.deselect()
    Premium_rb.deselect()
    ThreeMonths_rb.deselect()
    TwelveMonths_rb.deselect()
    TwentyFourMonths_rb.deselect()
    Direct_Debit.deselect()
    Other_btn.deselect()
    twenty_four_seven_access_chk.deselect()
    Diet_Consultation_chk.deselect()
    Personal_trainer_chk.deselect()
    Online_Access_Videos_chk.deselect()
    Weekly_rb.deselect()
    Monthly_rb.deselect()


# Defining each Entry and Input field Clear Functions
def firstnameclear():
    register_firstname.delete(0, 'end')


def lastnameclear():
    register_lastname.delete(0, 'end')


def addressclear():
    register_address.delete(0, 'end')


def phonenumberclear():
    register_phonenumber.delete(0, 'end')


def Membership_Details_Clear():
    Basic_rb.deselect(), Regular_rb.deselect(), Premium_rb.deselect()


def Duration_Clear():
    ThreeMonths_rb.deselect(), TwelveMonths_rb.deselect(), TwentyFourMonths_rb.deselect()


def EXTRAS_Clear():
    twenty_four_seven_access_chk.deselect(), Diet_Consultation_chk.deselect(), Personal_trainer_chk.deselect(), Online_Access_Videos_chk.deselect()


def Payment_Options_Clear():
    Direct_Debit.deselect(), Other_btn.deselect()


def Payment_Frequency_Clear():
    Weekly_rb.deselect(), Monthly_rb.deselect()


# Defining Clear Buttons for each Entry and Input fields
FirstNameClearButton = Button(top_frame, text='Clear', command=firstnameclear, width=2,   highlightbackground='#CCCCCC')
FirstNameClearButton.place(x=570, y=10)

LastNameClearButton = Button(top_frame, text='Clear', command=lastnameclear, width=2, highlightbackground='#CCCCCC')
LastNameClearButton.place(x=570, y=60)

AddressClearButton = Button(top_frame, text='Clear', command=addressclear, width=2, highlightbackground='#CCCCCC')
AddressClearButton.place(x=570, y=110)

PhoneNumberClearButton = Button(top_frame, text='Clear', command=phonenumberclear, width=2, highlightbackground='#CCCCCC')
PhoneNumberClearButton.place(x=570, y=160)

MembershipDetailsClearButton = Button(top_frame, text='Clear', command=Membership_Details_Clear, width=2, highlightbackground='#CCCCCC')
MembershipDetailsClearButton.place(x=570, y=220)

DurationClearButton = Button(top_frame, text='Clear', command=Duration_Clear, width=2, highlightbackground='#CCCCCC')
DurationClearButton.place(x=590, y=285)

ExtrasClearButton = Button(top_frame, text='Clear', command=EXTRAS_Clear, width=2, highlightbackground='#CCCCCC')
ExtrasClearButton.place(x=710, y=355)

PaymentFrequencyClearButton = Button(top_frame, text='Clear', command=Payment_Frequency_Clear, width=2, highlightbackground='#CCCCCC')
PaymentFrequencyClearButton.place(x=530, y=420)

PaymentOptionsClearButton = Button(top_frame, text='Clear', command=Payment_Options_Clear, width=2, highlightbackground='#CCCCCC')
PaymentOptionsClearButton.place(x=540, y=485)


# <------------------------------------------------------------------------------------------------>
# View Button Function and Display:
def view():
    lx = ["First Name: " + register_firstname.get(), "\n", "Last Name: " + register_lastname.get(), "\n",
          "Address: " + register_address.get(), "\n", "Phone Number: " + register_phonenumber.get(), "\n",
          "Membership Cost: ",
          "\n", "$" + str(Membership_Details_var.get()),
          "\n",
          "Duration cost: " "$" + Membership_Duration_var.get(),
          "\n",
          "Extras cost: " + ("$" + str(twenty_four_seven_var.get())), ',' + ("$" + str(Personal_trainer_var.get())),
          ',' +
          ("$" + str(Diet_Consultation_var.get())), ',' +
          ("$" + str(Online_Access_Videos_var.get())),
          '\n',
          "\n", "Payment Options: " + Membership_Payment_Options_var.get(), "\n",
          "Payment Frequency: " + str(Membership_Payment_Frequency_var.get()), "\n", ]

    messagebox.showinfo("Your Details", lx)


# <------------------------------------------------------------------------------------------------>

# Input Field Validations:
def validate_input():
    if not register_firstname.get() or not register_lastname.get() or not register_address.get() or not register_phonenumber.get() or not Membership_Details_var.get() or not Membership_Duration_var.get() or not twenty_four_seven_var.get() and not Diet_Consultation_var.get() and not Personal_trainer_var.get() and not Online_Access_Videos_var.get() or not Membership_Payment_Options_var.get() or not Membership_Payment_Frequency_var.get():
        messagebox.showerror("Missing", "Please Fill in the form!")
    else:
        None


# <------------------------------------------------------------------------------------------------>
# Register Button Function:
def Submit():
    global firstname, lastname
    PhoneNumberValidation(u_input=register_phonenumber.get())
    validate_input()
    CalculateCost()
    XtraCharges()
    DiscountTotal()
    PaymentAmountTotal()
    net_total()

    # get form data
    firstname = register_firstname.get()
    lastname = register_lastname.get()
    address = register_address.get()
    phonennumber = register_phonenumber.get()
    PaymentFrequency = Membership_Payment_Frequency_var.get()
    PaymentOptions = Membership_Payment_Options_var.get()
    membershipcostotal = MembershipCostTotal.get()
    extracharges = ExtraCharges.get()
    nettotal = NetTotal.get()
    discounttotal = TotalDiscount.get()
    paymentamounttotal = PaymentAmount.get()

    file = open('membersdatasaved.txt', 'a')
    file.write(str('First Name: ' + firstname) + '\n'), \
        file.write(str('Last Name: ' + lastname) + '\n'), \
        file.write(str('Address: ' + address) + '\n'), \
        file.write(str('Phone Number: ' + phonennumber) + '\n'), \
        file.write(str('Base Membership Cost Total: $' + str(membershipcostotal)) + '\n'), \
        file.write(str('Extra Cost: $' + str(extracharges)) + '\n'), \
        file.write(str('Total Discount: $ ' + str(discounttotal)) + '\n'), \
        file.write(str('Net membership Cost: $' + str(nettotal)) + '\n'), \
        file.write(str('Regular Payment Amount: $' + str(paymentamounttotal)) + '\n'), \
        file.write(str('Frequency of Payment: ' + PaymentOptions) + '\n'), \
        file.write(str('Method of Payment: ' + str(PaymentFrequency)) + '\n'),

# <------------------------------------------------------------------------------------------------>
    # Database creation
    # Add fitness class selection to the database
    # By doing that, recreate the table(dlete the table. Follow Code with Hala For more)
    # ---- creating table -----
    conn = sqlite3.connect('gym.db')
    cursor = conn.cursor()
    table_create_query = '''CREATE TABLE IF NOT EXISTS User_Registration (MemberID INTEGER PRIMARY KEY,firstname TEXT, lastname TEXT, address TEXT, phonenumber INT, basemembershipcost INT, extracost INT, totaldiscount INT, netmembershipcost INT, regularpaymentamount INT, frequencyofpayment INT, methodofpayment INT)'''
# Show the table
    conn.execute(table_create_query)

# # Insert Data
    
    data_insert_query = '''INSERT INTO User_Registration (firstname, lastname, address, phonenumber, basemembershipcost, extracost, totaldiscount, netmembershipcost, regularpaymentamount, frequencyofpayment, methodofpayment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    data_insert_tuple = (firstname, lastname, address, phonennumber, membershipcostotal, extracharges, discounttotal, nettotal,
        paymentamounttotal, PaymentFrequency, PaymentOptions,)
    
    # Check if user already exists into the Database
    cursor.execute("SELECT * FROM User_Registration WHERE firstname = ? AND lastname = ?", (firstname, lastname))
    existing_user = cursor.fetchone()

    if existing_user:
            messagebox.showerror("Registration Error", "User already exists.")
    else:
    # Insert the user's information into the database
        cursor.execute("INSERT INTO User_Registration (firstname, lastname, address, phonenumber, basemembershipcost, extracost, totaldiscount, netmembershipcost, regularpaymentamount, frequencyofpayment, methodofpayment) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (firstname, lastname, address, phonennumber, membershipcostotal, extracharges, discounttotal, nettotal,
        paymentamounttotal, PaymentFrequency, PaymentOptions,))
        conn.commit()
        messagebox.showinfo("Registration Successful", "User registered successfully.")

    cursor.execute(data_insert_query, data_insert_tuple)
    conn.close()


# <------------------------------------------------------------------------------------------------>
# Bottom Buttons:

# Form Clear button
FormClearButton = Button(ws, text='Clear', command=form_clear, highlightbackground='#0B5A81')
FormClearButton.place(x=150, y=1050)

# View Button
ViewButton = Button(ws, text='View', command=view, highlightbackground='#0B5A81')
ViewButton.place(x=340, y=1050)

# Calculate Button
CalculateButton = Button(ws, text='Calculate', command=CalculateCost, highlightbackground='#0B5A81')
CalculateButton.place(x=490, y=1050)

# Exit Button
ExitButton = Button(ws, text='Exit', command=exit, highlightbackground='#0B5A81')
ExitButton.place(x=800, y=1050)

# Register Button
RegisterButton = Button(ws, text='Register', command=Submit, highlightbackground='#0B5A81')
RegisterButton.place(x=650, y=1050)

# <=======================TOP NAVIGATION NAVIGATIONS======================>

# Home Button
HomeButton = Button(ws, text='Home',font=('Calibri', 14, 'bold'), fg="black", bg="#ed5e68", command=Home, width=15, height=1)
HomeButton.place(x=10, y=0.5)

# Help Button
HelpButton = Button(ws, text='Help',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=HELP, width=15, height=1)
HelpButton.place(x=250, y=0.5)

# Search Button
SearchButton = Button(ws, text='Search',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Search, width=15, height=1)
SearchButton.place(x=490, y=0.5)

# Fitness Button
FitnessCLassButton = Button(ws, text='Fitness',font=('Calibri', 15, 'bold'), fg="black", bg="#ed5e68", command=Fitness, width=15, height=1)
FitnessCLassButton.place(x=730, y=0.5)

# Loop to keep the form running
ws.mainloop()