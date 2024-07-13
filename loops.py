# for x in range(1,11):
#     print(x)
# # ***********
#problems#3#######
#1 sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)

#2 for i in range(1,21,2):
    # print("The odd numbers is",i)
   # print("the even number is ",i)
#3
# for i in range(2000,2025):
#     if i%4==0:
#         print("the leap years are",i)
# 4
# sample=[1452,11.23,True,'Be-practical',(0,-1),[5,12],{"class":'v',"section":'A'}]
# for i in sample:
#     print(f"The item is {i}",type(i))
#5
# total=0
# lst=[23,48,24,67,87,4,23,78]
# for i  in lst:
#     if i%2==0:
      # print(i)
# total+=i
# print(total)
# lst=[2,3,4,5,6]
# for i in lst:
    # i=i*i
    # print(i)
    # i=i*i*i
    # print(i)
# pos=[]
# neg=[]
# x=[23,4,-6,2,-9,21,3,-45,-8]
# for i in x:
#     if i>0:
#         pos.append(i)
#     else:
#         neg.append(i)
# print(pos)
# print(neg)

# calci
# a=int(input("enter the value of a"))
# b=int(input("enter the value of b"))
# choice='''
# 1)+
# 2)-
# 3)*
# 4)/
# '''
# print(choice)
# choice=int(input("choose the operation "))
# list=["+","-","*","/"]
# choice-=1
# op=list[choice]
# if op=='+':
#     print(f"The addition of {a},{b} is ",a+b)
# elif op=='-':
#     print(f"The subtraction of {a} {b} ",a-b)
# elif op=='*':
#     print(f"The multiplication of  {a} {b}",a*b)
# elif op== '/':
#     print(f"The division of {a} {b}",a/b)
# else:
#     print("Invalid option")
# def fact(n):
#     n=int(input("enter the number for factorial"))
#     if n==1:
#       return 1
#     else:
#      return n*fact(n-1)
#
# fact(n)
# tb=int(input("enter the number for the table"))
# list=[1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     print(f"{tb}*{i}=",tb*i)
#fact
# fact=int(input("enter the number:"))
# fact+=1
# list=[]
# val=1
#
# for i in range(1,fact):
#   list.append(i)
# for i in list:
#    val*=i
# print(val)
#fact2
# num=int(input("enter the number:"))
# fact=1
# for i in range(1,num+1):
#     fact*=i;
# print(f"the factorial of a number is {fact}is",fact)
# sum = 0;
# lst = [23, 48, 24, 67, 87, 4, 23, 78]
# for i in lst:
#   while(i>0):
#     sum+=i
# print(sum)
#pallindrome
# num=int(input("enter any number"))
# rev=0
# temp=num
# while num!=0:
#     digit=num%10;
#     rev=rev*10+digit
#     num//=10
# print("The reverse of a number is",rev)
# if rev==temp:
#     print("Is Palindrome")
# else:
#     print("Is not Pallindrome")
#reverse
# num=int(input("enter any number"))
# rev=0
# while num!=0:
#     digit=num%10;
#     rev=rev*10+digit
#     num//=10
# print("The reverse of a number is",rev)
# if rev==temp:
#     print("Is Palindrome")
# else:
#     print("Is not Pallindrome")
#Astrong number
# num=int(input("enter any number"))
# temp=num
# rev=0
# pow=0
# am=0
# while num!=0:
#      digit=num%10;
#      pow=digit
#      am=am**pow*10+digit
#      num //= 10
# if digit==temp:
#      print("Is amstrong number")
# else:
#      print("Is not amstrong number")
#
# num=int(input("enter any 3 digit number"))
# sum=0
# temp=num
# while temp>0:
#      d=temp%10
#      sum+=d*d*d
#      temp//=10
# if sum==num:
#      print("it is an amstrong number")
# else:
#      print("it is not an amstrong number")
#break and continue
# for i in range(1,21):
#     if i==14:
#         break;
#     print(i)
# for i in range(1,21):
#     if i==14:#it will skip that iteration and move to next iteration and continue
#         continue
#     print(i)

# for r in range(1,6):
#    for c in range(1,r+1):
#        print(c,end=" ")
#    print()#it means new line and it prints it after complete iteration
#here  the print() it is straight to second for loop means it is out of inner loop still end means out of outer loop also
# for r in range(6,1,-1):
#    for c in range(1,r):
#       print(c,end=" ")
#    print()#it means new line
#54321
# 5432
# 543
# 21
# 1
#patterns
# for x in range(6,1,-1):
#     for y in range(6,x-1,-1):
#         print(y-1,end=" ")
# #     print()
# for x in range(3):
#     for y in range(1,11):
#         print(y,end=" ")
#     print("")
# rows=int(input("enter the # of rows"))
# cols=int(input("enter the # of columns"))
# symbols=input("enter the # of symbols")
# # for x in range(rows):
#     for y in range(cols):
#         print(symbols,end=" ")
#     print()
#loop with list items
# fruits=['mango','apple','grapes','peach']
# for f in fruits:
#     for i in f:
#         print(i,end="*")
#     print()
# color=['red','green','pink']
# items=['apple','veggies','dress']
# for x in color:
#     for y in items:
#         print(x,y)
#     print('')

# i=5
# while(i>0):
#     j=5
#     while(j>i):
#         print("*",end='')
#         j=j-1
#     i=i-1
#     print()
#append 2 list
# list1=[10,20,30]
# list2=[40,50,60]
# result=[]
# for i in list1:
#     for j in list2:
#       result.append(i+j)
# print(result)



