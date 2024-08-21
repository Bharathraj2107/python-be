Total_amount=0
class SB_123:
    def Authorization(self):
        acc_no=input("enter the account number")
        if 'SB-123'==acc_no:
            print("Account created successfully")
    def deposit(self,Total_amount):
        money=int(input("enter the money to deposit"))
        Total_amount+=money
        print(str(Total_amount)+' is deposited')

    def Withdraw(self,Total_amount):
        money=int(input("enter the money to withdraw"))
        super()
        Total_amount-=money
        print(str(Total_amount)+' is withdrawn')


class SB_124:
    def Authorization(self):
        acc_no = input("enter the account number")
        if 'SB-124' == acc_no:
            print("Account created successfully")

    def deposit(self, Total_amount):
        money = int(input("enter the money to deposit"))
        Total_amount+=money
        print(Total_amount)

    def Withdraw(self, Total_amount):
        money = int(input("enter the money to withdraw"))
        Total_amount-=money
        print(Total_amount)

b1=SB_123()
b1.Authorization()
b1.deposit(Total_amount)
b1.Withdraw(Total_amount)
# b2=SB_124()
# b2.deposit(1200)
# b2.Withdraw(200)