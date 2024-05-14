# Task 1: 
credit_score = int(input("Please enter your credit score: "))
annual_income = int(input("Please enter your annual income: "))

if credit_score > 700 and annual_income > 50_000:
    print("Congrats you are eligible for loan!!😊")
else:
    print("We're sorry you are not eligible for the loan!!😥")

# Task 2:
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



 