from tkinter import *
from PIL import Image,ImageTk
#creats one basic label
my_root=Tk()
my_root.geometry("1000x600")#widthxheight#default size
my_root.title("NANI")
my_root.minsize(400,300)#locking the minimum size
my_root.maxsize(1000,750)#locking the max. size
#only png, gif files

#for jpg image
image=Image.open("img.jpg")
photo=ImageTk.PhotoImage(image)
label=Label(image=photo)
label.pack()

##photo=PhotoImage(file="horse.png" )
#label_create=Label(text="Calculator program")
label_image=Label(image=photo)
label_image.pack()
#use pack to get the data
#label_create.pack()
my_root.mainloop()

