from tkinter import *
root=Tk()
root.geometry("500x400")
f1=Frame(root, borderwidth=6, bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,fill="y")#filled to y

f2=Frame(root,borderwidth=3, bg="grey",relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l=Label(f1,text="ADD",pady=50)
l.pack(pady=100)#to get cntered text use padding
l1=Label(f2,text="CALCULTOR",font="Helvetica 16 bold",fg="red",pady=10)
l1.pack()#try to give padding here 
root.mainloop()
