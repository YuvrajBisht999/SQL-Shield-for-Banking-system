import sqlite3

from tkinter.messagebox import * #messagebox is a module of tkinter used for making message box(pop up window)

import hashlib # For SHA-256 hashing

GET_BALANCE_QUERY = "SELECT * FROM accmaster WHERE accno=?"
# "select query" is the sql query used for data retrival

UPDATE_BALANCE_QUERY = "UPDATE accmaster SET balance=balance+? WHERE accno=?"

SELECT_ACCOUNT_QUERY = "SELECT * FROM accmaster WHERE accno=? AND password=?"

ADMIN_ACCNO = "123"

ADMIN_HASH = hashlib.sha256("123".encode()).hexdigest()


def safe_execute(conn, query, params=(), fetch=False, fetchone=False):

    try:

        cur = conn.cursor()

        cur.execute(query, params)

        conn.commit()

        if fetch:

            return cur.fetchall()
        
        if fetchone:
            
            return cur.fetchone()
            # one row is retrived from database in the form of a tupple (0,Yuvraj Bisht,100)

        return True
    
    except sqlite3.IntegrityError as ie:

        showwarning("Integrity Error", str(ie))

    except sqlite3.OperationalError as oe:

        showerror("Operational Error", str(oe))

    except Exception as e:

        showerror("Database Error", str(e))
        
    return None

def create_table(conn): #conn is connection object

    try:

        cur = conn.cursor()

        #cursor of conn is created .cur is cusor object

        cur.execute('''
                    
            CREATE TABLE IF NOT EXISTS accmaster (
                    
                accno INTEGER PRIMARY KEY,
                    
                name TEXT,
                    
                balance INTEGER,
                    
                password TEXT
            )
                    
        ''')
        # will create a table named "accmaster" with 4 columns in the bracket
        # for comminting changes in database

        cur.execute('''
                    
            CREATE TABLE IF NOT EXISTS transactions (
                    
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                    
                accno INTEGER,
                    
                type TEXT,
                    
                amount INTEGER,
                    
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
                    
                FOREIGN KEY (accno) REFERENCES accmaster(accno)
                    
            )
                    
        ''')
        # DEFAULT CURRENT_TIMESTAMP automatically sets the value to the current date and time when a new row is inserted. 

        conn.commit()  # for comminting changes in database

    except Exception as e:

        showerror("Database Error", str(e))
        #Exception is the base class for most built-in exceptions in Python.
        #str(e) converts the exception object to a readable string.
        #showerror() pops up a GUI error dialog with a title and message.

def hash_password(password):

    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()   

def is_valid_account_number(accno):

    try:

        int(accno)

        return True
    
    except ValueError:

        return False      
    
def is_valid_amount(amount):

    try:

        amt = int(amount)

        return amt > 0
    
    except ValueError:
        
        return False    

def openAccount_db(conn,accno,name,balance, password):

    try:

        accno = int(accno)   #conversion to integer

        balance = int(balance)

        if balance < 0:

            raise ValueError("Balance cannot  be negative.")

        if not name.strip():

            raise ValueError("Name cannot be empty")
        
        if not password.strip():

            raise ValueError("Password cannot be empty")
        
        hashed_password = hash_password(password)

        query="insert into accmaster values(?,?,?,?)"    # the ?s are placeholders

        success = safe_execute(conn, query, [accno, name, balance, hashed_password])

        if success:

            showinfo("Bank", "Account created successfully") # showinfo(title,message)
            #pop up of showinfo box

    except ValueError:

        showwarning("Bank", "Please enter valid numeric values and a non-empty name.")
        #Catches ValueError, typically raised when:
        #Converting non-numeric input using int() or float()
        #Invalid operations on certain data types
        #Shows a warning dialog to alert the user that their input was invalid

def CheckBalance_db(conn, accno):

    if not is_valid_account_number(accno):

        showwarning("Bank", "Invalid account number format.")

        return

    row = safe_execute(conn, GET_BALANCE_QUERY, [int(accno)], fetchone=True)

    if row:

        showinfo("Bank", f"Accno: {row[0]}\nName:{row[1]}\nBalance:{row[2]}")

    else:

        showwarning("Bank", "Account Not Found") # a warning box will pop up
    
def deposit_db(conn, accno, amount):

    if not is_valid_account_number(accno) or not is_valid_amount(amount):

        showwarning("Bank", "Invalid account number or amount.")

        return

    accno = int(accno)

    amount = int(amount)

    success = safe_execute(conn, UPDATE_BALANCE_QUERY, [amount, accno])

    if success:

        safe_execute(conn, "INSERT INTO transactions (accno, type, amount) VALUES (?, 'deposit', ?)", [accno, amount])

        showinfo("Bank", "Amount deposited successfully")

    else:

        showwarning("Bank", "Account Not Found")        

def withdraw_db(conn, accno, amount):

    if not is_valid_account_number(accno) or not is_valid_amount(amount):

        showwarning("Bank", "Invalid account number or amount.")

        return

    accno = int(accno)

    amount = int(amount)

    row = safe_execute(conn, GET_BALANCE_QUERY, [accno], fetchone=True)

    if not row:

        showwarning("Bank", "Account Not Found")

        return

    balance = row[2]

    if balance >= amount:

        success = safe_execute(conn, "UPDATE accmaster SET balance=balance-? WHERE accno=?", [amount, accno])

        if success:

            safe_execute(conn, "INSERT INTO transactions (accno, type, amount) VALUES (?, 'withdraw', ?)", [accno, amount])

            showinfo("Bank", "Amount Withdrawn successfully")

    else:

        showwarning("Bank", "Insufficient Balance")    

def validate_login_db(conn, accno, password):

    try:

        if accno == ADMIN_ACCNO and hash_password(password) == ADMIN_HASH:

            return "admin"

        accno = int(accno)

        hashed_password = hash_password(password)

        row = safe_execute(conn, SELECT_ACCOUNT_QUERY, [accno, hashed_password], fetchone=True)

        if row:

            return "user"
        
        return None

    except ValueError:

        showwarning("Login Error", "Please enter a valid account number.")

        return None          
    
def get_all_transactions(conn):

    return safe_execute(conn, "SELECT * FROM transactions ORDER BY timestamp DESC", fetch=True) or []
    # The ORDER BY timestamp DESC clause sorts them in reverse chronological order — newest transactions come first.
    # ORDER BY timestamp: Sort the results based on the timestamp column.
    # DESC: Sort in descending order — i.e., latest first.

def get_all_accounts(conn):

    return safe_execute(conn, "SELECT accno, name, balance FROM accmaster", fetch=True) or []
