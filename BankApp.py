from tkinter import *  # importing gui library
from tkinter import ttk #This line imports the ttk (Themed Tkinter) module, which is part of the standard tkinter library in Python.
# It allows you to use modern, themed widgets that look more native to the operating system.

from tkinter.messagebox import *
import sqlite3  
import database # will import database.py

from PIL import Image, ImageTk

conn = sqlite3.Connection("mydatabase.db")
#it will create a database name "mydatabase.db" inside our folder
#conn is connection object

database.create_table(conn)

current_account = None # To store the account number of the logged-in user

def AdminWindow():
    clearWindow() #will clear the previous screen
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=85)
    ttk.Label(frame, text="ADMIN WINDOW", font="ariel 40 bold").grid(row=0, column=0, columnspan=2, pady=20)
    # label takes name of window ("win") and text to display as input and its font
    # label is for showing text on window
    # pady for some space between boxes of text vertically
    #In Tkinter, the columnspan option (used with the grid() geometry manager) specifies how many columns a widget should span across

    ttk.Button(frame, text="VIEW   ALL   TRANSACTIONS", width=55, command=ViewTransactionsWindow).grid(row=1, column=0, pady=20)
    #same as label above , width makes the button wide
    #button is for creating button on window
    #command will do what will happen after clicking the button

    ttk.Button(frame, text="VIEW   ALL   ACCOUNTS", width=55, command=ViewAllAccounts).grid(row=2, column=0, pady=20)
    ttk.Button(frame, text="LOGOUT", width=55, command=LoginWindow).grid(row=3, column=0, pady=20)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    #If frame is a shelf, then:frame.winfo_children() is the list of books on the shelf. & widget is each individual book. & grid_configure(...) adds space around each book to make it easier to read.    
    frame.tkraise()  

def ViewTransactionsWindow():
    clearWindow()
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=100)
    ttk.Label(frame, text="All Transactions", font="ariel 25 bold").grid(row=0, column=0, pady=10)
    transactions = database.get_all_transactions(conn)
    for i, t in enumerate(transactions):
        ttk.Label(frame, text=f"Acc:{t[1]} | {t[2]} | ${t[3]} | {t[4]}",font="ariel 15 bold").grid(row=i+1, column=0, sticky="w") # 'sticky=w' means make it appear on west side of screen
    ttk.Button(frame, text="Back", width=25, command=AdminWindow).grid(row=len(transactions)+2, column=0, pady=10)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    frame.tkraise()      

def ViewAllAccounts():
    clearWindow()
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=100)
    ttk.Label(frame, text="All Accounts", font="ariel 25 bold").grid(row=0, column=0, pady=10)
    accounts = database.get_all_accounts(conn)
    for i, acc in enumerate(accounts):
        ttk.Label(frame, text=f"Accno: {acc[0]}, Name: {acc[1]}, Balance: {acc[2]}",font="ariel 15 bold").grid(row=i+1, column=0, sticky="w")
    ttk.Button(frame, text="Back", width=25, command=AdminWindow).grid(row=len(accounts)+2, column=0, pady=10)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    frame.tkraise()      

def LoginWindow():
    clearWindow()

    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window

    frame = ttk.Frame(win)
    frame.pack(pady=110)
    ttk.Label(frame, text="BANK", font="ariel 30 bold").grid(row=0, column=0, columnspan=2, pady=10)
    ttk.Label(frame, text="Login Account Number:", font="ariel 20 bold").grid(row=1, column=0, pady=5, sticky="e")
    E1 = ttk.Entry(frame, width=30) #uses entry field to take input from user
    E1.grid(row=1, column=1, pady=5)
    ttk.Label(frame, text="Login Password:", font="ariel 20 bold").grid(row=2, column=0, pady=5, sticky="e")
    E2 = ttk.Entry(frame, width=30, show="*")
    E2.grid(row=2, column=1, pady=5)
    ttk.Button(frame, text="Login", width=20, command=lambda: validate_login(E1.get(), E2.get())).grid(row=3, column=0, columnspan=2)
    ttk.Button(frame, text="Create New Account", width=20, command=OpenAccountWindow).grid(row=4, column=0, columnspan=2, pady=25)
    ttk.Button(frame, text="Exit", width=20, command=win.destroy).grid(row=5, column=0, columnspan=2)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)

    # Bring the frame to the front
    frame.tkraise()    

