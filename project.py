name = input("please kindly enter your name:")
choice = '''
please select the type of vehicle
1)Two wheeler
2)four wheeler
'''
print(choice)
type = int(input("enter the choice:"))
list_2wheeler = ['RX', 'RoyalEnfield', 'KTM', 'TVS']
list_4wheeler = ['TataPunch', 'MarutiErtiga', 'HyundaiCreta', 'ToyotaFortuner']

if type == 1:
    print('''
 Please select any vehicle from the below
    1)RX
    2)RoyalEnfield
    3)KTM
    4)TVS
    ''')
elif type==2:
    print('''
    Please select any vehicle from the below
    1)TataPunch
    2)MarutiErtiga
    3)HyundaiCreta
    4)ToyotaFortuner
    ''')
# else:
    # print("Invalid choice")

hours =int(input("enter number of hours:"))
choice2 =int(input("enter the choice of vehicle:"))
choice2 -=1

vehicle=None
cost=0

if type == 1:
    tw = list_2wheeler
    vehicle = tw[choice2]
    if vehicle== 'RX':
         cost = 200*hours+0.18
    elif vehicle== 'RoyalEnfield':
         cost = 400*hours+0.18
    elif vehicle== 'KTM':
         cost = 600*hours+0.18
    elif vehicle== 'TVS':
      cost = 800*hours+0.18
elif type == 2:
    fw = list_4wheeler
    vehicle = fw[choice2]
    if vehicle== 'TataPunch':
        cost = 1000*hours+0.18
    elif vehicle== 'MarutiErtiga':
       cost = 1200*hours+0.18
    elif vehicle== 'HyundaiCreta':
        cost = 1400*hours+0.18
    elif vehicle== 'ToyotaFortuner':
      cost = 1600*hours+0.18


print("***************************")
print("BIKE AND CAR RENTS")
print(f"Customer Name: {name}")
print(f"Vehicle: {vehicle}")
print(f"Total Cost: {cost}")
print("THANK YOU")
print("##VISIT AGAIN##")
print("*****************************")

