# ATM Simulation Mini Project

# Here is a simple beginner-friendly ATM simulation project with
# PIN verification, balance inquiry, deposit, withdrawal, and exit.

# ATM Simulation - Python Mini Project
# Python concepts used:

# while loops
# if-elif-else
# Variables
# input() and print()
# Exception handling with try-except
# Arithmetic operations
# String formatting

balance = 10000
correct_pin = "1234"

print("===========================")
print("       WELCOME TO ATM")
print("===========================")

# PIN Verification
attempts = 3

while attempts > 0:
    pin = input("Enter your 4-digit PIN: ")

    if pin == correct_pin:
        print("\n Login successfully")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining: ", attempts)


if attempts == 0:
    print("Your card has been blocked.")
else:
    while True:
        print("\n======== ATM MENU ============")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("==================================")

        choice = input("Enter your Choice: ")

        if choice == 1:
            print(f"Your Current balance is ${balance:.2f}")

        elif choice == 2:
            try:
                amount = float(input("Enter deposit amount: $"))

                if amount <= 0:
                    print("Amount must be greater than 0.")
                else:
                    balance += amount
                    print(f"${amount:.2f} deposit successfully.")
                    print(f"New Balance: ${balance:.2f}")

            except ValueError:
                print("Please enter a valid number.")

        elif choice == 3:
            try:
                amount = float(input("Enter Withdrawal amount: $"))

                if amount <= 0:
                    print("Please Enter a valid amount.")
                else:
                    balance -= amount
                    print(f"Please collect your cash: ${amount:.2f}")
                    print(f"Remaining Balance: ${balance:.2f}")

            except ValueError:
                print("Please enter valid number.")

        elif choice == 4:
            print"\nThank You for using or ATM!")
            print("Please Collect Your Card.")
            break
        else:
            print("Invalid choice. Please select 1-4.")
