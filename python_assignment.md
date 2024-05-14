# Banking System - Control Structure

## Task 1: Conditional Statements
In a bank, you have been given the task is to create a program that checks if a customer is eligible for
a loan based on their credit score and income. The eligibility criteria are as follows:
• Credit Score must be above 700.
• Annual Income must be at least $50,000.<br>
Tasks:
1. Write a program that takes the customer's credit score and annual income as input.
2. Use conditional statements (if-else) to determine if the customer is eligible for a loan.
3. Display an appropriate message based on eligibility.

```python
credit_score = int(input("Please enter your credit score: "))
annual_income = int(input("Please enter your annual income: "))

if credit_score > 700 and annual_income > 50_000:
    print("Congrats you are eligible for loan!!😊")
else:
    print("We're sorry you are not eligible for the loan!!😥")
```
<hr>

## Task 2: Create a program that simulates an ATM transaction. 
Display options such as "Check Balance,"
"Withdraw," "Deposit,". Ask the user to enter their current balance and the amount they want to
withdraw or deposit. Implement checks to ensure that the withdrawal amount is not greater than the
available balance and that the withdrawal amount is in multiples of 100 or 500. Display appropriate
messages for success or failure.

```python
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
```
<hr>

## Task 3: : Loop Structures
You are responsible for calculating compound interest on savings accounts for bank customers. You
need to calculate the future balance for each customer's savings account after a certain number of years.
Tasks:
1. Create a program that calculates the future balance of a savings account.
2. Use a loop structure (e.g., for loop) to calculate the balance for multiple customers.
3. Prompt the user to enter the initial balance, annual interest rate, and the number of years.
4. Calculate the future balance using the formula:
future_balance = initial_balance * (1 + annual_interest_rate/100)^years.
5. Display the future balance for each customer.

```python
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
```

<hr>

## Task 4: Looping, Array and Data Validation
You are tasked with creating a program that allows bank customers to check their account balances.
The program should handle multiple customer accounts, and the customer should be able to enter their
account number, balance to check the balance.
Tasks:
1. Create a Python program that simulates a bank with multiple customer accounts.
2. Use a loop (e.g., while loop) to repeatedly ask the user for their account number and
balance until they enter a valid account number.
3. Validate the account number entered by the user.
4. If the account number is valid, display the account balance. If not, ask the user to try again.

```python
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
```
<hr>

## Task 5: Password Validation
Write a program that prompts the user to create a password for their bank account. Implement if<br>
conditions to validate the password according to these rules:<br>
• The password must be at least 8 characters long.<br>
• It must contain at least one uppercase letter.<br>
• It must contain at least one digit.<br>
• Display appropriate messages to indicate whether their password is valid or not.

```python
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
```

## Task 6: Password Validation
Create a program that maintains a list of bank transactions (deposits and withdrawals) for a customer.<br>
Use a while loop to allow the user to keep adding transactions until they choose to exit.<br>
Display the transaction history upon exit using looping statements.

```python
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
```

<hr>

## Task 7: Class & Object
1. Create a `Customer` class with the following confidential attributes:<br>

    • Attributes:<br>
    o Customer ID<br>
o First Name<br>
o Last Name<br>
o Email Address<br>
o Phone Number<br>
o Address<br>

    • Constructor and Methods:<br>
o Implement default constructors and overload the constructor with Customer
attributes, generate getter and setter, (print all information of attribute) methods for
the attributes.

2. Create an `Account` class with the following confidential attributes:<br>

    • Attributes:<br>
o Account Number<br>
o Account Type (e.g., Savings, Current)<br>
o Account Balance<br>

    • Constructor and Methods:<br>
o Implement default constructors and overload the constructor with Account
attributes,<br>
o Generate getter and setter, (print all information of attribute) methods for the
attributes.<br>
o Add methods to the Account class to allow deposits and withdrawals.<br>
- deposit(amount: float): Deposit the specified amount into the account.<br>
- withdraw(amount: float): Withdraw the specified amount from the account.<br>
withdraw amount only if there is sufficient fund else display insufficient
balance.<br>
- calculate_interest(): method for calculating interest amount for the available
balance. interest rate is fixed to 4.5%<br>

• Create a `Bank` class to represent the banking system. Perform the following operation in
main method:<br>
o create object for account class by calling parameter constructor.<br>
o deposit(amount: float): Deposit the specified amount into the account.<br>
o withdraw(amount: float): Withdraw the specified amount from the account.<br>
o calculate_interest(): Calculate and add interest to the account balance for savings
accounts.<br>

```python
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
```

<hr>

## Task 8:
