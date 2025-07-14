class ATM:
    def __init__(self):
        self.pin = 3569
        self.balance = 5000
    def check_balance(self):
        print(f"Your balance is ₹{self.balance}")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid amount to deposit.")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount to withdraw.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")
    def run(self):
        print("Welcome to the ATM!")
        entered_pin = int(input("Please enter your 4-digit PIN: "))
        if entered_pin != self.pin:
            print("Incorrect PIN. Exiting.")
            return
        while True:
            print("\n====== ATM Menu ======")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == "3":
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == "4":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
atm = ATM()
atm.run()