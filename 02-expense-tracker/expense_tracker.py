def expense_tracker():
    
    # will use later for expenditure feature
    expenditure = []
    
    while True:
        
        # menu
        print("__________________")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Average Current Spendings")
        print("__________________")
        # user option input for menu 
        option = int(input("Please choose an option: "))
        
        # deposit
        if option == 1:
            balance = int(input("Enter Deposit Amount: £"))
            print(f"Updated Balance: £{balance}") 
            print("__________________")
           
        #withdrawal 
        if option == 2:
            withdraw = int(input("Enter Withdrawal Amount: £"))
            balance = balance - withdraw
            print(f"Updated Balance: £{balance}")
          
        # check current balance  
        if option == 3:
            print(f"Current Balance: £{balance}")

        
expense_tracker()
