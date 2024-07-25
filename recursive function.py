# def factorial(x):
#     if x==1:
#         return 1
#     else:
#         return (x*factorial(x-1))
# num=int(input("enter the number:"))
# print("the factorial of num is",factorial(num))

# def is_palinrome(l,r,s):
#     if l>=r:
#         return True
#     if s[l]!=s[r]:
#         return False
#     return is_palinrome(l+1,r-1,s)
# my_string=input("enter the string")
# l=0
# r=len(my_string)-1#it reverse the character while using -1 and compare and store it in the r
# check=is_palinrome(l,r,my_string)

# if check:
#     print(f"{my_string} is palindrome")
# else:
#     print(f"{my_string} is not palindrome")

# def reverse_list(my_list,l,r):
#     if l>=r:
#         return my_list
#     tem=my_list[l]
#     my_list[l]=my_list[r]
#     my_list[r]=tem
#
#     return reverse_list(my_list,l+1,r-1)
# my_l=[3,1,5,4,7]
# l=0
# R=len(my_l)-1
# print('my list',my_l)
# print('reverse list',reverse_list(my_l,l,R))
# def cal_sum(num):
#     if num==1:
#         return 1
#     else:
#         return num+cal_sum(num-1)
# res=cal_sum(5)
# print(res)
def cal_sum():
    def cal_sum1():
        num=int(input("enter any number"))
        if num==1:
            return 1
        else:
            return num+cal_sum1()
    return cal_sum1()
res=cal_sum()
print(res)