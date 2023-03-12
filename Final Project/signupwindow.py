from tkinter import *
from tkvideo import tkvideo
from tkinter import messagebox

#Cerating the sign up function and setting it's window properties
def OpenSignUpWindow(root):
    SignUp_Window = Toplevel(root)
    SignUp_Window.geometry("500x600+720+250")
    SignUp_Window.title("Sign Up Window")
    SignUp_Window.bg = 'Grey'

    # Creating SignUp Video
    signup_video = Label(SignUp_Window) #Video label
    signup_video.place(x=-2, y=0)

    player = tkvideo("Final Project/Data/login_video.mp4",
                     signup_video, loop=True, size=(500, 600)) #Video path
    player.play()


    #Creating labels
    signup_label = Label(SignUp_Window, text='Create your account here!', font=(
        "Arial", 15), bg='Black', fg='White').place(x=130, y=120) #Main label
    

    newusername_label = Label(SignUp_Window, text='Enter your username here', font=(
        "Arial", 11), bg='Black', fg='White').place(x=90, y=160) #Username label

    password_label = Label(SignUp_Window, text='Enter password here', font=(
        "Arial", 11), bg='Black', fg='White').place(x=90, y=220) #Password label
    
    confirm_label = Label(SignUp_Window, text='Confirm your password here', font=(
        "Arial", 11), bg='Black', fg='White').place(x=90, y=280) #Confirm password label

    #Creating entries
    newusername = Entry(SignUp_Window, font=(25), border=(2))#Creating username entry
    newusername.place(x=90, y=190, width=320, height=25)

    newpassword = Entry(SignUp_Window, font=(25), border=(2))#Creating password entry
    newpassword.place(x=90, y=250, width=320, height=25)

    newpassword1 = Entry(SignUp_Window, font=(25), border=(2))#Creating confirm password label
    newpassword1.place(x=90, y=310, width=320, height=25)

    # Creating back function and button
    def back():
        SignUp_Window.destroy()

    back_b = Button(SignUp_Window, text='Back',
                    font=(20), command=back)
    back_b.place(x=200, y=370)
    #Creating createAccount function
    def createAccount():
        username = newusername.get() #Getting the values from the username entry into the username variable
        password = newpassword.get() #Getting the values from the password entry into the password variable
        confirmed_password = newpassword1.get()#Getting the values from the confirm password entry into the confirmed_password variable

        db = open("Final Project/data.txt", "r")#Opening text file to write new account
        #Creating lists
        d = []
        f = [] 
        #Spliting the values in data.txt into 2 lists, d and f
        for i in db:
            a, b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))
        
        #Checking if both passwords match
        if confirmed_password != password:
            messagebox.showerror(
                "Error", "Passwords don't match.", parent=SignUp_Window)
            #Checking if username already exists
        elif username in d:
            messagebox.showerror(
                "Error", "Username already exists.", parent=SignUp_Window)

        else:
            #Checking if password meets required length
            if len(password) < 6:
                messagebox.showerror(
                    "Error", "Password needs to be longer than 6 digits.", parent=SignUp_Window)
            else:
                #Ofening text file and writing username and password inside it
                db = open("Final Project/data.txt", "a")
                db.write(username + ", " + password+"\n")
                messagebox.showinfo(
                    title='Success!', message='Account created!')
                SignUp_Window.destroy()

    #Sign up button
    signup = Button(SignUp_Window, text='Sign Up!',
                    font=(20), command=createAccount)
    signup.place(x=90, y=370)
