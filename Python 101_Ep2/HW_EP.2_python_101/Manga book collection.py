from tkinter import *
from PIL import Image, ImageTk #เอารูปเข้ามาใส่
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk() #หน้าจอหลักของโปรแกรม
GUI.geometry('400x400') #ขนาดของโปรแกรม
GUI.resizable(False,False) #ล็อคขนาดหน้าจอไม่ให้ขยับ
GUI.title('Manga book collection') #ชื่อโปรแกรม
GUI.iconbitmap('IC_Book.ico') #เปลี่ยนรูป icon
GUI.option_add('*Font', 'Tahoma 12') #ปรับตั้งฟ้อนต์ขนาดตัวหนังสือ


L1 = Label(GUI,text='Program Manga book collections',font=('Tahoma',18),fg='blue',bg='peru')
L1.place(x=10 ,y=15)
##########################################################################

def Button():
    text = 'Bleach'
    img = Image.open('Bleach.jpg') #ดึงไฟล์ภาพ
    img = img.resize((int(img.width * .25), int(img.height * .25))) #ย่อขนาดของรูปที่เอาเข้ามาใส
    photo = ImageTk.PhotoImage(img)
    A1 = Label(image=photo).place(x=200,y=60)
    messagebox.showinfo('หนังสือที่เลือก',text)

FB1 = Frame(GUI) #สร้างกรอบครอบไว้
FB1.place(x=30 ,y=60)
B1 = ttk.Button(FB1,text='Bleach',command=Button)
B1.pack(ipadx=15,ipady=10)
##########################################################################

def Button1():
    text = 'Demon slayer'
    img = Image.open('Demon slayer.jpg') #ดึงไฟล์ภาพ
    img = img.resize((int(img.width * .25), int(img.height * .25))) #ย่อขนาดของรูปที่เอาเข้ามาใส
    photo = ImageTk.PhotoImage(img)
    A1 = Label(image=photo).place(x=200,y=60)
    messagebox.showinfo('หนังสือที่เลือก',text)

FB2 = Frame(GUI) #สร้างกรอบครอบไว้
FB2.place(x=30 ,y=60)
B2 = ttk.Button(FB1,text='Demon slayer',command=Button1)
B2.pack(ipadx=15,ipady=10)
##########################################################################

def Button2():
    text = 'Dragon ball'
    img = Image.open('Dragon Ball.jpg') #ดึงไฟล์ภาพ
    img = img.resize((int(img.width * .25), int(img.height * .25))) #ย่อขนาดของรูปที่เอาเข้ามาใส
    photo = ImageTk.PhotoImage(img)
    A1 = Label(image=photo).place(x=200,y=60)
    messagebox.showinfo('หนังสือที่เลือก',text)

FB3 = Frame(GUI) #สร้างกรอบครอบไว้
FB3.place(x=30 ,y=60)
B3 = ttk.Button(FB1,text='Dragon ball',command=Button2)
B3.pack(ipadx=15,ipady=10)
##########################################################################

def Button3():
    text = 'Naruto'
    img = Image.open('Naruto.jpg') #ดึงไฟล์ภาพ
    img = img.resize((int(img.width * .25), int(img.height * .25))) #ย่อขนาดของรูปที่เอาเข้ามาใส
    photo = ImageTk.PhotoImage(img)
    A1 = Label(image=photo).place(x=200,y=60)
    messagebox.showinfo('หนังสือที่เลือก',text)

FB4 = Frame(GUI) #สร้างกรอบครอบไว้
FB4.place(x=30 ,y=60)
B4 = ttk.Button(FB1,text='Naruto',command=Button3)
B4.pack(ipadx=15,ipady=10)
##########################################################################

def Button4():
    text = 'One piece'
    img = Image.open('One piece.jpg') #ดึงไฟล์ภาพ
    img = img.resize((int(img.width * .25), int(img.height * .25))) #ย่อขนาดของรูปที่เอาเข้ามาใส
    photo = ImageTk.PhotoImage(img)
    A1 = Label(image=photo).place(x=200,y=60)
    messagebox.showinfo('หนังสือที่เลือก',text)

FB5 = Frame(GUI) #สร้างกรอบครอบไว้
FB5.place(x=30 ,y=60)
B5 = ttk.Button(FB1,text='One piece',command=Button4)
B5.pack(ipadx=15,ipady=10)
##########################################################################

def Button5():
    text = 'The Breaker'
    img = Image.open('The Breaker.jpg') #ดึงไฟล์ภาพ
    img = img.resize((int(img.width * .25), int(img.height * .25))) #ย่อขนาดของรูปที่เอาเข้ามาใส
    photo = ImageTk.PhotoImage(img)
    A1 = Label(image=photo).place(x=200,y=60)
    messagebox.showinfo('หนังสือที่เลือก',text)

FB6 = Frame(GUI) #สร้างกรอบครอบไว้
FB6.place(x=30 ,y=60)
B6 = ttk.Button(FB1,text='The Breaker',command=Button5)
B6.pack(ipadx=15,ipady=10)
##########################################################################

def Button6():
    text = 'มหาเวทย์ผนึกมาร'
    img = Image.open('มหาเวทย์ผนึกมาร.jpg') #ดึงไฟล์ภาพ
    img = img.resize((int(img.width * .25), int(img.height * .25))) #ย่อขนาดของรูปที่เอาเข้ามาใส
    photo = ImageTk.PhotoImage(img)
    A1 = Label(image=photo).place(x=200,y=60)
    messagebox.showinfo('หนังสือที่เลือก',text)

FB7 = Frame(GUI) #สร้างกรอบครอบไว้
FB7.place(x=30 ,y=60)
B7 = ttk.Button(FB1,text='มหาเวทย์ผนึกมาร',command=Button6)
B7.pack(ipadx=15,ipady=10)
##########################################################################
    
GUI.mainloop()



