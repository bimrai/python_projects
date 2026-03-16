def investment_simulator():
    
    # will use later for expenditure feature
    expenditure = []
    
    balance = 0
    
    while True:
        
        # menu
        print("____________________________________________")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Stock Market")
        print("5. Portfolio")
        print("____________________________________________")
        # user option input for menu 
        option = int(input("Please choose an option: "))
        
        # deposit
        if option == 1:
            deposit = int(input("Enter Deposit Amount: £"))
            balance += deposit
            print(f"Updated Balance: £{balance}") 
            print("____________________________________________")
           
        #withdrawal 
        if option == 2:
            withdraw = int(input("Enter Withdrawal Amount: £"))
            balance = balance - withdraw
            print(f"Updated Balance: £{balance}")
          
        # check current balance  
        if option == 3:
            print(f"Current Balance: £{balance}")
            
        if option == 4:
            print("____________________________________________")
            print("1. Watchlist")
            print("0. Back")
            print("____________________________________________")
            option = int(input("Please choose an option: "))
            
            if option == 1:
                print("____________________________________________")
                print("1. Apple")
                print("2. NVIDIA")
                print("3. Tesla")
                print("4. Meta")
                print("5. Amazon")
                print("0. Back")
                print("____________________________________________")
                option = int(input("Please choose an option: "))
                
                if option == 1:
                    apple_stock = 189.83
                    print(f"Apple Stock Current Price: £{apple_stock}")
                    
                    while True:
                        amount = int(input("Apple Stock, Enter Amount: £"))
                    
                        if balance >= amount and balance > apple_stock:
                            apple_shares = amount / apple_stock
                            print(f"You have Succesfully Purchased {apple_shares:.4f} Shares of Apple Stock worth about £{amount}.")
                            balance -= amount
                            break
                        elif balance < amount:
                            print(f"Insufficient Funds: £{balance}.")
                            print("Would you like to add funds?")
                            print("1. Yes")
                            print("0. No")
                            pick = int(input("Enter 1 or 0: "))
                            
                            if pick == 1:
                                balance = int(input("Enter Deposit Amount: £"))
                                balance += balance
                                print(f"Updated Balance: £{balance}") 
                                print("____________________________________________")
                            else:
                                break
                
                if option == 2:
                    print("will add later")
                if option == 2:
                    print("will add later")
                if option == 2:
                    print("will add later")
                if option == 2:
                    print("will add later")
                    
                if option == 0:
                    continue
                    
                        

        
investment_simulator()