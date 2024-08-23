class SB_123:
    def __init__(self):
        self.Total_amount = 0  # Initialize the balance as an instance variable

    def Authorization(self):
        acc_no = input("Enter the account number: ")
        if acc_no == 'SB-123':
            print("Account created successfully")
        else:
            print("Invalid account number")

    def deposit(self):
        money = int(input("Enter the money to deposit: "))
        self.Total_amount += money
        print(f'{money} is deposited. Total balance is {self.Total_amount}')

    def Withdraw(self):
        money = int(input("Enter the money to withdraw: "))
        if money > self.Total_amount:
            print("Insufficient funds!")
        else:
            self.Total_amount -= money
            print(f'{money} is withdrawn. Remaining balance is {self.Total_amount}')


class SB_124:
    def __init__(self):
        self.Total_amount = 0  # Initialize the balance as an instance variable

    def Authorization(self):
        acc_no = input("Enter the account number: ")
        if acc_no == 'SB-124':
            print("Account created successfully")
        else:
            print("Invalid account number")

    def deposit(self):
        money = int(input("Enter the money to deposit: "))
        self.Total_amount += money
        print(f'{money} is deposited. Total balance is {self.Total_amount}')

    def Withdraw(self):
        money = int(input("Enter the money to withdraw: "))
        if money > self.Total_amount:
            print("Insufficient funds!")
        else:
            self.Total_amount -= money
            print(f'{money} is withdrawn. Remaining balance is {self.Total_amount}')


# Example usage
b1 = SB_123()
b1.Authorization()
b1.deposit()
b1.Withdraw()

# b2 = SB_124()
# b2.Authorization()
# b2.deposit()
# b2.Withdraw()
