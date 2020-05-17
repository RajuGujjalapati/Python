from tkinter import *
root=Tk()
root.geometry("700x300")
def getvals():
    print(f"The username is {fnamevalue.get()}")#get the user values 
    print(f"The password is {lnamevalue.get()}")
    with open("records.txt", "a") as f:
        f.write(f"{fnamevalue.get(), lnamevalue.get()}\n")
Label(root, text="Dance Club", fg = "green", font = "verdana 24 bold").grid(row = 0, column = 5, pady = 5)
fname = Label(root, text = "First Name")
lname = Label(root, text = "Last Name")

fname.grid(row = 1, pady = 5)
lname.grid(row = 2, pady = 5)


#user_name=Label(root, text="user name")
#password=Label(root, text="password")
#user_name.grid()
#password.grid(row=1)
#entry widget - we can give values.
# variables classes in tkinter
 #BooleanVar,DoubleVar, IntVar, StringVar
fnamevalue=StringVar()
lnamevalue=StringVar()
userentry = Entry(root, textvariable= fnamevalue)
passentry = Entry(root, textvariable=lnamevalue)
userentry.grid(row=1, column=1)
passentry.grid(row=2, column=1)
Button(text="submit", command=getvals).grid()
root.mainloop()
