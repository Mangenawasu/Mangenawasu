import tkinter as tk
from tkinter import *
import os
import string
import datetime


#main window ####
window = tk.Tk()     #
###############

#*****************†******†‡

gProv = ""
gID = ""
gAge = ""
logged = False
Supwin = None
date = datetime.date.today()
date = str(date) + "\n"
Vrollwin = None

########REG BUTTONS CMD#######

#Open Voter entry creation
def Voters():
        mid_frame.place(relwidth=0.8, relheight=0.65, relx=0.1, rely=0.3)
        lower_frame.place(relwidth=1, relheight =0.12, rely=0.88)
        return None


#Add entries to respective files
#Clear entry fields
def Register():
	global gName
	global gID
	global gProv
	global gAge
	global name #global vars and txt files
	finNames = open("names.txt", 'a')
	finAges = open("ages.txt", 'a')
	finId = open("idNums.txt", 'a')
	finProvinces = open("provinces.txt", 'a')
	finDates = open("dates.txt", 'a')
	
	#update & close files, clear fields
	
   
	age = gAge.get()
	if int(age) < 18:
		Message(mid_frame, text="Voter under 18. Person needs to be at least 18 to register", fg="red", relief=FLAT).pack()
	else:
		finAges.write(age+"\n")
		name = gName.get() + '\n'
		finNames.write(name)
		idnum = gID.get() + '\n'
		finId.write(idnum)
		prov = gProv.get() + '\n'
		finProvinces.write(prov)
		finDates.write(date)
	gAge.delete(0, END)
	gName.delete(0, END)
	gID.delete(0, END)
	gProv.delete(0, END)
	
	finDates.close()
	finProvinces.close()
	finId.close()
	finAges.close()
	finNames.close()
	
	return None
	
	
def  dateVroll():
	global Vrollwin
	Vrollwin = Toplevel(window)
	vframe = Frame(Vrollwin).place(relwidth=1, relheight=1, relx=1, rely=1)
	finNames = open("names.txt", 'r')
	finAges = open("ages.txt", 'r')
	finId = open("idNums.txt", 'r')
	finProvinces = open("provinces.txt", 'r')
	finDates = open("dates.txt", 'r')
	
	tnames = finNames.readlines()
	tages = finAges.readlines()
	tid = finId.readlines()
	tprov = finProvinces.readlines()
	tdates = finDates.readlines()
	
	finNames.close()
	finAges.close()
	finId.close()
	finProvinces.close()
	finDates.close()
	
	Label(Vrollwin, text="NAME", relief=SUNKEN).grid(row=1, column=1)
	LBname = Listbox(Vrollwin)
	for i in range(len(tnames)):
		LBname.insert(i, tnames[i].strip())
	LBname.grid(row=2, column=1)
	
	Label(Vrollwin, text="AGE", relief=SUNKEN).grid(row=1, column=2)
	LBage = Listbox(Vrollwin)
	for i in range(len(tages)):
		LBage.insert(i, tages[i].strip())
	LBage.grid(row=2, column=2)
	
	Label(Vrollwin, text="ID Num", relief=SUNKEN).grid(row=1, column=3)
	LBid = Listbox(Vrollwin)
	for i in range(len(tid)):
		LBid.insert(i, tid[i].strip())
	LBid.grid(row=2, column=3)
	
	Label(Vrollwin, text="PROVINCE", relief=SUNKEN).grid(row=1, column=4)
	LBprov = Listbox(Vrollwin)
	for i in range(len(tprov)):
		LBprov.insert(i, tprov[i].strip())
	LBprov.grid(row=2, column=4)
	
	Label(Vrollwin, text="REG DATE", relief=SUNKEN).grid(row=1, column=5)
	LBdate = Listbox(Vrollwin)
	for i in range(len(tdates)):
		LBdate.insert(i, tdates[i].strip())
	LBdate.grid(row=2, column=5)
	
	
