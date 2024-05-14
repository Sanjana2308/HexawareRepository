# Task 1:
def check_for_loan():
    credit_score = int(input("Please enter your credit score: "))
    annual_income = int(input("Please enter your annual income: "))

    if credit_score > 700 and annual_income > 50_000:
        print("Congrats you are eligible for loan!!😊")
    else:
        print("We're sorry you are not eligible for the loan!!😥")

check_for_loan()


#Task 2:
def perform_transactions():
    current_balance = int(input("Enter your current balance: "))

    while True:

        choice = int(input("""
Please Enter your choice:
    1. Check balance
    2. Withdraw
    3. Deposit
    4. Exit
"""))
    
        if choice == 1:
            print(f"Your current balance is ₹{current_balance} 😊")

        elif choice == 2:
            withdrawal_amount = int(input(("Enter the amount to be withdrawn: ")))
            if withdrawal_amount < current_balance:
                current_balance -= withdrawal_amount
                print("Amount withdrawn successfully!!🥳")
                print(f"Your updated balance is ₹{current_balance}")
            else:
                print(f"""Insufficient balance in your account!!😥 
Your current balance is ₹{current_balance}.""")

        if choice == 3:
            deposit_amount = int(input("Enter the amount to be deposited (in multiples of 100 or 500): "))
            if deposit_amount % 100 == 0 or deposit_amount % 500 == 0:
                current_balance += deposit_amount
                print("Amount deposited successfully!!🥳")
                print(f"Your updated balance is ₹{current_balance}")
            else:
                print("WARNING!⚠️  Enter deposit amount in multiples of 100 or 500 only.")

        elif choice == 4:
            break

perform_transactions()


#Task 3:
def calculate_compound_interest():
    num_customers = int(input("Enter the number of customers: "))
    for number in range(1, num_customers+1):
        name = input("Enter your name: ")
        print(f"Enter data for {name}")
        initial_balance = int(input("Enter initial balance: "))
        annual_interest_rate = int(input("Enter annual interest rate: "))
        years = int(input("Enter the number of years: "))
        future_balance = round(initial_balance*(1 + annual_interest_rate/100)**years)
        print(f"""{name} 😊, your balance after applying compound interest for {years} years is 
₹{future_balance}""")

calculate_compound_interest()


# Task 4:
def check_account_balance():
    accounts = {}
    num_customers = int(input("Enter the number of customers: "))

    for number in range(1, num_customers + 1):
        print(f"Enter details for Customer {number} 🙂")
        account_number = int(input("Enter your account number: "))
        # Checking if customer has already entered account number or not
        if account_number not in accounts:
            balance = int(input("Enter your balance: "))
            accounts[account_number] = balance
        while True:
            account_number = int(input("Enter your account number for validation: "))
            if account_number in accounts:
                break
            else:
                print("Warning! ⚠️  Wrong credentials! Try again 🙂")
        print(f"Your account balance is ₹{accounts[account_number]} 😎")
        
check_account_balance()
 

# Task 5:
def validate_password():
    print("Its time to make your account more secure!😊")
    print("Lets create a password for your account")
    while True:
        password = input("Enter password: ")
        if len(password) < 8:
            print("Invalid Password! Must have at least 8 characters long! ⚠️")
        elif not any (character.isupper() for character in password):
            print("Invalid Password! Must have at least one uppercase letter! ⚠️")
        elif not any (character.isdigit() for character in password):
            print("Invalid Password! Must have at least one digit! ⚠️")
        else:
            print("Yay, your password is valid!🥳")
            break

validate_password()


# Task 6:
def track_transactions():
    # We will create a list of Dictionaries
    transactions = []
    while True:
        
        choice = int(input("""Enter your choice:
1. Deposit
2. Withdraw
3. Exit
"""))
        if choice == 1:
            deposit_amount = int(input("Enter deposit amount: "))
            transactions.append({'Transaction Type': 'Deposit', 'Amount': deposit_amount})

        elif choice == 2:
            withdrawal_amount = int(input("Enter withdrawal amount: "))
            transactions.append({'Transaction Type': 'Withdraw', 'Amount': withdrawal_amount})

        elif choice == 3:
            break

    print(transactions)

track_transactions()

# Task 7:
class Customer:
    def __init__(self, customer_id, first_name, last_name, email_address, phone_number, address):
        self.__customer_id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email_address = email_address
        self.__phone_number = phone_number
        self.__address = address
    
    # Getter methods
    def get_customer_id(self):
        return self.__customer_id
    
    def get_first_name(self):
        return self.__first_name
    
    def get_last_name(self):
        return self.__last_name
    
    def get_email_address(self):
        return self.__email_address
    
    def get_phone_number(self):
        return self.__phone_number
    
    def get_address(self):
        return self.__address
    
    # Setter Methods
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_email_address(self, email_address):
        self.__email_address = email_address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_address(self, address):
        self.__address = address

    def print_all_information(self):
        print(f"Customer ID: {self.__customer_id}")
        print(f"First Name: {self.__first_name}")
        print(f"Last Name: {self.__last_name}")
        print(f"Email Address: {self.__email_address}")
        print(f"Phone Number: {self.__phone_number}")
        print(f"Address: {self.__address}")

class Account:
    def __init__(self, acc_number, acc_type, acc_balance):
        self.__acc_number = acc_number
        self.__acc_type = acc_type
        self.__acc_balance = acc_balance

    # Getter Methods
    def get_acc_number(self):
        return self.__acc_number
    
    def get_acc_type(self):
        return self.__acc_type
    
    def get_acc_balance(self): 
        return self.__acc_balance

    # Setter Methods
    def set_acc_number(self, acc_number):
        self.__acc_number = acc_number

    def set_acc_type(self, acc_type):
        self.get_acc_type = acc_type

    def set_acc_balance(self, acc_balance):
        self.__acc_balance = acc_balance

    def print_all_information(self):
        print(f"Account Number: {self.__acc_number}")
        print(f"Account Type: {self.__acc_type}")
        print(f"Account Balance: ₹{self.__acc_balance}")

    def deposit(self, amount):
        self.__acc_balance += amount
        print(f"Deposit of ₹{amount} was successful!🥳")
        print(f"Updated Balance: ₹{self.__acc_balance}")

    def withdraw(self, amount):
        if amount > self.__acc_balance:
            print("Insufficient balance!😥")
        else:
            self.__acc_balance -= amount
            print(f"Withdrawal of ₹{amount} was successful!🥳")
            print(f"Updated Balance: ₹{self.__acc_balance}")

    def cal_interest(self):
        if self.__acc_type.lower() == 'savings':
            interest = self.__acc_balance * 0.45
            self.__acc_balance += interest
            print("Interest Calculated Successfully!🥳")
            print(f"Interest = {interest}")
            print(f"Updated Balance: ₹{self.__acc_balance}")
        else:
            print("Interest calculation is only applicable for savings accounts.")
    
class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def create_customer(self, customer_id, first_name, last_name, email_address, phone_number, address):
        customer = Customer(customer_id, first_name, last_name, email_address, phone_number, address)
        self.customers.append(customer)
        return customer

    def create_account(self, acc_number, acc_type, acc_balance):
        account = Account(acc_number, acc_type, acc_balance)
        self.accounts.append(account)
        return account
    
    def perform_operations(self):
        account = self.create_account(1234, "Savings", 50000)
        account.print_all_information()
        account.deposit(500)
        account.withdraw(600)
        account.cal_interest()

if __name__ == "__main__":
    bank = Bank()
    bank.perform_operations()

# Task 8:







 