import tkinter as tk

#Creating Windows
class FirstWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(padx = 10, pady = 10)
        
        

class SecondWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.pack(padx = 10, pady = 10)

        #btn = tk.Button(SecondWindow, text="Order", command= self.OpenLogInWindow)
        #btn.pack(padx=20, pady=20)


class ThirdWindow(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self,text = "Main Window 3").pack(padx = 10, pady = 10)
        self.pack(padx = 10, pady = 10)



class MainWindow():
    def __init__(self, master):
        mainframe = tk.Frame(master)
        mainframe.pack(padx=10, pady=20, fill='both', expand=1)
        self.index = 0
        master.geometry("1500x980")
        mainframe.place(x=0, y=0)

        self.frameList = [FirstWindow(mainframe), SecondWindow(mainframe)]
        self.frameList[1].forget()

        root.wm_title("NameHere")

        bottomframe = tk.Frame(master)
        bottomframe.pack(padx=200, pady=200)
        bottomframe.place(x=0, y=350)

        orderbtn = tk.Button(mainframe, text = "Order", command= self.changeWindow)
        orderbtn.pack(padx=100, pady=10)
        orderbtn.place(x=0,y=0)

        btn = tk.Button(mainframe, text="Log in", command= self.OpenLogInWindow) 
        btn.pack(padx=20, pady=20)
        btn.place(x=70,y=0)

    def changeWindow(self):
        self.frameList[self.index].forget()
        self.index = (self.index + 1) % len(self.frameList)
        self.frameList[self.index].tkraise()
        self.frameList[self.index].pack(padx = 10, pady = 10)

    def OpenLogInWindow(self):
        newWindow = tk.Toplevel(root)
        newWindow.geometry("500x600+720+250")
        newWindow.title("Log in Window")
       

root = tk.Tk()
window = MainWindow(root)
root.mainloop()