def  nameVroll():
	global Vrollwin
	Vrollwin = Toplevel(window)
	
	finNames = open("names.txt", 'r')
	finAges = open("ages.txt", 'r')
	finId = open("idNums.txt", 'r')
	finProvinces = open("provinces.txt", 'r')
	finDates = open("dates.txt", 'r')
	
	tnames = finNames.readlines()
	tages = finAges.readlines()
	tid = finId.readlines()
	tprov = finProvinces.readlines()
	tdates = finDates.readlines()
	
	finNames.close()
	finAges.close()
	finId.close()
	finProvinces.close()
	finDates.close()
	
	Label(Vrollwin, text="NAME", relief=SUNKEN).grid(row=1, column=1)
	Label(Vrollwin, text="AGE", relief=SUNKEN).grid(row=1, column=2)
	Label(Vrollwin, text="ID Num", relief=SUNKEN).grid(row=1, column=3)
	Label(Vrollwin, text="PROVINCE", relief=SUNKEN).grid(row=1, column=4)
	Label(Vrollwin, text="REG DATE", relief=SUNKEN).grid(row=1, column=5)
	
	LBname = Listbox(Vrollwin)
	LBage = Listbox(Vrollwin)
	LBid = Listbox(Vrollwin)
	LBprov = Listbox(Vrollwin)
	LBdate = Listbox(Vrollwin)
	
	t= []
	for name in tnames:
		t.append([0, 1, 2, 3, 4])
			
	for i in range(len(t)):
		(t[i])[0] = tnames[i].strip()
		(t[i])[1] = tages[i].strip()
		(t[i])[2] = tid[i].strip()
		(t[i])[3] = tprov[i].strip()
		(t[i])[4] = tdates[i].strip()
	t.sort()
	
	for i in range(len(t)):
		item = t[i]
		LBname.insert(i, item[0].strip())
		LBage.insert(i, item[1].strip())
		LBid.insert(i, item[2].strip())
		LBprov.insert(i, item[3].strip())
		LBdate.insert(i, item[4].strip())
	
	LBname.grid(row=2, column=1)
	LBage.grid(row=2, column=2)
	LBid.grid(row=2, column=3)
	LBprov.grid(row=2, column=4)
	LBdate.grid(row=2, column=5)
	
	
def  provVroll():
	global Vrollwin
	Vrollwin = Toplevel(window)
	
	finNames = open("names.txt", 'r')
	finAges = open("ages.txt", 'r')
	finId = open("idNums.txt", 'r')
	finProvinces = open("provinces.txt", 'r')
	finDates = open("dates.txt", 'r')
	
	tnames = finNames.readlines()
	tages = finAges.readlines()
	tid = finId.readlines()
	tprov = finProvinces.readlines()
	tdates = finDates.readlines()
	
	finNames.close()
	finAges.close()
	finId.close()
	finProvinces.close()
	finDates.close()
	
	Label(Vrollwin, text="NAME", relief=SUNKEN).grid(row=1, column=1)
	Label(Vrollwin, text="AGE", relief=SUNKEN).grid(row=1, column=2)
	Label(Vrollwin, text="ID Num", relief=SUNKEN).grid(row=1, column=3)
	Label(Vrollwin, text="PROVINCE", relief=SUNKEN).grid(row=1, column=4)
	Label(Vrollwin, text="REG DATE", relief=SUNKEN).grid(row=1, column=5)
	
	LBname = Listbox(Vrollwin)
	LBage = Listbox(Vrollwin)
	LBid = Listbox(Vrollwin)
	LBprov = Listbox(Vrollwin)
	LBdate = Listbox(Vrollwin)
	
	t= []
	for name in tnames:
		t.append([0, 1, 2, 3, 4])
			
	for i in range(len(t)):
		(t[i])[0] = tprov[i].strip()
		(t[i])[1] = tages[i].strip()
		(t[i])[2] = tid[i].strip()
		(t[i])[3] = tnames[i].strip()
		(t[i])[4] = tdates[i].strip()
	t.sort()
	
	for i in range(len(t)):
		item = t[i]
		LBprov.insert(i, item[0].strip())
		LBage.insert(i, item[1].strip())
		LBid.insert(i, item[2].strip())
		LBname.insert(i, item[3].strip())
		LBdate.insert(i, item[4].strip())
	
	LBname.grid(row=2, column=1)
	LBage.grid(row=2, column=2)
	LBid.grid(row=2, column=3)
	LBprov.grid(row=2, column=4)
	LBdate.grid(row=2, column=5)
	
	
