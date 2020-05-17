from tkinter import *
root=Tk()
root.geometry("700x300")
frame=Frame(root,borderwidth=6, bg="grey", relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")
def hello():
    print("CHECKING FOR TKINTER BUTTON")
def name():
    print("RAJU")
b1=Button(frame,fg="red",text="print", command=hello)
b1.pack(side=LEFT, padx=20)
#COMMAND executes the function and gives the results when we clicks
b2=Button(frame,fg="red",text="print",command=name)
b2.pack(side=LEFT)
b3=Button(frame,fg="red",text="print")
b3.pack(side=LEFT)
b4=Button(frame,fg="red",text="print")
b4.pack(side=TOP)
root.mainloop()
