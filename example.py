import mysql.connector
import tkinter as tk

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Stargirl12@",
    database = "storing account data"
)
cursor = connection.cursor()
status_label = tk.Label(text="")
def user_home():
    def delete():
        number = account_number.get()
        cursor.execute("DELETE FROM account_info WHERE number = %s", (number,))
        connection.commit()
        tk.Label(home, text="Deletion successful.").grid(row=4, column=5)
        home.destroy()
        root.deiconify()
    def check_balance():
        number = number_entry.get()
        cursor.execute("SELECT balance FROM account_info WHERE number = %s", (number,))
        result = cursor.fetchone()
        if result is None:
            tk.Label(text="Account not found.").grid(row=13, column=3)
        else:
            balance = result[0]
            tk.Label(home, text=f"Account balance: {balance}").grid(row=14, column=3)
    def withdrawal():
        number = account_number_entry_w.get()
        amount = withdrawal_entry.get()
        cursor.execute("SELECT balance FROM account_info WHERE number = %s", (number,))
        result = cursor.fetchone()
        if result is None:
            tk.Label(home, text="Account not found.").grid(row=5, column=2)
        else:
            balance = result[0]
        if int(balance) < int(amount):
            tk.Label(home, text="Insufficient balance.").grid(row=7, column=2)
        else:
            cursor.execute("UPDATE account_info SET balance = balance - %s WHERE number = %s", (amount, number))
            connection.commit()
            tk.Label(home, text="Withdrawal successful.").grid(row=6, column=2)
    def deposit():
        number = account_number_entry.get()
        amount = deposit_entry.get()
        cursor.execute("UPDATE account_info SET balance = balance + %s WHERE number = %s", (amount, number))
        connection.commit()
        status_label.config(text="Deposit successful.")
    home = tk.Toplevel()
    home.geometry("1200x700")
    home.title("Bank Homepage")
    tk.Label(home, text="Enter amount to deposit").grid(row=0, column=1)
    deposit_entry = tk.Entry(home)
    deposit_entry.grid(row=1, column=1)
    tk.Label(home, text="Account Number").grid(row=2, column=1)
    account_number_entry = tk.Entry(home)
    account_number_entry.grid(row=3, column=1)
    tk.Button(home, text="DEPOSIT", command=deposit).grid(row=4, column=1)

    tk.Label(home, text="Enter amount to withdrawal").grid(row=0, column=3)
    withdrawal_entry = tk.Entry(home)
    withdrawal_entry.grid(row=1, column=3)
    tk.Label(home, text="Account Number").grid(row=2, column=3)
    account_number_entry_w = tk.Entry(home)
    account_number_entry_w.grid(row=3, column=3)
    tk.Button(home, text="WITHDRAWAL", command=withdrawal).grid(row=4, column=3)
    
    tk.Label(home, text="To check Balance input Account number").grid(row=10, column=3)
    number_entry = tk.Entry(home)
    number_entry.grid(row=11, column=3)
    tk.Button(home, text="Check Balance",command=check_balance).grid(row=12, column=3)
    
    tk.Label(home, text="delete Account").grid(row=0, column=4)
    account_number = tk.Entry(home)
    account_number.grid(row=1, column=5)
    tk.Button(home, text="Delete Account", command= delete).grid(row=2, column=5)

def create_account(name, number):
    query = ("INSERT INTO account_info (name, number, balance) VALUES (%s, %s, %s)")
    values = (name, number, 0)
    cursor.execute(query, values)
    connection.commit()
    status_label.config(text="Account created successfully.")
def login_window():
    login_page = tk.Toplevel()
    login_page.geometry("300x250")
    login_page.title("Login page")
    def login():
        name = name_entry.get()
        number = number_entry.get()
        query = ("SELECT * FROM account_info WHERE name = %s and number = %s")
        cursor.execute(query, (name,number))
        user = cursor.fetchone()
        if user is not None:
            tk.Label(login_page, text="Login Sucessfull").grid(row=6, column=6)
            root.withdraw()
            login_page.withdraw()
            user_home()
        else:
            tk.Label(login_page, text="IVALID USERSAME OR PASSWORD").grid(row=7, column=1)

    tk.Label(login_page, text= "Account name ").grid(row=0, column=1)
    name_entry = tk.Entry(login_page)
    name_entry.grid(row=1, column=1)
    tk.Label(login_page, text="Account number").grid(row=2, column=1)
    number_entry = tk.Entry(login_page)
    number_entry.grid(row=3, column=1)
    tk.Button(login_page, text="log in", command=login).grid(row=4, column=1)






def modify(number, name, balance):
    cursor.execute("UPDATE account_info SET name = %s, balance = %s WHERE number = %s", (name, balance, number))
    connection.commit()
    status_label.config(text="Modification successful.")


def handle_create_account():
    name = account_name_entry.get()
    number = int(account_number_entry.get())
    create_account(name, number)
    tk.Label(root, text= "account created successfully").grid(row= 5, column= 1)


def handle_modify():
    number = account_number_entry.get()
    name = account_name_entry.get()
    balance = float(amount_entry.get())
    modify(number, name, balance)

root = tk.Tk()
root.title("Peace 2 Banking App")
root.geometry("300x250")

account_name_label = tk.Label(root, text="Account Name")
account_name_label.grid(row=0, column=0)
# account_name_label.pack()

account_number_label = tk.Label(root, text="Account Number")
account_number_label.grid(row=1, column=0)
# account_number_label.pack()

# amount_label = tk.Label(root, text="Amount")
# amount_label.grid(row=2, column=0)
# amount_label.pack()

account_name_entry = tk.Entry(root)
account_name_entry.grid(row=0, column=1)
# account_name_entry.pack()

account_number_entry = tk.Entry(root)
account_number_entry.grid(row=1, column=1)
# account_number_entry.pack()
# amount_entry = tk.Entry(root)
# amount_entry.grid(row=2, column=1)
# amount_entry.pack()
tk.Button(root, text="Create Account", command=handle_create_account).grid(row=4, column=1)
tk.Label(root, text = " if you alaready have an account").grid(row= 7, column=1)
tk.Button(root, text="Login",command= login_window).grid(row=8, column=1)
# create_account_button.pack()
root.mainloop()