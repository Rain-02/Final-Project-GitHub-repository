from tkinter import *
from tkvideo import tkvideo
from tkinter import messagebox
import signupwindow
import main_menu


# Creating Login class and setting it's window properties
class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Play Delivery")
        self.root.iconbitmap('Final Project/Data/icon.ico')
        self.root.geometry("1080x720+100+50")
        self.root.resizable(False, False)

        # Background Video

        lblVideo = Label(self.root)  # Video label
        lblVideo.place(x=-2, y=0)

        player = tkvideo("Final Project/Data/login_video.mp4",
                         lblVideo, loop=True, size=(1080, 720))  # Video player
        player.play()

        # Login Frame

        Frame_login = Frame(self.root, bg="Black")
        Frame_login.place(x=300, y=160, width=500, height=400)

        # Login Title
        title = Label(Frame_login, text='Welcome!\n Login to your account or Signup to continue.', font=(
            "Arial", 15), bg='Black', fg='White').place(x=60, y=10)

        # Username entry box
        self.username = Entry(Frame_login, font=("Arial", 10), border=(2))
        self.username.place(x=90, y=100, width=320, height=25)

        user_label = Label(Frame_login, text='Username', font=(
            "Arial", 10), bg='Black', fg='White').place(x=90, y=75)

        # Password entry box
        self.password = Entry(Frame_login, font=(
            "Arial", 10), border=(2), show="*")

        self.password.place(x=90, y=155, width=320, height=25)
        password_label = Label(Frame_login, text='Password', font=(
            "Arial", 10), bg='Black', fg='White').place(x=90, y=128)

        # Main Menu Window Function

        # SKIP BUTTON FOR TESTING PURPOSES
        skip = Button(Frame_login, text='Skip',
                      font=(20), command=lambda: main_menu.menu_window(self.root, self.username.get()))
        skip.place(x=90, y=340)

        # Creating access function
        def access():

            # Stores the value from the username entry box into the username variable.
            username = self.username.get()
            # Stores the value from the password entry box into the password variable.
            password = self.password.get()

            if not len(username or password) < 1:  # Validating if entry box is not empty

                # Opening accounts text file
                db = open("Final Project/data.txt", "r")
                # Creating lists
                d = []
                f = []
                # Spliting the values in data.txt into 2 lists, d and f
                for i in db:
                    a, b = i.split(", ")
                    b = b.strip()
                    d.append(a)
                    f.append(b)
                data = dict(zip(d, f))

                try:
                    if data[username]:
                        try:
                            if password == data[username]:
                                main_menu.menu_window(
                                    self.root, self.username.get())

                            else:
                                messagebox.showerror(
                                    "Error", "Passwords is incorrect.", parent=Frame_login)
                        except:
                            messagebox.showerror(
                                "Error", "Passwords is incorrect.", parent=Frame_login)
                    else:
                        messagebox.showerror(
                            "Error", "Username does not exist.", parent=Frame_login)
                except:
                    messagebox.showerror(
                        "Error", "Username does not exist.", parent=Frame_login)

        # Sign up button
        signup = Button(Frame_login, text='Sign Up!',
                        font=(20), command=lambda: signupwindow.OpenSignUpWindow(self.root))
        signup.place(x=90, y=235)

        # submit button
        submit = Button(Frame_login, text='Log In!', font=(20), command=access)
        submit.place(x=90, y=201)


root = Tk()
obj = Login(root)
root.mainloop()