def  ageVroll():
	global Vrollwin
	Vrollwin = Toplevel(window)
	
	finNames = open("names.txt", 'r')
	finAges = open("ages.txt", 'r')
	finId = open("idNums.txt", 'r')
	finProvinces = open("provinces.txt", 'r')
	finDates = open("dates.txt", 'r')
	
	tnames = finNames.readlines()
	tages = finAges.readlines()
	tid = finId.readlines()
	tprov = finProvinces.readlines()
	tdates = finDates.readlines()
	
	finNames.close()
	finAges.close()
	finId.close()
	finProvinces.close()
	finDates.close()
	
	Label(Vrollwin, text="NAME", relief=SUNKEN).grid(row=1, column=1)
	Label(Vrollwin, text="AGE", relief=SUNKEN).grid(row=1, column=2)
	Label(Vrollwin, text="ID Num", relief=SUNKEN).grid(row=1, column=3)
	Label(Vrollwin, text="PROVINCE", relief=SUNKEN).grid(row=1, column=4)
	Label(Vrollwin, text="REG DATE", relief=SUNKEN).grid(row=1, column=5)
	
	LBname = Listbox(Vrollwin)
	LBage = Listbox(Vrollwin)
	LBid = Listbox(Vrollwin)
	LBprov = Listbox(Vrollwin)
	LBdate = Listbox(Vrollwin)
	
	t= []
	for name in tnames:
		t.append([0, 1, 2, 3, 4])
			
	for i in range(len(t)):
		(t[i])[0] = tages[i].strip()
		(t[i])[1] = tnames[i].strip()
		(t[i])[2] = tid[i].strip()
		(t[i])[3] = tprov[i].strip()
		(t[i])[4] = tdates[i].strip()
	t.sort()
	
	for i in range(len(t)):
		item = t[i]
		LBage.insert(i, item[0].strip())
		LBname.insert(i, item[1].strip())
		LBid.insert(i, item[2].strip())
		LBprov.insert(i, item[3].strip())
		LBdate.insert(i, item[4].strip())
	
	LBname.grid(row=2, column=1)
	LBage.grid(row=2, column=2)
	LBid.grid(row=2, column=3)
	LBprov.grid(row=2, column=4)
	LBdate.grid(row=2, column=5)
	
	
	
    
def Back():
	mid_frame.place(relwidth=0, relheight=0)
	lower_frame.place(relwidth=0, relheight =0, rely=0.88)
	return None

##############################


#title
window.title("iVote Voters Registration")

#canvas
canvas = tk.Canvas(window, height=1250, width=1000, bg="#263D42")
canvas.pack()
frame = tk.Frame(window, pady=10)
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.05)

mid_frame = tk.Frame(frame, bg="#EEEEEE", pady=10)
#mid_frame.place(relwidth=0.8, relheight=0.65, relx=0.1, rely=0.3)

lower_frame = Frame(window)
#lower_frame.place(relwidth=1, relheight =0.12, rely=0.88)

############################$###

#MENU

def donothing():
   Accountwin = Toplevel(window )
   button = Button(Accountwin, text="Do nothing button")
   button.pack()
   
username = ""
password = ""
passwd = ""
check = 0
Accountwin = False
Loginwin = None



#MM BUTTONS
Button (window, text="Register New Voter", bg="#263D42", fg="white", command = Voters, state=DISABLED).pack()
viewVoters = Button (window, text="View Registered Voters", bg="#263D42", fg="white", state=DISABLED).pack()
#	Enabled
button_frame = Frame(window)

Button (button_frame, text="Register New Voter", bg="#263D42", fg="white", command = Voters).pack()
viewVoters = Button (button_frame, text="View Registered Voters", bg="#263D42", fg="white", command=dateVroll).pack()




def signup():
   try:
   	Loginwin.withdraw()
   except:
   	nothing = 0
   global username
   global password
   global passwd
   global Accountwin
   Accountwin = Toplevel(window )
   #Display entry fields
   Label(Accountwin, text="Username: ").grid(row=1, column=1)
   username = Entry(Accountwin, width = 20)
   username.grid(row=1, column=2)
   
   Label(Accountwin, text="Password: ").grid(row=2, column=1)
   password = Entry(Accountwin, show="*")
   password.grid(row=2, column=2)
   
   Label(Accountwin, text="Re-enter Password: ").grid(row=3, column=1)
   passwd = Entry(Accountwin, show="*")
   passwd.grid(row=3, column=2)
   
   Label(Accountwin).grid(row=4, column=1)
   
   checkVar = IntVar()
   Checkbutton(Accountwin, text = "Voter Reg Officer", variable = checkVar, onvalue = 1, offvalue = 0, height=5, command=chkbtn).grid(row=5, column=1)
   button = Button(Accountwin, text="Signup", command=Signup)
   button.grid(row=5, column=2)
   return None
   
