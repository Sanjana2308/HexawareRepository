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
        print(f"Your account balance is ₹{accounts[account_number]}")
        
check_account_balance()








 