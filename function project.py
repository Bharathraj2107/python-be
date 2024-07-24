Total_amount = 10000
name = input("Enter the name: ")
password = input("Enter the password: ")
print("Welcome!")

choices = """
    1) withdraw money
    2) deposit money
    3) log out
    """

def withdraw(money, Total_amount):
    if money > Total_amount:
        print("Insufficient funds")
    else:
        Total_amount -= money
        print(f"Your Bank Balance is {Total_amount}")
    return Total_amount

def depo_money(money, Total_amount):
    Total_amount += money
    print(f"Your Bank Balance is {Total_amount}")
    return Total_amount

def log_out():
    print("Thank you")
    print("Visit again")

while True:
    print(choices)
    user_choice = input("Enter the choice: ")

    if user_choice == "1":
        money = int(input("Enter the money to withdraw: "))
        Total_amount = withdraw(money, Total_amount)

    elif user_choice == "2":
        money = int(input("Enter the money to deposit: "))
        Total_amount = depo_money(money, Total_amount)

    elif user_choice == "3":
        log_out()
        break

    else:
        print("Invalid choice")
