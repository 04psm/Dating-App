from tkinter import *
from PIL import  Image,ImageTk
from tkinter import messagebox
class GUI:
    def __init__(self,f,g):
        self._root=Tk()


        self._root.minsize(400,400)
        self._root.configure(background="#10F6B5")
        self._label1=Label(self._root, text="~TINDER~",bg="#FFF100",fg="red")
        self._label1.configure(font=("Ravie",22,"bold"))
        self._label1.pack(pady=(30,30))

        self._label2 = Label(self._root, text="Email:-",bg="#30FF02",fg="#ffffff")
        self._label2.configure(font=("constantia", 13,))
        self._label2.pack(pady=(5,5))

        self._emailInput=Entry(self._root)
        self._emailInput.pack(pady=(0,20), ipady=7, ipadx=30)

        self._label3 = Label(self._root, text="Password:-",bg="#F69832",fg="#ffffff")
        self._label3.configure(font=("constantia", 13))
        self._label3.pack(pady=(5,5))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 10), ipady=7, ipadx=30)

        self._loginBtn=Button(self._root, text="Login", width=30,height=3,bg="#FA4304",fg="#ffff00", command=lambda: f(self._emailInput.get(),self._passwordInput.get()) )
        self._loginBtn.pack()

        self._label4= Label(self._root, text="NOT A MEMBER ? ",bg="#142AF8",fg="#30FF02")
        self._label4.configure(font=("Elephant", 13))
        self._label4.pack(pady=(10, 5))
        self._regBtn = Button(self._root, text="Click Here", width=10,bg="#FA29B5",fg="#ffff00",
                               command=lambda: self.regWindow(g))
        self._regBtn.pack()


        self._root.mainloop()
    def regWindow(self,g):
        self._root=Tk()
        self._root.minsize(700, 700)
        self._root.configure(background="#2CEEA9")
        self._label1 = Label(self._root, text="~TINDER~",bg="#FFF100")
        self._label1.configure(font=("Ravie", 22))
        self._label1.pack(pady=(28, 28))

        self._label2 = Label(self._root, text="Enter Your Name:-",bg="#FA4304")
        self._label2.configure(font=("constantia",11 ))
        self._label2.pack(pady=(4, 4))

        self._nameInput = Entry(self._root)
        self._nameInput.pack(pady=(0, 16), ipady=5, ipadx=25)

        self._label3 = Label(self._root, text="Enter Your Email:-",bg="#FA29B5")
        self._label3.configure(font=("constantia", 11))
        self._label3.pack(pady=(4,4))

        self._emailInput = Entry(self._root)
        self._emailInput.pack(pady=(0, 16), ipady=5, ipadx=25)

        self._label4 = Label(self._root, text="Set A Password:-",bg="#30FF02")
        self._label4.configure(font=("constantia", 11))
        self._label4.pack(pady=(4, 4))

        self._passwordInput = Entry(self._root)
        self._passwordInput.pack(pady=(0, 16), ipady=5, ipadx=25)

        self._label5 = Label(self._root, text="Enter Your Age:-", bg="#FBE60C")
        self._label5.configure(font=("constantia", 11,))
        self._label5.pack(pady=(4, 4))

        self._ageInput = Entry(self._root)
        self._ageInput.pack(pady=(0, 16), ipady=5, ipadx=25)

        self._label6 = Label(self._root, text="What Is Your Gender:-", bg="#FF7E04")
        self._label6.configure(font=("constantia", 11,))
        self._label6.pack(pady=(4, 4))

        self._genderInput = Entry(self._root)
        self._genderInput.pack(pady=(0, 16), ipady=5, ipadx=25)

        self._label7 = Label(self._root, text="What's Your City Name:-", bg="#1C04FF")
        self._label7.configure(font=("constantia", 11,))
        self._label7.pack(pady=(4, 4))

        self._cityInput = Entry(self._root)
        self._cityInput.pack(pady=(0, 15), ipady=5, ipadx=25)

        self._label8 = Label(self._root, text="Tell Something About You:-", bg="#FF0E34")
        self._label8.configure(font=("constantia", 11,))
        self._label8.pack(pady=(4, 4))

        self._bioInput = Entry(self._root)
        self._bioInput.pack(pady=(0, 20), ipady=5, ipadx=50)

        self._registerBtn = Button(self._root, text="Register", width=30, height=2,
                                command=lambda: g(self._nameInput.get(),self._emailInput.get(),self._passwordInput.get(),self._ageInput.get(),self._genderInput.get(),self._cityInput.get(),self._bioInput.get()))
        self._registerBtn.pack()

        self._root.mainloop()

    def clearScreen(self):
        for i in self._root.pack_slaves():
            i.destroy()

    def clearScreen1(self):
        for i in self._root.grid_slaves():
            i.destroy()

    def headerMenu(self,other):
        menu = Menu(self._root)
        self._root.config(menu=menu)
        filemenu = Menu(menu)
        menu.add_cascade(label="Home", menu=filemenu)
        filemenu.add_command(label="My Profile", command=lambda: self.mainWindow())
        filemenu.add_command(label="Edit Profile", command=lambda: self.clearScreen())
        filemenu.add_command(label="View Profile", command=lambda: other.viewUsers(0))
        filemenu.add_command(label="LogOut", command=lambda: self.clearScreen())

        helpmenu = Menu(menu)
        menu.add_cascade(label="Proposals", menu=helpmenu)
        helpmenu.add_command(label="My Proposals", command=lambda: self.clearScreen())
        helpmenu.add_command(label="My Requests", command=lambda: self.clearScreen())
        helpmenu.add_command(label="My Matches", command=lambda: self.clearScreen())

    def mainWindow(self, other, data,mode,num=0):
        self.clearScreen()
        self.headerMenu(other)

        imagUrl= "imag_9.png"

        load = Image.open(imagUrl)
        load = load.resize((200, 200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        img = Label(image=render)
        img.image = render
        img.pack()

        self.label1=Label(self._root,text="Name: ",bg="#FA03D2")
        self.label1.configure(font=("Forte",18))
        self.label1.pack()

        name=data[0][1]
        self.label2 = Label(self._root, text=name,bg="#03FAED")
        self.label2.configure(font=("Forte", 18))
        self.label2.pack()

        self.label3 = Label(self._root, text="Age: ",bg="#FA0603")
        self.label3.configure(font=("Castellar", 18))
        self.label3.pack()

        age=str(data[0][4])
        self.label4 = Label(self._root, text=age,bg="#FF011D")
        self.label4.configure(font=("Bernard MT Condensed", 15))
        self.label4.pack()

        self.label5 = Label(self._root, text="Not interested in:",bg="#FAF903")
        self.label5.configure(font=("Bernard MT Condensed", 15))
        self.label5.pack()

        gender=data[0][5]
        self.label6 = Label(self._root, text=gender,bg="#3F37DB")
        self.label6.configure(font=("Bernard MT Condensed", 15))
        self.label6.pack()

        self.label7 = Label(self._root, text="I Am From:", bg="#F506F3")
        self.label7.configure(font=("Bernard MT Condensed", 15))
        self.label7.pack()

        city = data[0][7]
        self.label8 = Label(self._root, text=city, bg="#E72755")
        self.label8.configure(font=("Bernard MT Condensed", 15))
        self.label8.pack()

        self.label9 = Label(self._root, text="About Me:" ,bg="#F1FB0C")
        self.label9.configure(font=("Bernard MT Condensed", 15))
        self.label9.pack()

        bio = data[0][8]
        self.label10 = Label(self._root, text=bio, bg="#F80498")
        self.label10.configure(font=("Bernard MT Condensed", 15))
        self.label10.pack()

        if mode==2:
            frame = Frame(self._root)
            frame.pack()
            btn1 = Button(frame, text="Previous", fg="#fff", bg="#fd5068",command=lambda:other.viewUsers(num-1))
            btn1.pack(side=LEFT)
            btn2 = Button(frame, text="Propose", fg="#fff", bg="#fd5068", command=lambda: other.propose(data[0][0]))
            btn2.pack(side=LEFT)
            btn3 = Button(frame, text="Next", fg="#fff", bg="#fd5068",command=lambda:other.viewUsers(num+1))
            btn3.pack(side=LEFT)

    def printMessage(self,title,message):
        messagebox.showerror(title,message)
        
        
        
