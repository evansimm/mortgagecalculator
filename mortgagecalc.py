# imports the Loan class from mortgage module
# https://pypi.org/project/mortgage/

from mortgage import Loan

principal = float(input("Enter the loan principal amount: "))
interest = float(input("Enter the interest rate (as a whole number or decimal): "))
term = int(input("Enter the loan term in years: "))

#if user enters number number for interest as a whole number, convert to decimal
if interest > 1:
    interest = interest / 100

# loan = Loan(principal=100000, interest=.05, term=30)
loan = Loan(principal, interest, term)

#Prompt user to select an option. 1. Monthly payment 2. Total interest 3. Summarize
while True:  # Start an infinite loop to keep asking for input until valid
    option = input("Enter 1 for monthly payment, 2 for total interest, or 3 for a summary: ")
    
    if option == "1":
        # Display the monthly payment
        print(f"The monthly payment is: {loan.monthly_payment:.2f}")
        break  # Exit the loop after valid input and action
    elif option == "2":
        # Display the total interest
        print(f"The total interest is: {loan.total_interest:.2f}")
        break  # Exit the loop after valid input and action
    elif option == "3":
        # Assuming summarize is a method, it should be called as a function
        print(loan.summarize)
        break  # Exit the loop after valid input and action
    else:
        # If user enters an invalid option, inform them and continue the loop
        print("Invalid option. Please enter 1, 2, or 3.")