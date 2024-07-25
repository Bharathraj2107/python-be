
choice = """
1) Domestic
2) International
3) Quit
"""
Total_amount = 10000

Domestic_choices = """
1) Air India Express
2) IndiGo
3) SpiceJet
"""
International_choices = """
1) Malaysia Airlines
2) Etihad Airways
3) Emirates
"""
select = """
1) Book ticket
2) Cancel ticket
"""
def book_ticket(money, Total_amount):
    if money > Total_amount:
        print("Insufficient funds")
    else:
        Total_amount -= money
        print(f"Your Ticket price is {money}")
        print("your Ticket has been booked")
        print(f"Your Balance money is {Total_amount}")
    return Total_amount


def cancel_ticket(money, Total_amount):
    Total_amount += money
    print(f"Your Balance money is {Total_amount}")
    return Total_amount

def quit():
    print("Thank you")
    print("Visit again")
    exit()

while True:
    print(choice)
    user_choice = int(input("Enter the choice:"))

    if user_choice == 1:
        print(Domestic_choices)
        user_choiceD = int(input("Enter the choice:"))
        print(user_choiceD)

    elif user_choice == 2:
        print(International_choices)
        user_choiceI = int(input("Enter the choice:"))
        print(user_choiceI)

    elif user_choice == 3:
        quit()

    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        continue

    print(select)
    user_select = int(input("Please select the option:"))
    if user_select == 1:
        moneyb = int(input("Enter the price to book the ticket:1st class:Rs:7000,2nd class:Rs:5000,3rd class:Rs:3500: "))
        Total_amount = book_ticket(moneyb, Total_amount)
    elif user_select == 2:
        money=moneyb
        Total_amount = cancel_ticket(money, Total_amount)
        print("Your Ticket has been cancelled and your money has been refunded")
    else:
        print("Invalid choice. Please select 1 or 2.")
        