def validate_login(accno, password):
    global current_account
    if not accno or not password:
        showwarning("Input Error", "Both account number and password are required.")
        return
    result = database.validate_login_db(conn, accno, password)
    if result == "admin":
        showinfo("Admin Login", "Welcome Admin!")
        AdminWindow() # takes to admin screen
    elif result == "user":
        current_account = accno
        showinfo("Login Success", "Welcome to your account!")
        MainWindow()
    else:
        showwarning("Login Failed", "Invalid account number or password.")

def MainWindow():
    clearWindow()
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=100)
    ttk.Label(frame, text="CUSTOMER WINDOW", font="ariel 30 bold").grid(row=0, column=0, columnspan=2, pady=10)
    ttk.Button(frame, text="Check Balance", width=70, command=CheckBalanceWindow).grid(row=1, column=0, pady=5)
    ttk.Button(frame, text="Deposit Amount", width=70, command=DepositWindow).grid(row=2, column=0, pady=5)
    ttk.Button(frame, text="Withdraw Amount", width=70, command=WithdrawWindow).grid(row=3, column=0, pady=5)
    ttk.Button(frame, text="Logout", width=70, command=Logout).grid(row=4, column=0, pady=5)
    ttk.Button(frame, text="Exit", width=70, command=win.destroy).grid(row=5, column=0, pady=5)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    frame.tkraise()      

def Logout():
    global current_account
    current_account = None
    showinfo("Logout", "You have been logged out.")
    LoginWindow() 

def validate_and_create_account(accno, name, balance, password):
    if not accno or not name or not balance or not password:
        showwarning("Input Error", "All fields are required.")
        return
    if accno == "123":
        showwarning("Input Error", "Account Number cannot be 123")
        return
    database.openAccount_db(conn, accno, name, balance, password)

def OpenAccountWindow():
    clearWindow()
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=110)
    ttk.Label(frame, text="OPEN NEW ACCOUNT", font="ariel 30 bold").grid(row=0, column=0, columnspan=2, pady=5)
    ttk.Label(frame, text="Enter Account Number", font="ariel 15 bold").grid(row=1, column=0, pady=5, sticky="e")
    E1 = ttk.Entry(frame, width=20)
    E1.grid(row=1, column=1, pady=5)
    ttk.Label(frame, text="Enter Name", font="ariel 15 bold").grid(row=2, column=0, pady=5, sticky="e")
    E2 = ttk.Entry(frame, width=20)
    E2.grid(row=2, column=1, pady=5)
    ttk.Label(frame, text="Enter Initial Balance", font="ariel 15 bold").grid(row=3, column=0, pady=5, sticky="e")
    E3 = ttk.Entry(frame, width=20)
    E3.grid(row=3, column=1, pady=5)
    ttk.Label(frame, text="Set Password", font="ariel 15 bold").grid(row=4, column=0, pady=5, sticky="e")
    E4 = ttk.Entry(frame, width=20)
    E4.grid(row=4, column=1, pady=5)
    ttk.Button(frame, text="CREATE", width=70, command=lambda: validate_and_create_account(E1.get(), E2.get(), E3.get(), E4.get())).grid(row=5, column=0, columnspan=2, pady=5)
    ttk.Button(frame, text="BACK", width=70, command=LoginWindow).grid(row=6, column=0, columnspan=2, pady=5)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    frame.tkraise()      

def CheckBalanceWindow():
    clearWindow()
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=125)
    ttk.Label(frame, text="Check Balance", font="ariel 35 bold").grid(row=0, column=0, columnspan=2, pady=25)
    ttk.Label(frame, text="Account number", font="ariel 12 bold").grid(row=1, column=0, pady=5, sticky="e")
    E1 = ttk.Entry(frame, width=30)
    E1.grid(row=1, column=1, pady=5)
    E1.insert(0, current_account) # Pre-fill with logged-in account
    E1.config(state='readonly') # Make it read-only
    ttk.Button(frame, text="ENTER", width=70, command=lambda: database.CheckBalance_db(conn, current_account)).grid(row=2, column=0, columnspan=2, pady=5)
    ttk.Button(frame, text="BACK", width=70, command=MainWindow).grid(row=3, column=0, columnspan=2, pady=5)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    frame.tkraise()      

