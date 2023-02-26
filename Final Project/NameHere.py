from tkinter import *


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        btn = Button(root, text="Order", command=self.OpenOrderWindow, width=18,
                     height=2, background='Black', foreground='White', font='TimesNewRoman')
        btn.place(x=250, y=300)

        btn = Button(root, text="New Releases", command=self.OpenNewReleasesWindow, width=18,
                     height=2, background='Black',  foreground='White', font='TimesNewRoman')
        btn.place(x=525, y=300)

        btn = Button(root, text="Log In", command=self.OpenLogInWindow, width=18,
                     height=2, background='Black',  foreground='White', font='TimesNewRoman')
        btn.place(x=825, y=300)

        btn = Button(root, text="Sign In", command=self.OpenSignInWindow, width=18,
                     height=2, background='Black',  foreground='White', font='TimesNewRoman')
        btn.place(x=1100, y=300)

    def OpenNewReleasesWindow(self):
        newWindow = Toplevel(root)
        newWindow.geometry("500x600+720+250")
        newWindow.title("New Releases Window")

    def OpenLogInWindow(self):
        newWindow = Toplevel(root)
        newWindow.geometry("500x600+720+250")
        newWindow.title("Log In Window")

    def OpenSignInWindow(self):
        newWindow = Toplevel(root)
        newWindow.geometry("500x600+720+250")
        newWindow.title("Sign In Window")

    def OpenOrderWindow(self):
        newWindow = Toplevel(root)
        newWindow.geometry("500x600+720+250")
        newWindow.title("Order Window")

    def exitProgram(self):
        exit()


# Creating window and setting resolution
root = Tk()
app = Window(root)
root.geometry("1500x980")
# root.tk.call('tk', 'scaling', 2.0)

# Button Order and a function.


def func():
    print("It works")


# set window title
root.wm_title("NameHere")

# show window
root.mainloop()
