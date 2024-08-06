import datetime#this provides class for manipulating date and time

# Script starts.
# datetime module is imported.
# greet_with_time decorator is defined.
# greet function is defined and decorated
# with greet_with_time.
# User is prompted to enter  their name.
# User enterstheir
# name, and it is stored in name.
# greet(name) is called:
# wrapper function from greet_with_time decorator
# executes:
# Current time is obtained.
# Original greet function is called
# with the modified name argument.
# Greeting message with the current time is printed.

# The greet_with_time function is defined, taking a function func as an argument.
# Inside greet_with_time, the wrapper function is defined. It takes a single argument name.
# The wrapper function gets the current time using datetime.datetime.now().time() and converts it to a string.
# It then calls the original function func, appending a message with the current time to the argument name.
# The greet_with_time function returns the wrapper function.
#
# The greet function (which is now the wrapper function returned by the greet_with_time decorator) is called with the argument name.
# Inside the wrapper function:
# The current time is obtained using datetime.datetime.now().time() and converted to a string.
# The original greet function is called with the modified name argument, which now includes the current time message.
# The print statement inside the original greet function executes, printing the greeting message with the current time.

def greet_with_time(func):
    def wrapper(name):
        current_time=str(datetime.datetime.now().time())
        func(name+"! the time is currently"+current_time)
    return wrapper
@greet_with_time

def greet(name):
    print("hello"+name)
name=input("enter your name")
greet(name)
#
# def authenticate(func):
#     def wrapper(name):
#         if name=="john":
#             func(name)
#         else:
#             print("access denied")
#     return wrapper
#
# def greet_with_time(format_string):
#     def actual_decorator(func):
#         def wrapper(name):
#             current_time=datetime.datetime.now().time()
#             formatted_time=current_time.strftime(format_string)
#             func(name+"! the time is currently"+formatted_time)
#         return wrapper
#     return actual_decorator
# @authenticate
# @greet_with_time("%I:%M %p")

# def greet(name):
#     print("hello"+name)
#
# greet("john")

# def site():
#     print("python programming... im calling by the variable")
# website=site
# print(f"{site=}",)
# print(f"{website=}")
# site()
# website()

# def sqrt(num):
#     return num ** 0.5
# def square(num):
#     return num ** 2
# def math(function):
#     print(function(4))
# math(sqrt)
# math(square)

# def math():
#     def square(num):
#        return num ** 2
#        print(square(2))
# math()
#
# def math(num):
#     def square():
#         return num ** 2
#     print(square())
# math(2)

# def sum_decorator(func):
#     def inner_demo():
#         print("the addition of two odd numbers 3 and 7")
#         func()
#         print("is always an even number")
#     return inner_demo
# @sum_decorator
# def odd_add():
#     print(3+7)
# odd_add()