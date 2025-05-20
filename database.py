import sqlite3

from tkinter.messagebox import * #messagebox is a module of tkinter used for making message box(pop up window)

def create_table(conn):  #conn is connection object

    query="create table if not exists accmaster(accno int,name text,balance int)"
    #will create a table named "accmaster" with 3 columns in the bracket 

    cur=conn.cursor()
    #cursor of conn is created .cur is cusor object

    cur.execute(query)  #execution of query

    conn.commit()  # for comminting changes in datatabase

def openAccount_db(conn,accno,name,balance):

    accno=int(accno)   #conversion to integer

    balance=int(balance)

    query="insert into accmaster values(?,?,?)"    # the ?s are placeholders

    cur=conn.cursor()

    cur.execute(query,[accno,name,balance]) #insert query ke placeholders mein pass hojayega 3 datas

    conn.commit()

    if cur.rowcount>0:

        showinfo("Bank","Account created successfully")   #showinfo(title,message)   
        #pop up of showinfo box

def CheckBalance_db(conn,accno):

    accno=int(accno)

    query="select * from accmaster where accno=?"
    # "select query" is the sql query used for data retrival

    cur=conn.cursor()

    cur.execute(query,[accno]) 

    row=cur.fetchone() # one row is retrived from database in the form of a tupple (0,Yuvraj Bisht,100)

    if row==None:

        showwarning("Bank","Account Not Found") # a warning box will pop up

    else:

        showinfo("Bank",f"Accno: {row[0]}\nName:{row[1]}\nBalance:{row[2]}")

def deposit_db(conn,accno,amount):
    accno=int(accno)  

    amount=int(amount)

    query="update accmaster set balance=balance+? where accno=?"

    cur=conn.cursor()

    cur.execute(query,[amount,accno]) 

    conn.commit()

    if cur.rowcount>0:

        showinfo("Bank","Amount deposited successfully")

    else:

        showwarning("Bank","Account Not Found") 

def withdraw_db(conn,accno,amount):
    accno=int(accno)  

    amount=int(amount)



    query="select * from accmaster where accno=?"

    cur=conn.cursor()

    cur.execute(query,[accno]) 

    row=cur.fetchone()

    if row==None:

        showwarning("Bank","Account Not Found")

    else:
        balance=row[2]

        if balance>=amount:

            query2="update accmaster set balance=balance-? where accno=?"   #update querry

            cur2=conn.cursor()  # fro 2 operation new cursor is required

            cur2.execute(query2,[amount,accno])

            conn.commit()

            if cur2.rowcount>0:
                
                showinfo("Bank","Amount Withdraw successfully")

        else:

            showwarning("Bank","Insufficient Balance")





         