def DepositWindow():
    clearWindow()
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=125)
    ttk.Label(frame, text="DEPOSIT", font="ariel 35 bold").grid(row=0, column=0, columnspan=2, pady=5)
    ttk.Label(frame, text="Account number", font="ariel 12 bold").grid(row=1, column=0, pady=5, sticky="e")
    E1 = ttk.Entry(frame, width=30)
    E1.grid(row=1, column=1, pady=5)
    E1.insert(0, current_account)
    E1.config(state='readonly')
    ttk.Label(frame, text="Enter Amount", font="ariel 12 bold").grid(row=2, column=0, pady=5, sticky="e")
    E2 = ttk.Entry(frame, width=30)
    E2.grid(row=2, column=1, pady=5)
    ttk.Button(frame, text="PAY", width=70, command=lambda: database.deposit_db(conn, E1.get(), E2.get())).grid(row=3, column=0, columnspan=2, pady=5)
    ttk.Button(frame, text="BACK", width=70, command=MainWindow).grid(row=4, column=0, columnspan=2, pady=5)


    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    frame.tkraise()      

def validate_and_withdraw(accno, amount):
    if not accno or not amount:
        showwarning("Input Error", "Both fields are required.")
        return
    database.withdraw_db(conn, accno, amount)

def WithdrawWindow():
    clearWindow()
    image = Image.open("bck.png")

    # Resize image to fit window or a specific size if needed
    image = image.resize((1920, 1080), Image.LANCZOS) # Image.LANCZOS is a high-quality resampling filter used when resizing images with Pillow (Python Imaging Library). It’s excellent for reducing images while keeping them smooth and sharp.
    
    photo = ImageTk.PhotoImage(image)
    #Converts a Pillow Image object into a format that Tkinter's Label, Canvas, or Button can display

        # Create a Label to hold the image
    background_label = ttk.Label(win, image=photo)
    background_label.image = photo  # Keep a reference to prevent garbage collection
    background_label.place(x=0, y=0, relwidth=1, relheight=1) # Cover the entire window
    frame = ttk.Frame(win)
    frame.pack(pady=125)
    ttk.Label(frame, text="WITHDRAW MONEY", font="ariel 35 bold").grid(row=0, column=0, columnspan=2, pady=5)
    ttk.Label(frame, text="Enter Account number", font="ariel 12 bold").grid(row=1, column=0, pady=5, sticky="e")
    E1 = ttk.Entry(frame, width=35)
    E1.grid(row=1, column=1, pady=5)
    E1.insert(0, current_account)
    E1.config(state='readonly')
    ttk.Label(frame, text="Enter Amount", font="ariel 12 bold").grid(row=2, column=0, pady=5, sticky="e")
    E2 = ttk.Entry(frame, width=35)
    E2.grid(row=2, column=1, pady=5)
    ttk.Button(frame, text="ENTER", width=70, command=lambda: validate_and_withdraw(E1.get(), E2.get())).grid(row=3, column=0, columnspan=2, pady=5)
    ttk.Button(frame, text="BACK", width=70, command=MainWindow).grid(row=4, column=0, columnspan=2, pady=5)

    for widget in frame.winfo_children():
        widget.grid_configure(padx=10, pady=6)
    frame.tkraise()      

def clearWindow():
    for item in win.winfo_children():
        item.destroy()
    #this fuction clears the existing screen    

# Initialize window
win = Tk() #tkinter object created named "win". win is the name of our window
win.geometry("1920x1080") #size of window
win.title("BankApp")  # creates title of window



# Enhancement #1: Apply modern ttk theme
style = ttk.Style()
style.theme_use("clam")

# Enhancement #2: Set background color
win.configure(bg="#dce3ea")

style.configure("TFrame",
                background="#918DB4",
                relief="groove",
                borderwidth=2)
# relief="groove" ,Purpose: Adds a 3D-style border around the widget.

style.configure("TLabel", background="#97a2ba", font=("Segoe UI", 12))
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.map("TButton",
          foreground=[('active', "#20AA07")],
          background=[('active', "#0d4d95")])
#foreground	Changes text color on hover
#background	Changes button background color

style.configure("TEntry", padding=4)
#This sets internal padding for all Entry fields.

LoginWindow()  # calling of class
win.mainloop()  #makes the window open continously
