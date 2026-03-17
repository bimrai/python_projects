def investment_simulator():
    
    # will use later for expenditure feature
    # expenditure = []
    
    # account class
    class Account:
        def __init__(self, user, balance, user_portfolio):
            self.user = user
            self.balance = balance
            self.user_portfolio = user_portfolio

        def deposit(self): 
            amount = int(input("Deposit \n Enter Deposit Amount: £"))
            self.balance += amount
            print("____________________________________________")
            print(f"You have successfully deposited £{amount:,.2f} \nUpdated Balance: £{self.balance:,.2f}")
        
        def check_balance(self):
            print("____________________________________________")
            print(f"Balance \n Current Balance: £{self.balance:,.2f}")
            
        def withdraw(self):
            while True:
                print("____________________________________________")
                withdraw = int(input("Withdraw \n Enter Withdrawal Amount: £"))
                
                if withdraw <= self.balance:
                    self.balance = self.balance - withdraw
                    print(f"You have successfully withdrawn £{withdraw:,.2f} \n Updated Balance: £{self.balance:,.2f}")
                    break
                elif withdraw > self.balance:
                    print("Insufficent Funds")
                    continue
    
    # class object created           
    account = Account("BIM117", 0, {})
    
    while True:
        
        # menu
        print("____________________________________________")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Stock Market")
        print("5. Portfolio")
        print("0. Logout")
        print("____________________________________________")
        # user option input for menu 
        option = int(input("Please choose an option: "))
        
        # deposit
        if option == 1:
            account.deposit()
           
        #withdrawal 
        if option == 2:
            account.withdraw()
          
        # check current balance  
        if option == 3:
            account.check_balance()
            
        # stock market   
        if option == 4:
            print("Stock Market:")
            print("1. Apple")
            print("2. NVIDIA")
            print("3. Tesla")
            print("4. Meta")
            print("5. Amazon")
            print("0. Back")
            print("____________________________________________")
            option = int(input("Please choose an option: "))
            
            # apple stock purchase
            if option == 1:
                apple_stock = 189.83
                print("____________________________________________")
                print(f"Selected Apple Stock: \n Apple Stock Current Price: £{apple_stock:,.2f} | Current Balance: £{account.balance:,.2f}")
                
                while True:
                    amount = int(input("Apple Stock - Enter Purchase Amount: £"))
                    
                    apple_shares = amount / apple_stock
                    
                    # buying power check + confirm purchase
                    if account.balance >= amount and account.balance > apple_stock:
                        print(f"Please confirm your purchase:")
                        print(f"Apple Stock Purchase: £{amount:,.2f} \n Shares: {apple_shares:,.4f}")
                        print("1. Confirm")
                        print("0. Cancel")
                        confirm = int(input("Please Enter: "))
                        
                        # purchase overview
                        if confirm == 1:
                            print(f"Transaction Complete! \n You have Succesfully Purchased {apple_shares:,.4f} Shares of Apple Stock worth about £{amount:,.2f}.")
                            account.balance -= amount
                            print(f"Updated Balance: £{account.balance:,.2f}")
                            break
                        else:
                            break
                    # option to add more balance or return to main menu if not
                    elif account.balance < amount:
                        print(f"Insufficient Funds: £{account.balance:,.2f}.")
                        print("Would you like to add funds?")
                        print("1. Yes")
                        print("0. No")
                        pick = int(input("Enter 1 or 0: "))
                        
                        if pick == 1:
                            account.deposit = int(input("Enter Deposit Amount: £"))
                            account.balance = account.balance + account.deposit
                            print(f"Updated Balance: £{account.balance:,.2f}") 
                            print("____________________________________________")
                        else:
                            break
            
            # stocks
            if option == 2:
                print("will add later")
            if option == 2:
                print("will add later")
            if option == 2:
                print("will add later")
            if option == 2:
                print("will add later")
        
        # exit 
        if option == 0:
            print("You have successfully logged out! Have a nice day!")
            break
                    


                              
investment_simulator() # run python main.py
