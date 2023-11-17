# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account
# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.s
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    savings_balance = float(input("Please enter/set your savings balance: "))
    savings_interest = float(input("Please enter/set your savings interest rate: "))
    savings_months = int(input("Please enter/set how many months for your savings account: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings = create_savings_account(savings_balance, savings_interest, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Details about your updated savings account for {savings_months} months: Your Interest Earned: {updated_savings[1]}, Your Updated Balance: {updated_savings[0]}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    # Setting the CD balance, then interest_rate, then the number of months 
    cd_balance = float(input("Please enter the CD account balance: "))
    cd_interest_rate = float(input("Please enter the interest rate for your CD account:"))
    cd_months = int(input("Please enter the number of months for the CD acount: "))
   


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print(f"Details about your updated CD account for {cd_months} months: Your Interest Earned: {updated_cd[1]}, Your Updated Balance: {updated_cd[0]}")

if __name__ == "__main__":
    # Call the main function.
    main()
    
