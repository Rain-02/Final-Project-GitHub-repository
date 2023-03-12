from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
from tkcalendar import *
import datetime


#Creating menu_window function and setting it's window properties
def menu_window(root, username):
    main_frame = Frame(root, bg="Black")
    main_frame.place(x=0, y=0, width=1080, height=720)


    #Creating main labels
    main_label = Label(main_frame, text='Welcome, ' + username+'! ',
                       font=("Arial", 15), bg='Black', fg='White').place(x=200, y=260)
    
    main_label2 = Label(main_frame, text='Choose the date and click \non the game you want to rent! ', font=("Arial", 15), bg='Black', fg='White').place(x=720, y=260)

    # Creating back to login button and function
    def BackLogin():
        main_frame.destroy()

    back_b = Button(main_frame, text='Back to login page.', font=(
        20), command=BackLogin)
    back_b.place(x=0, y=250)

    # Creating the main logo.
    main_image = ImageTk.PhotoImage(
        Image.open("Final Project/Data/logo.png"))
    main_image_label = Label(main_frame, image=main_image)
    main_image_label.photo = main_image
    main_image_label.place(x=-2, y=0)


    #Get current day into current_day variable
    current_day = datetime.datetime.now()

    # Creating the first calendar

    cal_lbl = Label(main_frame, font=('Arial', 10),
                    text="First day:", bg='Black', fg='White') #Calendar label
    cal_lbl.place(x=800, y=350)
    cal1 = DateEntry(main_frame, selectmode="day",
                     year=current_day.year, month=current_day.month, day=current_day.day) #Creating date entry using the current_day variable
    cal1.place(x=800, y=380)


    #Creating second calendar

    cal_lbl2 = Label(main_frame, font=('Arial', 10),
                     text="Return day:", bg='Black', fg='White')#Calendar label
    cal_lbl2.place(x=800, y=450)

    cal2 = DateEntry(main_frame, selectmode="day",
                     year=current_day.year, month=current_day.month, day=current_day.day)#Creating date entry using the current_day variable
    cal2.place(x=800, y=480)




    #Creating games frame
    games_frame = Frame(main_frame, bg='White')
    games_frame.place(x=0, y=320, width=630, height=400)
    #Creating a canvas
    my_canvas = Canvas(games_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    #Creating and setting up scrollbar in the canvar
    my_scrollbar = ttk.Scrollbar(
        games_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))
    
    #Creating another frame to be used.
    second_frame = Frame(my_canvas)
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    #Creating and setting up the select function and it's windows properties
    def select(gamename, image, synopsis):
        select_window = Toplevel(root) #Creating another window
        select_window.geometry("500x600+720+250")
        select_window.title("Rent!")

        frame = Frame(select_window, bg='Black') #Creating a frame
        frame.place(x=0, y=0, width=1080, height=720)

        #Setting up game image
        game_image = ImageTk.PhotoImage(Image.open(image))#Opening image
        game_image_label = Label(frame, image=game_image)#Creating label for the image
        game_image_label.photo = game_image #Setting label as image
        game_image_label.place(x=145, y=0)
        select_window.resizable(False, False)

        #Creating gamename label
        gamename_lbl = Label (frame, font=('Arial', 15), text=gamename, fg='White', bg='Black')
        gamename_lbl.place(x=180, y=260)

        #Creating synopsis text box to be used as a text display
        synopsis_w = Text(frame, width=35, height=10, font=(
            'Arial', 12), fg='White', bg='Black', wrap=WORD, borderwidth=0)
        synopsis_w.place(x=60, y=300)
        synopsis_w.insert(INSERT, synopsis) #Inserting text into text box
        synopsis_w['state'] = 'disabled' #Disabling text box so it can't be interacted with
        #synopsis_w.tag_config()
        #Creating date function
        def date():
            lbl = Label(frame, font=('Arial', 10), text="You've set the date to rent " +
                        gamename+" from "+cal1.get()+" to "+cal2.get(), bg='Black', fg='White')
            lbl.place(x=70, y=500)
            #Creating message function
            def message():
                messagebox.showinfo(title='Success!', message="The game you chose will arrive at your address on " +
                                    cal1.get()+", you are expected to send it back on "+cal2.get()+".\nEnjoy the game!")
                select_window.destroy()
            #Creating confirm button to call the date function
            confirm = Button(frame, text='Click here to confirm', font=(
                20), command=message, bd=2)
            confirm.place(x=170, y=550)
        #Creating rent button to call the date function
        rent = Button(frame, text='Rent!', font=(
            20), command=date, width=10, bd=2)
        rent.place(x=200, y=550)

    #Creating game_images function to store all of the game images
    def game_images():
        #Setting up game image and label
        game_image = ImageTk.PhotoImage(Image.open(
            "Final Project/Data/game_icons/sonic.png"))
        game_image_label = Label(second_frame, image=game_image)
        game_image_label.photo = game_image
        #Setting up game button
        game1 = Button(second_frame, image=game_image, font=(20), command=lambda: select(
            "Sonic Frontiers", "Final Project/Data/game_icons/sonic.png", "Worlds are colliding in Sonic the Hedgehog's newest high-speed adventure. \n In search of the missing Chaos emeralds, Sonic becomes stranded on an ancient island teeming with unusual creatures.\n Battle hordes of powerful enemies as you explore a breathtaking world of action, adventure, and mystery."))
        game1.grid(row=0, column=0)
        #Setting up game image and label
        game_image2 = ImageTk.PhotoImage(Image.open(
            "Final Project/Data/game_icons/dead_space.png"))
        game_image_label2 = Label(second_frame, image=game_image2)
        game_image_label2.photo = game_image2
        #Setting up game button
        game2 = Button(second_frame, image=game_image2, font=(20), command=lambda: select(
            "Dead Space", "Final Project/Data/game_icons/dead_space.png", "The sci-fi survival-horror classic returns, completely rebuilt to offer an even more immersive experience — including visual, audio, and gameplay improvements — while staying faithful to the original game’s thrilling vision."))
        game2.grid(row=0, column=1)
        #Setting up game image and label
        game_image3 = ImageTk.PhotoImage(Image.open(
            "Final Project/Data/game_icons/god_of_war.png"))
        game_image_label3 = Label(second_frame, image=game_image3)
        game_image_label3.photo = game_image3
        #Setting up game button
        game3 = Button(second_frame, image=game_image3, font=(20),  command=lambda: select(
            "God Of War", "Final Project/Data/game_icons/god_of_war.png", "His vengeance against the Gods of Olympus years behind him, Kratos now lives as a man in the realm of Norse Gods and monsters. It is in this harsh, unforgiving world that he must fight to survive… and teach his son to do the same."))
        game3.grid(row=0, column=2)
        #Setting up game image and label
        game_image4 = ImageTk.PhotoImage(Image.open(
            "Final Project/Data/game_icons/horizon.png"))
        game_image_label4 = Label(second_frame, image=game_image4)
        game_image_label4.photo = game_image4
        #Setting up game button
        game4 = Button(second_frame, image=game_image4, font=(20), command=lambda: select(
            "Horizon Zero Dawn", "Final Project/Data/game_icons/horizon.png", "Horizon Forbidden West continues the story of Aloy, a young hunter of the Nora tribe and a clone of the Old World scientist Elisabet Sobeck, as she leads a band of companions on a quest to the arcane frontier known as the Forbidden West to find the source of a mysterious plague that kills all it infects."))
        game4.grid(row=1, column=0)
        #Setting up game image and label
        game_image5 =ImageTk.PhotoImage(Image.open(
            "Final Project/Data/game_icons/nba.png"))
        game_image_label5 = Label(second_frame, image=game_image5)
        game_image_label5.photo = game_image5
        #Setting up game button
        game5 = Button(second_frame, image=game_image5, font=(
            20), command=lambda: select("NBA2K23", "Final Project/Data/game_icons/nba.png", "Rise to the occasion in NBA 2K23. Showcase your talent in MyCAREER. Pair All-Stars with timeless legends in MyTEAM. Build your own dynasty in MyGM, or guide the NBA in a new direction with MyLEAGUE."))
        game5.grid(row=1, column=1)
        #Setting up game image and label
        game_image6 = ImageTk.PhotoImage(
            Image.open("Final Project/Data/game_icons/guardians.png"))
        game_image_label6 = Label(second_frame, image=game_image6)
        game_image_label6.photo = game_image6
        #Setting up game button
        game6 = Button(second_frame, image=game_image6, font=(
            20), command=lambda: select("Guardians of the Galaxy", "Final Project/Data/game_icons/guardians.png", "Fire up a wild ride across the cosmos with a fresh take on Marvel’s Guardians of the Galaxy. In this action-adventure game, you are Star-Lord leading the unpredictable Guardians from one explosion of chaos to the next."))
        game6.grid(row=1, column=2)
        #Setting up game image and label
        game_image7 = ImageTk.PhotoImage(Image.open(
            "Final Project/Data/game_icons/the_last_of_us.png"))
        game_image_label7 = Label(second_frame, image=game_image7)
        game_image_label7.photo = game_image7
        #Setting up game button
        game7 = Button(second_frame, image=game_image7, font=(
            20), command=lambda: select("The Last Of Us. Part 1", "Final Project/Data/game_icons/the_last_of_us.png", "Experience the emotional storytelling and unforgettable characters in The Last of Us™, winner of over 200 Game of the Year awards."))
        game7.grid(row=2, column=0)
        #Setting up game image and label
        game_image8 = ImageTk.PhotoImage(Image.open(
            "Final Project/Data/game_icons/demon_slayer.png"))
        game_image_label8 = Label(second_frame, image=game_image8)
        game_image_label8.photo = game_image8
        #Setting up game button
        game8 = Button(second_frame, image=game_image8, font=(
            20), command=lambda: select("Demon Slayer", "Final Project/Data/game_icons/demon_slayer.png", "Become the Blade that Destroys Demons!"))
        game8.grid(row=2, column=1)
        #Setting up game image and label
        game_image9 = ImageTk.PhotoImage(
            Image.open("Final Project/Data/game_icons/atomic.png"))
        game_image_label9 = Label(second_frame, image=game_image9)
        game_image_label9.photo = game_image9
        #Setting up game button
        game9 = Button(second_frame, image=game_image9, font=(
            20), command=lambda: select("Atomic Heart", "Final Project/Data/game_icons/atomic.png", "In a mad and sublime utopian world, take part in explosive encounters. Adapt your fighting style to each opponent, use your environment and upgrade your equipment to fulfill your mission."))
        game9.grid(row=2, column=2)
        #Setting up game image and label
        game_image10 = ImageTk.PhotoImage(
            Image.open("Final Project/Data/game_icons/elden.png"))
        game_image_label10 = Label(second_frame, image=game_image10)
        game_image_label10.photo = game_image10
        #Setting up game button
        game10 = Button(second_frame, image=game_image10, font=(
            20), command=lambda: select("Elden Ring", "Final Project/Data/game_icons/elden.png", "Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between."))
        game10.grid(row=3, column=0)
        #Setting up game image and label
        game_image11 = ImageTk.PhotoImage(
            Image.open("Final Project/Data/game_icons/fifa.png"))
        game_image_label11 = Label(second_frame, image=game_image11)
        game_image_label11.photo = game_image11
        #Setting up game button
        game11 = Button(second_frame, image=game_image11, font=(
            20), command=lambda: select("FIFA23", "Final Project/Data/game_icons/fifa.png", "FIFA 23 brings The World’s Game to the pitch, with HyperMotion2 Technology, men’s and women’s FIFA World Cup™coming during the season, women’s club teams, cross-play features*, and more."))
        game11.grid(row=3, column=1)
        #Setting up game image and label
        game_image12 = ImageTk.PhotoImage(
            Image.open("Final Project/Data/game_icons/hogwarts.png"))
        game_image_label12 = Label(second_frame, image=game_image12)
        game_image_label12.photo = game_image12
        #Setting up game button
        game12 = Button(second_frame, image=game_image12, font=(
            20), command=lambda: select("Hogwarts Legacy", "Final Project/Data/game_icons/hogwarts.png", "Hogwarts Legacy is an immersive, open-world action RPG. Now you can take control of the action and be at the center of your own adventure in the wizarding world."))
        game12.grid(row=3, column=2)
    game_images()
