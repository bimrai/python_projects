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
        print("0. Exit")
        print("____________________________________________")
        # user option input for menu 
        option = int(input("Please choose an option: "))
        
        # deposit
        if option == 1:
            deposit = int(input("Deposit \n Enter Deposit Amount: £"))
            balance += deposit
            print("____________________________________________")
            print(f"You have successfully deposited £{deposit:,.2f} \n Updated Balance: £{balance:,.2f}")
           
        #withdrawal 
        if option == 2:
            while True:
                print("____________________________________________")
                withdraw = int(input("Withdraw \n Enter Withdrawal Amount: £"))
                
                if withdraw <= balance:
                    balance = balance - withdraw
                    print(f"You have successfully withdrawn £{withdraw:,.2f} \n Updated Balance: £{balance:,.2f}")
                    break
                elif withdraw > balance:
                    print("Insufficent Funds")
                    continue
          
        # check current balance  
        if option == 3:
            print("____________________________________________")
            print(f"Balance \n Current Balance: £{balance:,.2f}")
            
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
            
            if option == 1:
                apple_stock = 189.83
                print("____________________________________________")
                print(f"Selected Apple Stock: \n Apple Stock Current Price: £{apple_stock:,.2f} | Current Balance: £{balance:,.2f}")
                
                while True:
                    amount = int(input("Apple Stock - Enter Purchase Amount: £"))
                    
                    apple_shares = amount / apple_stock
                    
                    if balance >= amount and balance > apple_stock:
                        print(f"Please confirm your purchase - Apple Stock Purchase: £{amount:,.2f} \n Shares: {apple_shares:,.4f}")
                        print("1. Confirm")
                        print("0. Cancel")
                        confirm = int(input("Please Enter: "))
                        

                        if confirm == 1:
                            print(f"Transaction Complete! \n You have Succesfully Purchased {apple_shares:,.4f} Shares of Apple Stock worth about £{amount:,.2f}.")
                            balance -= amount
                            break
                        else:
                            break
                    
                    elif balance < amount:
                        print(f"Insufficient Funds: £{balance:,.2f}.")
                        print("Would you like to add funds?")
                        print("1. Yes")
                        print("0. No")
                        pick = int(input("Enter 1 or 0: "))
                        
                        if pick == 1:
                            deposit = int(input("Enter Deposit Amount: £"))
                            balance = balance + deposit
                            print(f"Updated Balance: £{balance:,.2f}") 
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
            print("Have a nice day. Goodbye!")
            break
                    


                              
investment_simulator() # run python investment_simulator.py
