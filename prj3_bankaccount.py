import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="",
    database="sense7ai"
)

accountdetails = []

class BankAccount:
    def __init__(self, holder, amount):
        self.holder = holder
        self.amount = amount
        accountdetails.append(self)
        print(f"The account holder {self.holder} has {self.amount}")

    def createaccount(self):
        accountdetails.append(self.holder, self.amount)
        print(f"{self.holder} created an account with the amount {self.amount}")

    def deposit(self, damount):
        self.amount += damount
        accountdetails.append(self.amount)
        print(f"The amount is deposited to the account")
        print(f"The amount is {self.amount} to {self.holder}")
        print("-" * 50)

    def withdraw(self, withdrawamount):
        if self.amount > withdrawamount:
            self.amount -= withdrawamount
            accountdetails.append(self.amount)
            print(f"The balance amount of the holder {self.holder} is {self.amount}")
            print("-" * 50)
        else:
            print("Not sufficient money")
            print("-" * 50)

def print_menu():
    print("=" * 50)
    print(" " * 16 + "Bank Account Menu" + " " * 16)
    print("=" * 50)
    print("1. Create new account")
    print("2. Withdraw Amount")
    print("3. Deposit Amount")
    print("4. Store the data in file and Database")
    print("5. Transfer Amount")
    print("6. Exit")
    print("=" * 50)

print("The Bank Account")
print("=" * 50)
ramu = BankAccount('ramu', 5000)
paru = BankAccount('paru', 10000)

while True:
    print_menu()
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input("Enter the name: ")
        amount = int(input("Enter the amount: "))
        name = BankAccount(name, amount)
        print("-" * 50)
        
    elif choice == 2:
        name = input("Enter your name: ")
        withdrawamount = int(input("Enter withdraw amount: "))
        present = False
        for i in accountdetails:
            if i.holder.lower() == name.lower():
                i.withdraw(withdrawamount)
                present = True
                break
        if not present:
            print("He/she does not have an account")
            print("-" * 50)
                
    elif choice == 3:
        name = input("Enter your name: ")
        damount = int(input("Enter amount to deposit: "))
        present = False
        for i in accountdetails:
            if i.holder.lower() == name.lower():
                i.deposit(damount)
                present = True
                break
        if not present:
            print("He/she does not have an account")
            print("-" * 50)

    elif choice == 4:
        print("=" * 50)
        print(" " * 16 + "Account Details" + " " * 16)
        print("=" * 50)
        for i in accountdetails:
            
            mysqlcursor = con.cursor()
            mysqlcursor.execute("""insert into BankAccount(name,Balance)values(%s,%s)""", (i.holder, i.amount))
            con.commit()

        with open("Bankfile.txt", "w") as file:
            for i in accountdetails:
                file.write(f"Holder: {i.holder}, Amount: {i.amount}\n")
        print("-" * 50)
   
    elif choice == 5:
        name = input("Enter your name: ")
        toname = input("Enter the receiver's name: ")
        tamount = int(input("Enter the amount to be transferred: "))
        
        from_account = next((i for i in accountdetails if i.holder.lower() == name.lower()), None)
        to_account = next((i for i in accountdetails if i.holder.lower() == toname.lower()), None)

        if from_account and to_account:
            if from_account.amount >= tamount:
                from_account.withdraw(tamount)
                to_account.deposit(tamount)
                print(f"Transferred {tamount} from {name} to {toname}")
                print("-" * 50)
            else:
                print("Not sufficient money for the transfer")
                print("-" * 50)
        else:
            print("Accounts not found")
            print("-" * 50)
    
    elif choice == 6:
        break

