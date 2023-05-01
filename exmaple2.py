import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "Stargirl12@",
        database = "storing account data"
        
    )

if __name__ == '__main__':
    connection = connect_to_db()
    cursor = connection.cursor()


def create_account(name, number, cursor, connection):
    query = ("INSERT INTO account_info (name, number, balance) VALUES (%s, %s, %s)")
    values = (name, number, 0)
    cursor.execute(query, values)
    connection.commit()
    print("Account created successfully.")

def deposit(number, amount):
    cursor.execute("UPDATE account_info SET balance = balance + %s WHERE number = %s", (amount, number))
    connection.commit()
    print("Deposit successful.")

def check_balance(number):
    cursor.execute("SELECT balance FROM account_info WHERE number = %s", (number,))
    result = cursor.fetchone()
    if result is None:
        print("Account not found.")
    else:
        balance = result[0]
        print(f"Account balance: {balance}")
def withdrawal(number, amount):
    cursor.execute("SELECT balance FROM account_info WHERE number = %s", (number,))
    result = cursor.fetchone()
    if result is None:
        print("Account not found.")
    else:
        balance = result[0]
        if balance < amount:
            print("Insufficient balance.")
        else:
            cursor.execute("UPDATE account_info SET balance = balance - %s WHERE number = %s", (amount, number))
            connection.commit()
            print("Withdrawal successful.")

def modify(number, name, balance):
    cursor.execute("UPDATE account_info SET name = %s, balance = %s WHERE number = %s", (name, balance, number))
    connection.commit()
    print("Modification successful.")

def delete(number):
    cursor.execute("DELETE FROM account_info WHERE number = %s", (number,))
    connection.commit()
    print("Deletion successful.")
print(" Hello there!")
print("Welcome to peace 2  app!\n")
print(" Choose from these 6 choices")

while True:
    print("1. Create Account")
    print("2. Deposit")
    print("3. Check Balance")
    print("4. withdrawl")
    print("5. modify")
    print("6. delete")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter account name: ")
        number = int(input("Enter account number: "))
        create_account(name, number, cursor, connection)
        print("Account created successfully.\n")
    elif choice == "2":
        number = input("Enter your account number: ")
        amount = float(input("Enter amount to deposit: "))
        deposit(number, amount)
        print("Deposit successful.")
    elif choice == "3":
        number = input("Enter account number: ")
        check_balance(number)
    elif choice == "4":
        number = input("Enter your account number: ")
        amount = float(input("Enter amount to withdraw: "))
        withdrawal(number, amount)
    elif choice == "5":
        number = input("Enter your account number: ")
        name = input("Enter new account name: ")
        balance = float(input("Enter new account balance: "))
        modify(number, name, balance)
    elif choice == "6":
        number = input("Enter your account number: ")
        delete(number)

        