# try:
#     numerator=50
#     denom=int(input("Enter the denominator"))
#     quotient=(numerator/denom)
#     print(quotient,"Division performed successfully")
# except ZeroDivisionError:
#     print("denominator as zero is not allowed")
# except ValueError:
#     print("Only integers should be entered")
# else:
#     print("The result of division operation is ",quotient)#this is printed only when try block is executed
# finally:
#     print("Over and out")#it is printed all the time whether it executes try or except to indicate it is completed executed
#
# prices={'pen':10,'pencil':5,'Notebook':25}
# item=input('get price of:')
# try:
#     print(f"The price of {item} is {prices[item]}")
# except KeyError:
#     print(f"The price of {item} is not known")
# else:
#     print(f"There is no error in the statement")

# print("Trying to display the factorial")
#
# try:
#     fact=1
#     num=int(input("enter any number"))
#     for x in range(1,num+1):
#         fact*=x#fact=fact*x
#     print(f"The factorial of {x} is ::",fact)
# except ValueError:
#     print("Input only numbers not the alphabets")
# else:
#     print("finally got the answer")
# finally:
#     print("The code got its answer")
def square_data(numbers):
    if not isinstance(numbers,(list,tuple or set)):#if set occurs it gives error if , instead of or no error if or means if set occurs gives error
        raise TypeError(f"list or tuple expected,got '{type(numbers).__name__}'")
    return [number**2 for number in numbers]
# print(square_data([1,2,3,4,5]))
print(square_data({1,2,3,4,5}))