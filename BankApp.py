from tkinter import *    #importing gui library

from tkinter.messagebox import *

import sqlite3  

import database #will import database.py

conn=sqlite3.Connection("mydatabase.db")
#it will create a dtabase name "mydatabase.db" inside our folder
#conn is connection object

database.create_table(conn)

def MainWindow():

    clearWindow()

    L1=Label(win,text="Welcome to Bank",font="ariel 20 bold")  
    # L1 is obect of class label. label takes name of window ("win") and text to display as input and its font
    #label is for showing text on window

    L1.pack(pady=5)    #makes the label to show on window(attaches the label to win),pady for some space between boxes of text vertically

    B1=Button(win,text="Open Account",width=20,command=OpenAccountWindow)    #same as label above , width makes the button wide
    #button is for creating button on window
    #command will do what will happen after clicking the button

    B1.pack(pady=5)    #same as label above

    B2=Button(win,text="Check Balance",width=20,command=CheckBalanceWindow)    

    B2.pack(pady=5)    

    B3=Button(win,text="Deposit Amount",width=20,command=DepositWindow)   

    B3.pack(pady=5)     

    B4=Button(win,text="Withdraw Amount",width=20,command=WithdrawWindow)   

    B4.pack(pady=5)     

    B5=Button(win,text="Exit",width=20,command=win.destroy)    

    B5.pack(pady=5)  

def validate_and_create_account(accno, name, balance):

    if not accno or not name or not balance:

        showwarning("Input Error", "All fields are required.")

        return
    
    database.openAccount_db(conn, accno, name, balance)      

def OpenAccountWindow():

    clearWindow()  #will clear the previous screen

    L1=Label(win,text="Open Account",font="ariel 20 bold")  
    
    L1.pack(pady=5)   

    L2=Label(win,text="Enter Account")  
   
    L2.pack(pady=5)    

    E1=Entry(win,width=20)   #uses entry field to take input from user

    E1.pack()   

    L3=Label(win,text="Enter Name",)  
   
    L3.pack(pady=5)    

    E2=Entry(win,width=20)   

    E2.pack() 

    L4=Label(win,text="Enter Balance",)  
   
    L4.pack(pady=5)    

    E3=Entry(win,width=20)   

    E3.pack()  

    B1=Button(win,text="Create",width=20,command=lambda:validate_and_create_account(E1.get(),E2.get(),E3.get()))    

    B1.pack(pady=5) 

    B2=Button(win,text="Back",width=20,command=MainWindow)    

    B2.pack(pady=5)

def validate_and_check_balance(accno):

    if not accno:

        showwarning("Input Error", "Account number is required.")

        return
    
    database.CheckBalance_db(conn, accno)     

def CheckBalanceWindow():

    clearWindow()  

    L1=Label(win,text="Check Balance",font="ariel 20 bold")  
    
    L1.pack(pady=5)   

    L2=Label(win,text="Enter Account number")  
   
    L2.pack(pady=5)    

    E1=Entry(win,width=20)   

    E1.pack()     

    B1=Button(win,text="Check",width=20,command=lambda:validate_and_check_balance(E1.get()))    

    B1.pack(pady=5) 

    B2=Button(win,text="Back",width=20,command=MainWindow)    

    B2.pack(pady=5)

def validate_and_deposit(accno, amount):

    if not accno or not amount:

        showwarning("Input Error", "Both fields are required.")

        return
    
    database.deposit_db(conn, accno, amount)    

def DepositWindow():
    
    clearWindow()  

    L1=Label(win,text="Deposit Amount",font="ariel 20 bold")  
    
    L1.pack(pady=5)   

    L2=Label(win,text="Enter Account number")  
   
    L2.pack(pady=5)    

    E1=Entry(win,width=20)   

    E1.pack()  

    L3=Label(win,text="Enter Amount")  
   
    L3.pack(pady=5)    

    E2=Entry(win,width=20)   

    E2.pack()   

    B1=Button(win,text="deposit",width=20,command=lambda:validate_and_deposit(E1.get(),E2.get()))    

    B1.pack(pady=5) 

    B2=Button(win,text="Back",width=20,command=MainWindow)    

    B2.pack(pady=5)

def validate_and_withdraw(accno, amount):

    if not accno or not amount:

        showwarning("Input Error", "Both fields are required.")

        return
    
    database.withdraw_db(conn, accno, amount)    

def WithdrawWindow():
    
    clearWindow()  

    L1=Label(win,text="Withdraw Amount",font="ariel 20 bold")  
    
    L1.pack(pady=5)   

    L2=Label(win,text="Enter Account number")  
   
    L2.pack(pady=5)    

    E1=Entry(win,width=20)   

    E1.pack()  

    L3=Label(win,text="Enter Amount")  
   
    L3.pack(pady=5)    

    E2=Entry(win,width=20)   

    E2.pack()   

    B1=Button(win,text="withdraw",width=20,command=lambda:validate_and_withdraw(E1.get(),E2.get()))    

    B1.pack(pady=5) 

    B2=Button(win,text="Back",width=20,command=MainWindow)    

    B2.pack(pady=5)            

def clearWindow():
    for item in win.winfo_children():
        item.destroy()
    #this fuction clears the existing screen    




    

win=Tk()    #tkinter object created named "win". win is the name of our window

win.geometry("300x400")   #size of window

win.title("BankApp")     # creates title of window

MainWindow() # calling of class

win.mainloop()   #makes the window open continously


