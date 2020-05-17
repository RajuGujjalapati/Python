from tkinter import *
root=Tk()
root.geometry("1000x500")
#root.config(bg="skyblue")
#heading
Label(root, text="welcome to raju travels:",pady=15, font="comicsansms 13 bold").grid(row=0, column=3)
#text for our form
def getvals():
    print("WORKING SUCCESSFULLY")
name = Label(root, text="name")
phone = Label(root, text="phone")
gender= Label(root, text="gender")
emergency= Label(root, text="Emergency contact")
paymentmode= Label(root, text="payment mode")

#pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

#Tkinter values for storing  entries
namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentmodevalue=StringVar()
foodservicesvalue=IntVar()

#Entries for our form
nameentry=Entry(root, textvariable=namevalue)
phoneentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymentmodeentry=Entry(root, textvariable=paymentmodevalue)
#packing the entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)
#check box and packing it
foodservice=Checkbutton(text="would you like to add food services?:", variable=foodservicesvalue)
foodservice.grid(row=6, column=3)
#button , packing and assign it
Button(text="SUBMIT", command=getvals).grid(row=7, column=3)
root.mainloop()
