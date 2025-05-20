import sqlite3

from tkinter.messagebox import * #messagebox is a module of tkinter used for making message box(pop up window)

def create_table(conn):  #conn is connection object

    query = "CREATE TABLE IF NOT EXISTS accmaster (accno INTEGER PRIMARY KEY, name TEXT, balance INTEGER)"
    #will create a table named "accmaster" with 3 columns in the bracket 

    try:

        cur=conn.cursor()
        #cursor of conn is created .cur is cusor object

        cur.execute(query)  #execution of query

        conn.commit()  # for comminting changes in datatabase

    except Exception as e:

        showerror("Database Error", str(e))
        #Exception is the base class for most built-in exceptions in Python.
        #str(e) converts the exception object to a readable string.
        #showerror() pops up a GUI error dialog with a title and message.

def openAccount_db(conn,accno,name,balance):

    try:

        accno = int(accno)   #conversion to integer

        balance = int(balance)

        if balance < 0:

            raise ValueError("Balance cannot  be negative.")

        if not name.strip():
            raise ValueError("Name cannot be empty")

        query="insert into accmaster values(?,?,?)"    # the ?s are placeholders

        cur=conn.cursor()

        cur.execute(query,[accno,name,balance]) #insert query ke placeholders mein pass hojayega 3 datas

        conn.commit()

        if cur.rowcount>0:

              showinfo("Bank","Account created successfully")   #showinfo(title,message)   
              #pop up of showinfo box

    except ValueError:

        showwarning("Bank", "Please enter valid numeric values and a non-empty name.")
        #Catches ValueError, typically raised when:
        #Converting non-numeric input using int() or float()
        #Invalid operations on certain data types
        #Shows a warning dialog to alert the user that their input was invalid



    except sqlite3.IntegrityError:

        showwarning("Bank", "Account number already exists.")

    except Exception as e:

        showerror("Database Error", str(e))
  

def CheckBalance_db(conn,accno):

    try:

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
    
    except ValueError:

        showwarning("Bank", "Please enter a valid account number.")

    except Exception as e:

        showerror("Database Error", str(e))
    
def deposit_db(conn,accno,amount):
    try:
        accno=int(accno)  

        amount=int(amount)

        if amount <= 0:

            raise ValueError("Amount must be positive.")

        query="update accmaster set balance=balance+? where accno=?"

        cur=conn.cursor()

        cur.execute(query,[amount,accno]) 

        conn.commit()

        if cur.rowcount>0:

            showinfo("Bank","Amount deposited successfully")

        else:

            showwarning("Bank","Account Not Found") 

    except ValueError:

        showwarning("Bank", "Please enter valid numeric values.")

    except Exception as e:

        showerror("Database Error", str(e))        

def withdraw_db(conn,accno,amount):

    try:

        accno=int(accno)  

        amount=int(amount)

        if amount <= 0:
            
            raise ValueError("Amount must be positive.")

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

                    cur2=conn.cursor()  # for 2 operation new cursor is required

                    cur2.execute(query2,[amount,accno])

                    conn.commit()

                    if cur2.rowcount>0:
                
                          showinfo("Bank","Amount Withdraw successfully")

               else:

                         showwarning("Bank","Insufficient Balance")

    except ValueError:

        showwarning("Bank", "Please enter valid numeric values.")

    except Exception as e:

        showerror("Database Error", str(e))    