# for r in range(1,7):
#     for c in range(1,r+1):
#        print(r,end=" ")
#     print()
#here r means number of rows c means number of columns
#here r starts from 1 and last index -1 so 6
#here c starts with 1 and r+1 means initial it is 1,2 for c last indesx-1 so (1,1) so 1 column will be printed
#(1,3) means (1,2) it takes and prints both in next line
# for r in range(1,7):
#     for c in range(1,r+1):
#        print("*",end=" ")
#     print()
# for r in range(7,1,-1):
#     for c in range(1,r+1):
#        print("*",end=" ")
#     print()
#here for 7,1,-1 it starts with 7 decrement by 1 it prints all until last number does not reaches 1 it stops
#see the below for start 10 and end 7
#1 2 3 4 5 6 7 8 9 10
#1 2 3 4 5 6 7 8 9
#1 2 3 4 5 6 7 8 here it prints until last number is not 7
# Number of rows in the upper part of the diamond
# n = 5

# Upper part of the diamond
# for r in range(1, n + 1):
#     # Print leading spaces
#     for c in range(n - r):
#         print(" ", end="")
#     # Print asterisks
#     for c in range(1, 2 * r):
#         print("*", end="")
#     # Move to the next line
#     print()
#
# # Lower part of the diamond
# for r in range(n - 1, 0, -1):
#     # Print leading spaces
#     for c in range(n - r):
#         print(" ", end="")
#     # Print asterisks
#     for c in range(1, 2 * r):
#         print("*", end="")
#     # Move to the next line
#     print()
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
#explain this pattern
#multiply 2 lists
# list1=[2,4,6,8]
# list2=[2,4,6,8]
# for i in list1:
#    for j in list2:
#     if i==j:
#         continue
#     print(i,"*",j,"=",i*j)
# a=1
# while a<=50:
#     sum=0
#     for i in range(1,a):
#         if i%2==0:
#             sum+=i
#     a=a+1
# print("the sum of even numbers is::",sum)
# a=2
# for i in range(1,a):#(1,0)not print anything and (1,1) prints 1
# #     print(i)
# x=1
# while x<=10:
#     print(x)
#     x+=1
# fruits=['apple','mango','grapes','kiwi']
# for f in fruits:
#     count=0
#     while count<6:
#         print(f,end=" ")
#         count=count+1
#     print()
# for x in range(1,4):
#     print(x)

#rock paper scissor game
# import random
# num=random.randint(0,2)
# # a = """
# # do you want play:
# # 1)yes
# # 2)no
# # """
# option="""
# 1)scissor
# 2)paper
# 3)stone
# """
# print(option)
# choice=input("enter the choice:")
# list=['scissor','paper','stone']
# type=list[num]
# print(f"computer choose {type}")
# # if choice==type:
# #     continue
# if choice=='scissor' and type=='paper':
#         print("you win")
# elif choice == 'scissor' and type== 'scissor':
#         print("draw")
# elif choice == 'scissor' and type == 'stone':
#         print("computer win")
# elif choice == 'paper' and type == 'paper':
#         print("draw")
# elif choice == 'paper' and type == 'scissor':
#         print("computer win")
# elif choice == 'paper' and type == 'stone':
#         print("you win")
# elif choice == 'stone' and type == 'paper':
#         print("computer win")
# elif choice == 'stone' and type == 'scissor':
#         print("you win")
# elif choice == 'stone' and type == 'stone':
#         print("draw")
# else:
#   print(a)
# a=input("enter yes or no")
# import random
#
# choices = ['stone', 'paper', 'scissors']
#
# while True:
#     user_choice = input("Enter your choice (stone, paper, scissors) or 'quit' to exit: ").lower()
#
#     if user_choice == 'quit':
#         print("Thanks for playing!")
#         break
#
#     if user_choice not in choices:
#         print("Invalid choice. Please try again.")
#         continue
#
#     computer_choice = random.choice(choices)
#     print(f"Computer chose: {computer_choice}")
#
#     if user_choice == computer_choice:
#         result = "It's a tie!"
#     elif (user_choice == 'stone' and computer_choice == 'scissors') or \
#             (user_choice == 'paper' and computer_choice == 'stone') or \
#             (user_choice == 'scissors' and computer_choice == 'paper'):
#         result = "You win!"
#     else:
#         result = "You lose!"
#
#     print(result)
#     print()  # Print a newline for better readability
#
#     play_again = input("Do you want to play again? (yes/no): ").lower()
#     if play_again != 'yes':
#         print("Thanks for playing!")
#         break
import random

choices=['scissors','stone','paper']

while True:
    user_choice=input("enter the choice('scissors','paper',stone) or quit:").lower()

    if user_choice=='quit':
        print("Thanks for playing")
        break;

    if user_choice not in choices:
        print("invalid option please try again")
        continue
        
    computer_choice=random.choice(choices)
    print(f"computers choice is {computer_choice}")
#here \ backslash means code is continued on the next line also

    if user_choice==computer_choice:
        result="It's a Tie"
    elif (user_choice == 'stone' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'stone') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result = "You win!"
    else:
        result = "You lose!"

    print(result)
    print()

    playagain=input("do you want to playagain (yes/no)")
    if playagain!='yes':
        print("Thanks for playing")
        break