def chkbtn():
	global check
	if check == 0:
		check = 1
	else:
		check = 0
	return None
	
	
def Signup():
    global Accountwin
    global username
    global password
    global passwd
    global check
    global Supwin
    Supwin = Toplevel(Accountwin)
    finAcc = open("account info.txt", "a")
    name = username.get() + "\n"
    psword = password.get() + "\n"
    pswd = passwd.get() + "\n"
    
    if check == 1:
    	if psword == pswd:
    		username.delete(0, END)
    		password.delete(0, END)
    		passwd.delete(0, END)
    		finAcc.write(name)
    		finAcc.write(psword)
    		Accountwin.withdraw()
    		Label(Supwin, text="Account created!").pack()
    		Button(Supwin, text="Login", command=login).pack()
    	else:
    		Label(Supwin, text="Passwords do not match").pack()
    		Button(Supwin, text="Retry").pack()
    else:
    		Label(Supwin, text="You must be a ZEC Voter Registration Officer to signup.").pack()
    		Button(Supwin, text="Back").pack()
    		
    finAcc.close()
    return
    
    
Password = ""
Username = ""
    
def login():
   global Username
   global Password
   global Loginwin
   global Supwin
   try:
   	Supwin.withdraw()
   except:
   	nothing = 0
   Loginwin = Toplevel(window )
   #Display entry fields
   Label(Loginwin, text="Username: ").grid(row=1, column=1)
   Username = Entry(Loginwin, width = 20)
   Username.grid(row=1, column=2)
   
   Label(Loginwin, text="Password: ").grid(row=2, column=1)
   Password = Entry(Loginwin, show="*")
   Password.grid(row=2, column=2)

   button = Button(Loginwin, text="Login", command=Login)
   button.grid(row=4, column=2)
   return None
    
    
def Login():
    global Username
    global Password
    global Loginwin
    global logged
    finAcc = open("account info.txt", "r")
    det = finAcc.readlines() #list with saved usernames and passwords
    finAcc.close()
    Name = Username.get() +"\n"
    Username.delete(0, END)
    Pswd = Password.get()
    Password.delete(0, END)
    x = True #control var
    #search name in list
    for i in range(len(det)):
    	if det[i] == Name:
    		pswd = det[i+1]
    		pswd = pswd.strip()
    		x = False
    
    if x:
    	Label(Loginwin, text="User not found").grid(row=6, column=1)
    	Button(Loginwin, text="Signup?", relief=FLAT, fg="blue", command=signup).grid(row=6, column=2)
    	
    else:
    	if pswd == Pswd:
    		Label(Loginwin, text="Welcome "+Name).grid(row=7, column=1)
    		button_frame.place(relwidth=1, relheight =0.12, rely=0.88)
    		logged = True
    	
    	else:
    		Label(Loginwin, text="Incorrect password").grid(row=7, column=1)
    
    
#text
var = StringVar()
label = Message( frame, bd=10, textvariable=var, relief=SUNKEN, width=400, justify=CENTER, font="Arial 10" )
var.set("Welcome to iVote Voters Registration System!")
label.pack()
    
    
#POLLING STATIONS
pollframe = Frame(frame)
var = IntVar()

def Byo():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Byo City Council HO")
	LB.insert(2, "Emtonjeni Pry Sch")
	LB.insert(3, "Gifford High Sch")
	LB.insert(4, "Olwesibili High Sch")
	LB.insert(5, "Another P. Station")
	LB.insert(6, "Liyatshisa S/C")
	LB.insert(7, "Yet another one")
	LB.insert(8, "And another...")
	LB.insert(9, "Almost there...")
	LB.insert(10, "Ten, that's good")
	LB.place(relx=0.35, rely=0.01)
	
def Hre():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "CoH Head Office")
	LB.insert(2, "Marlbrough S/C")
	LB.insert(3, "Chitungwiza Mun. HO")
	LB.insert(4, "Epworth Pry.")
	LB.insert(5, "Zengeza High Sch")
	LB.insert(6, "Makoni Reg Offices")
	LB.insert(7, "Mereki S/C")
	LB.insert(8, "Glenview S/C")
	LB.insert(9, "Glenorah B High Sch")
	LB.insert(10, "Chinembiri Pry.")
	LB.place(relx=0.35, rely=0.01)
	
