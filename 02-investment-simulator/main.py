# list object not callable, so i gotta change it from list call to create maybe list/dict to record logs like stock on portfolio. 

def investment_simulator():
    
    # account class
    class Account:
        def __init__(self, user, balance, stocks, total_invested, transaction_log):
            self.user = user
            self.balance = balance
            self.stocks = stocks
            self.total_invested = total_invested
            self.transaction_log = transaction_log
        
        def deposit(self): 
            amount = int(input("Deposit \n Enter Deposit Amount: £"))
            self.balance += amount
            # self.transaction_log = amount
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
                   
        def portfolio(self): 
                print("____________________________________________")
                print("Portfolio")
                print(f"Balance: £{self.balance:,.2f}")
                print(f"Total Invested: £{self.total_invested:,.2f}")
                for stock in self.stocks:
                    stock.show_stock()
                    
        def transaction_log(self):
            print("____________________________________________")
            print("Transaction History")
            print(print(f"Balance: £{self.balance:,.2f}"))
            print(f"Total Invested: £{self.total_invested:,.2f}")
            
            for log in self.transaction_log:
                log.show_transaction()
            
            
        
        #     # pass
    
    class Transaction_History:
        def __init__(self, transaction_name, transaction_amount):
            self.transaction_name = transaction_name
            self.transaction_amount = transaction_amount
            
        def show_transaction(self):
            print(f"{self.transaction_name}: £{self.transaction_amount}")
        
    
    # stock class
    class Stock:
        def __init__(self, stock_name, shares, buy_price, stock_total):
            self.stock_name = stock_name
            self.shares = shares
            self.buy_price = buy_price
            self.stock_total = stock_total
        
        def show_stock(self):
            print(f"Stock: {self.stock_name} \n Shares: {self.shares} Total Invested: £{self.stock_total} \n Bought Price: £{self.buy_price}")
            
    stock = {
        "Apple Inc" : 189.83,
        "NVIDIA Corp": 182.62,
        "Tesla Inc" : 398.28,
        "Meta Platforms Inc": 620.34,
        "Amazon.com Inc": 211.65, 
    }
    
    # class object created           
    account = Account("BIM117", 0, [], 0, [])
    
    while True:
        # menu
        print("____________________________________________")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Stock Market")
        print("5. Portfolio")
        print("6. Transaction History")
        print("0. Logout")
        print("____________________________________________")
        # user option input for menu 
        menu_option = int(input("Please Choose An Option: "))
        
        # handle non accepted inputs
        while menu_option not in range(0, 7):
            menu_option = int(input("Invalid! Please Choose An Option: "))
        
        # deposit
        if menu_option == 1:
            account.deposit()
           
        #withdrawal 
        if menu_option == 2:
            account.withdraw()
          
        # check current balance  
        if menu_option == 3:
            account.check_balance()
            
        # stock market   
        if menu_option == 4:
            
            print("Stock Market:")
            
            for i, company in enumerate(stock.keys(), start = 1):
                print(f"{i}. {company}")
            
            print("0. Back")
            
            print("____________________________________________")
            stock_choice = int(input("Please Select An Option: "))
            
            # apple stock purchase
            if stock_choice == 1:
                apple_stock = 189.83
                print("____________________________________________")
                print(f"Selected Apple Stock: \n Apple Stock Current Price: £{apple_stock:,.2f} | Current Balance: £{account.balance:,.2f}")
                
                print("Please choose: \n 1. Buy \n 2. Sell \n 0. Back")
                stock_trade = int(input("Please Select An Option: "))
                
                while stock_trade:
                    amount = int(input("Apple Stock - Enter Purchase Amount: £"))
                    
                    apple_shares = amount / apple_stock
                    
                    # buying power check + confirm purchase
                    if account.balance >= amount and account.balance > apple_stock:
                        print(f"Please confirm your purchase:")
                        print(f"Apple Stock Purchase: £{amount:,.2f}, Shares: {apple_shares:,.4f} \n 1. Confirm \n 0. Cancel")
                        confirm = int(input("Please Select An Option: "))
                        
                        # purchase overview
                        if confirm == 1:
                            print(f"Transaction Complete! \n You have Succesfully Purchased {apple_shares:,.4f} Shares of Apple Stock worth about £{amount:,.2f}.")
                            account.balance -= amount
                            account.total_invested += amount
                            # account.stock_invested
                            
                            # check if stock already exists or needs to be created
                            found = False
                            
                            for stock in account.stocks:
                                if stock.stock_name == "Apple":
                                    stock.shares += apple_shares
                                    stock.stock_total += amount
                                    found = True
                                    break
                                
                            if not found:
                                new_stock = Stock("Apple", apple_shares, apple_stock, amount)
                                account.stocks.append(new_stock)
                            
                            new_transaction = Transaction_History("APPLE", amount)
                            account.transaction_log.appened(new_transaction)
                            
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
                            # account.deposit()
                            account.balance = account.balance + account.deposit
                            print(f"Updated Balance: £{account.balance:,.2f}") 
                            print("____________________________________________")
                        else:
                            continue
            
            # stocks
            if stock_choice == 2:
                print("will add later")
            if stock_choice == 2:
                print("will add later")
            if stock_choice == 2:
                print("will add later")
            if stock_choice == 0:
                continue
        
        if menu_option == 5:
            account.portfolio()
            
        if menu_option == 6:
            account.transaction_log()
        
        # exit 
        if menu_option == 0:
            print("You have successfully logged out! Have a nice day!")
            break
                    


                              
investment_simulator() # run python main.py
