from tkinter import*

#Creating Windows
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
    


        #orderbtn = tk.Button(Demol, text = "Order", command= self.changeWindow)
        #orderbtn.place(x=0,y=0)


        btn = Button(Window, text="Log in", command= self.OpenLogInWindow) 
        btn.place(x=70,y=0)


    def OpenLogInWindow(self):
        newWindow = Toplevel(root)
        newWindow.geometry("500x600+720+250")
        newWindow.title("Log in Window")
       

root = Tk()
Window = Window(root)
root.mainloop()
