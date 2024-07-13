Hotel="Priyadarshini Grand"
Receipe='''
1)Dosa and Idle
2)palav
3)juice
4)Ice Cream
'''
print(Receipe)
choice=int(input("choose the item "))
list=["Dosa and Idle","palav","juice","Ice Cream"]
choice-=1
dish=list[choice]
Table='''
1)Table 1
2)Table 2
3)Table 3
4)Table 4
'''
cost=0
print(Table)
tc=int(input("choose the table"))
if dish =="Dosa and Idle":
     cost = 35
elif dish== "palav":
    # print(f"{dish}cost is 45 and table is {tc}")
    cost=45
elif dish == "juice":
    # print(f"{dish}cost is 20 and table is {tc}")
    cost=20
elif dish == "Ice Cream ":
     cost=10
print("*******************")
print(f"{Hotel} ")
print(f"{dish} is the dish")
print(f"The cost is {cost} ")
print(f"{tc} is the table")
print("Thank You")
print("Visit again")
print("********************")
# The error in the provided code is because the if and elif conditions are checking
# Receipe == "dish", which is always false
# since Receipe is a string containing the list of items, and "dish" is not in Receipe.
# Instead, you should compare dish directly with the respective strings.
#The if and elif conditions now check dish against the respective strings instead of Receipe == "dish".