def Mnc():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Mutare Mun. HO")
	LB.insert(2, "Sakubva Pry")
	LB.insert(3, "Chipinge T/C HO")
	LB.insert(4, "Vumba RDC")
	LB.insert(5, "Dangamvura High")
	LB.insert(6, "A cool Manica place")
	LB.insert(7, "Gaza High Sch")
	LB.insert(8, "Another polling st")
	LB.insert(9, "We just need ten")
	LB.insert(10, "There")
	LB.place(relx=0.35, rely=0.01)
	
def MsC():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Mash Cent Area")
	LB.insert(2, "Municipal Head Office")
	LB.insert(3, "Chidodo Pry.")
	LB.insert(4, "The RDC")
	LB.insert(5, "Chiedza High")
	LB.insert(6, "A cool Mash place")
	LB.insert(7, "Gudza High Sch")
	LB.insert(8, "Another polling st")
	LB.insert(9, "We just need ten")
	LB.insert(10, "There")
	LB.place(relx=0.35, rely=0.01)
	
def MsW():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Mash East Area")
	LB.insert(2, "Marondera TC")
	LB.insert(3, "Jonasi Pry.")
	LB.insert(4, "The RDC")
	LB.insert(5, "Chiedza High")
	LB.insert(6, "A cool Mash place")
	LB.insert(7, "Some High Sch")
	LB.insert(8, "Marikopo Sec Sch.")
	LB.insert(9, "Chinamanenji S/C")
	LB.insert(10, "Pamwezve")
	LB.place(relx=0.35, rely=0.01)
	
def MsE():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Mash East Area")
	LB.insert(2, "Municipal Head Office")
	LB.insert(3, "Chido Pry.")
	LB.insert(4, "The RDC")
	LB.insert(5, "Chiedza High")
	LB.insert(6, "A cool Mash place")
	LB.insert(7, "Some High Sch")
	LB.insert(8, "Another polling st")
	LB.insert(9, "Almost there...")
	LB.insert(10, "The last one")
	LB.place(relx=0.35, rely=0.01)
	
def MtN():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Empandleni High Sch.")
	LB.insert(2, "Municipal Head Office")
	LB.insert(3, "Isitshwala Sec.")
	LB.insert(4, "The RDC")
	LB.insert(5, "Chiedza High")
	LB.insert(6, "A cool Mash place")
	LB.insert(7, "Siziba S/C")
	LB.insert(8, "Another one")
	LB.insert(9, "Almost there...")
	LB.insert(10, "Lolu Registrar's Ofc")
	LB.place(relx=0.35, rely=0.01)
	
def MtS():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Godlwayo High Sch.")
	LB.insert(2, "Municipal Head Office")
	LB.insert(3, "Isitshwala Sec.")
	LB.insert(4, "Rural RDC")
	LB.insert(5, "Chiedza High")
	LB.insert(6, "Some Matebele place")
	LB.insert(7, "Filabusi S/C")
	LB.insert(8, "Another one")
	LB.insert(9, "Selous town centre")
	LB.insert(10, "Lolu Registrar's Ofc")
	LB.place(relx=0.35, rely=0.01)
	
def Mid():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Somabhula High Sch.")
	LB.insert(2, "Gweru City Counc HO")
	LB.insert(3, "Kwekwe High")
	LB.insert(4, "Mbizo 5 s/c")
	LB.insert(5, "Manunure High")
	LB.insert(6, "Nehosho Pry.")
	LB.insert(7, "Kdm centre")
	LB.insert(8, "Senga s/c")
	LB.insert(9, "Sunview Pvt Cllg")
	LB.insert(10, "Gokwe Registrar's Ofc")
	LB.place(relx=0.35, rely=0.01)
	
def Mas():
	global pollframe
	LB = Listbox(pollframe, bd=10)
	LB.insert(1, "Gwenhamo High Sch.")
	LB.insert(2, "Masvingo Head Office")
	LB.insert(3, "Nehoreka Sec.")
	LB.insert(4, "Rural RDC")
	LB.insert(5, "Chiredzi Twn Council")
	LB.insert(6, "G. Zim")
	LB.insert(7, "Ruvheneko S/C")
	LB.insert(8, "Another one")
	LB.insert(9, "Selous town centre")
	LB.insert(10, "Lolu Registrar's Ofc")
	LB.place(relx=0.35, rely=0.01)

def closePoll():
	global pollframe
	global label
	pollframe.place(relwidth=0, relheight=0)
	label.pack()
	
def pollStations():
	global pollframe
	global var
	global label
	label.place(relwidth=0, relheight=0)
	pollframe.place(relx=0, rely=0, relwidth=1, relheight=1)
	Radiobutton(pollframe, text="Bulawayo", variable=var, value=1, command=Byo).pack( anchor = W )
	Radiobutton(pollframe, text="Harare", variable=var, value=2, command=Hre).pack(anchor=W)
	Radiobutton(pollframe, text="Manicaland", variable=var, value=3, command=Mnc).pack( anchor = W )
	Radiobutton(pollframe, text="Mash Central", variable=var, value=4, command=MsC).pack( anchor = W )
	Radiobutton(pollframe, text="Mash East", variable=var, value=5, command=MsE).pack( anchor = W )
	Radiobutton(pollframe, text="Mash West", variable=var, value=6, command=MsW).pack( anchor = W )
	Radiobutton(pollframe, text="Mat North", variable=var, value=7, command=MtN).pack( anchor = W )
	Radiobutton(pollframe, text="Mat South", variable=var, value=8, command=MtS).pack( anchor = W )
	Radiobutton(pollframe, text="Midlands", variable=var, value=9, command=Mid).pack( anchor = W )
	Radiobutton(pollframe, text="Masvingo", variable=var, value=10, command=Mas).pack( anchor = W )
	Button(pollframe, text="Back!", bd=5, relief=GROOVE, command=closePoll).pack()
  
  
  
#ABOUT
abtframe =Frame(frame)
abt = Message(abtframe, text="iVote Voters Registration System (R) is an open source system for pre-registering national election voters. All information is automatically stored in the system's database for an easy retrieval. The system is designed for use only by Voter Registration Officers approved by the Zimbabwe Electoral Commission (ZEC). \n \n iVote Voters Registration System (c) 2022", fg="#263D42").pack()

def closeAbt():
	global abtframe
	abtframe.place(relwidth=0, relheight=0)
	
def about():
    global abtframe
    abtframe.place(relwidth=0.9, relheight=0.6, relx=0.05, rely=0.4)
    Button(abtframe, text="Back!", bd=5, relief=GROOVE, command=closeAbt).pack()
    
    
#menu display
menubar = Menu(window )
Accountmenu = Menu(menubar, tearoff=0)
Accountmenu.add_command(label="Signup", command=signup)
Accountmenu.add_command(label="Login", command=login)

Accountmenu.add_separator()

Accountmenu.add_command(label="Exit", command=window .quit)
menubar.add_cascade(label="Account", menu=Accountmenu)

databasemenu = Menu(menubar, tearoff=0)
databasemenu.add_command(label="Sort by:", state=DISABLED)

databasemenu.add_separator()
databasemenu.add_command(label="Voter's Name", command=nameVroll)
databasemenu.add_command(label="Voter's Age", command=ageVroll)
databasemenu.add_command(label="Province", command=provVroll)
databasemenu.add_command(label="Registration Date", command=dateVroll)

menubar.add_cascade(label="Voters Database", menu=databasemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Polling Stations", command=pollStations)
helpmenu.add_command(label="About...", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

window .config(menu=menubar)



#################################

#Display entry fields
Lname = Label(mid_frame, text="Voter's  name: ", bg="#EEEEEE")
Lname.pack()
gName = Entry(mid_frame, width = 20)
gName.pack()
Label(mid_frame,  bg="#EEEEEE").pack()
Lage = Label(mid_frame, text="Voter's  age: ",  bg="#EEEEEE")
Lage.pack()
gAge = Entry(mid_frame, width = 5)
gAge.pack()
Label(mid_frame,  bg="#EEEEEE").pack()
Lid = Label(mid_frame, text="National ID Num: ",  bg="#EEEEEE")
Lid.pack()
gID = Entry(mid_frame, width = 20)
gID.pack()
Label(mid_frame,  bg="#EEEEEE").pack()
Lprov = Label(mid_frame, text="Province: ",  bg="#EEEEEE")
Lprov.pack()
gProv = Entry(mid_frame, width = 20)
gProv.pack()



#Lower frame
lower_frame = Frame(window)
#lower_frame.place(relwidth=1, relheight =0.12, rely=0.88)


#V_ENTRY Buttons
Button(lower_frame, text="Register!", command=Register, bg="#263D42", fg="white").pack()
Button(lower_frame, text="BACK!", command=Back, bg="#263D42", fg="white").pack()


window.mainloop()
