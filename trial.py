# my_tuple="mouse",456,[8,4,6],(1,2,3),873987
# print(my_tuple[2][2])
# tuple="hil","csd","dog"
# a,b,c=tuple
# print(a)
# print(b)
# print(c)
# num_tuple = (2, 4, 5, 7, 8, (10,17,23),45,23)
# print(num_tuple[:3] )
# print(num_tuple[4:] )
# print(num_tuple[-3:] )
# print(num_tuple[2:5] )
# #negative Index:
# print(num_tuple [-1])
# print(num_tuple [-6])
# # nested tuple
# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# # nested index
# print(n_tuple[0][3])
# print(n_tuple[1][1])

# Examples:
# my_data = (1, "Steve", (11, 22, 33))
# print(my_data[1][3])
# print(my_data[2][1])

# Zipping Tuples:
# The zip( ) method takes multiple sequence objects and returns an iterable object by matching their elements.
# The zip( ) method takes the three tuples and returns a zip object, which is an iterator. To consume the iterator object, we need to convert it to either a list or a tuple, like this:
# Example:
# First_names = ('Anil', 'Sarah', 'Mehta', 'Arjun')
# last_names = ('Narang', 'Smith', 'Raj', 'Gowda')
# ages = (49, 55, 39, 33)
# res = zip(First_names, last_names,ages)
# print( res)
# print("------------------------------------------------")
# customers = tuple(res)
# print(customers)

# Unpacking Tuples
# Unpacking a tuple allows us to extract the tuple elements and assign them to named variables.
# first_name, last_name, age = customers[2]
# print(first_name, last_name,   ',', age,   'years old')
# my_data = (1, [9, 8, 7], "World")
# print(my_data)
# # changing the element of the list
# # this is valid because list is mutable
# my_data[1][2] = 99
# print(my_data)

# my_data = (1, 2, 3, 4, 5, 6)
# print(my_data)
# # deleting entire tuple is possible
# del my_data
# print(my_data)
#
# my_data = (11, 22, 33, 44, 55, 66, 77, 88, 99)
# print(my_data)
# print(22 in my_data)
# print(2 in my_data)
# print(88 not in my_data)
# print(101 not in my_data)

# Tuple_a = (1, 2)
# Tuple_b = ('x', 'y')
# Tuple_c = Tuple_a + Tuple_b
# print (Tuple_c)
#
# a = (1, 'x', 3, 1,5, 'x')
# print(a.index('x'))
# print(a.index(1))

# a = (3, 0, 2)
# a.sort()

# a = (3, 5, 8, 2)
# print(type(a))
# b = sorted(a)
# print(b)
# print(type(b))
# x=int(input("enter the value of x"))
# y=int(input("enter the value of y"))
#
# if x>y:
#     print(f"{x} is greater than {y}")
# else:
#     print(f"{x} is smaller than {y}")


# 1)
# x=int(input("enter a number"))
# if x%2==0:
#     print(f"The number is {x} is even")
# else:
#     print(f"The number is {x} is odd")
# 2)
# x=int(input("enter the year to check "))
# if x/4==0:
#     print(f"The year {x}is leap year")
# else:
#     print(f"The year {x}is not leap year")
# 3)
# x=int(input("enter the age"))
# if x>=18:
#     print(f"your {x} are eligible to vote")
# else:
#     print(f"your {x} not eligible to vote")
#
# # 4)
# x=int(input("enter the number to check divisibility"))
# if x%5==0 or x%3==0:
#     print(f"the number {x} is divisible by both 5 and 3")
# else:
#     print(f"the {x} number is not divisible by both")
# 5)
# x=int(input("enter the value of x"))
# y=int(input("enter the value of y"))
# z=int(input("enter the value of z"))
# if x>y and x>z:
#     print(f"{x} is greater among the three")
# elif y>x and y>z:
#     print(f"{y} is greater among the three")
# else:
#     print(f"{z} is greater among the three")
# 6)
# list_vow=['a','e','i','o','u']
# x=input("enter the letter")
# if x in list_vow:
#     print(f"{x} is a vowel ")
# else:
#     print(f"{x} is a constant")
# 7)

# a=int(input("enter the marks of a"))
# b=int(input("enter the marks of b"))
# c=int(input("enter the marks of c"))
# d=int(input("enter the marks of d"))
# e=int(input("enter the marks of e"))
# sum=a+b+c+d+e
# avg=sum/5
# if avg>95:
#     print(f"{avg} is Distinction")
# elif avg>=65 and avg<=95:
#     print(f"{avg} is First class")
# elif avg >= 45 and avg <= 60:
#     print(f"{avg} is Second class")
# elif avg>=30 and avg<=45:
#     print(f"{avg} is Third class")
# else:
#     print(f"{avg} is fail")
#8
# a="SBI123"
# id=89
# name="Bharath raj"
# address="Bangalore"
# contact=123456789
# balance=1234
# y=input("enter the account number")
# if y==a:
#     print(f"the account holder name is {name}")
#     print(f"the account holder address is {address}")
#     print(f"the account holder contact is {contact}")
#     print(f"The balance is {balance}")
# else:
#     print(f"invalid user give proper details")
#
# My_Set={1,'s',7.8,"hghj"}
# print(My_Set)
# a=set({2,'b',7.9})
# print(a)
# set1 = set( [1, 1, 1, 2, 2, 3] )          # from a list
# set2 = set( ('a', 'a', 'b', 'b', 'c') )   # from a tuple
# set3 = set('anaconda')
# print(set1,set2,set3)
# set4 = {1, 1, 'anaconda', 'anaconda', 8.6, (1, 2, 3), None}
# print('Set1:::: ', set1)
# print('Set2::::: ', set2)
# print('Set3:::: ', set3)
# print('Set4:::: ', set4)
# tp=(1,5,3)
# lp=sorted(tp) ##in tuple and set we can change manually
#in tuple there is no sort what is diff btw set() function and normal set
# print(lp)
# myset = {"apple", "banana", "cherry"}
# print(len(myset))
# print(myset)
# myset.add("orange")
# print(myset)
# myset = {"apple", "banana", "cherry"}
# myset.update( {"orange", "mango", "grapes"} )
# print(myset)
# my_set={1,'s',7.8}
# My_Set.add(3)
# print(My_Set)
# My_Set={1,'s',7.8}
# My_Set.update([2,4.6,1,'r'])
# print(My_Set)
# my_set.update( [4, 5], {1, 6, 8} )xfkjdfkgkljfgkljfgjkgjk
# print(my_set)
# myset = {1, 2, 3, 4}
# print(myset)
# # Removing a particular item using the discard() method
# myset.discard(1)
# print(myset)
# myset.discard(5)  # the item was absent in the set
# print(myset)
# Removing a particular item using the remove() method
# myset.remove(4)   # the item was present in the set
# print(myset)
# myset.remove(5)   # the item was absent in the set
# print(myset)
# Taking the set from the code above
# myset = {2, 3,7,9}
# # Removing and returning a random item
# print(myset.pop())  # the removed and returned item
# print(myset)        # the updated set
# # Removing all the items
# myset.clear()
# print(myset)
# # An attempt to remove and return a random item from an empty set
# myset.pop()
# print(myset)
# myset = {5, 10, 15}
# print('Set:', myset)
# print('Size:', len(myset))
# print('Min:', min(myset))
# print('Max:', max(myset))
# print('Sum:', sum(myset))
#print('\n')
# myset = {(1, 2), (1, 0), (2, 3)}
# print('Set:', myset)
# print('Min:', min(myset))
# print('Max:', max(myset))
# print(all({1, 2,'a',2.4}))
# print(all({1, False}))
# print(any({1, False}))
# print(any({False, False}))
# print(all({}))
# print(any({}))
#what it is evaluating revise once333333333333333333333333333333333333333333333333333
# myset = {4, 2, 5, 1, 3}
# print(myset)
# print(sorted(myset))
# --------------------------------------------------------------------------------------------------
# myset = {'c', 'b', 'e', 'a', 'd'}
# print(sorted(myset))
# sample_set = set(['100', 'Days', 'Of', 'Code'])
# print(sample_set)
# print('100' in sample_set)
# print('100' not in sample_set)
# print('red' in sample_set)
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7}
# print(a | b)
# print(b | a)
# print(a.union(b))
# print(b.union(a))
# a={1, 2, 4.6, 7.8, 'r', 's'}
# b={2,5,'d','abc'}
# c=a|b
# print(a or b) what is or
# print(a and b) and
# print(c) | why

# a={1, 2, 4.6, 7.8, 'r', 's'}
# b={2,5,'d','abc'}
# c={'m',23,76,4.7}
# print("Set a U b = ",a.union(b))
# print("Set a U b U c = ",a.union(b,c))
# Set_A = {1,2,3,4,5}
# Set_B = {4,5,6,7}
# print (Set_A & Set_B)
# a={1, 2,5, 4.6, 7.8, 'r', 's'}
# b={2,5,'d','abc'}
# c={2,3,4,}
# print(a&b)
# print(a&b&c)
# Difference of two sets
# initialize A and B
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A - B)
# # use difference function on A
# print(A.difference(B))
# print(B-A)
# # use difference function on B
# B.difference(A)
# a={1, 2,5, 4.6, 7.8, 'r', 's'}
# b=frozenset(a)
# print(b)
# frozenset() is an inbuilt Python function that takes an iterable object as input and makes it immutable. It Simply freezes the iterable objects and makes them unchangeable. The frozenset() function returns an unchangeable frozenset object (which is like a set object, only unchangeable).
# d=dict({'boy':'roy','age':35})
# print(d)
# MLB_team = dict ( [
#      ('Colorado', 'Rockies'),
#      ('Boston', 'Red Sox'),
#      ('Minnesota', 'Twins'),
#      ('Milwaukee', 'Brewers'),
#      ('Seattle', 'Mariners'),
# ] )
# MLB_team['Boston'] = 'Bos'
# print(MLB_team)

# print(MLB_team)
# MLB_team = dict (
#      Colorad='Rockies',
#      Boston='Red Sox',
#      Minnesota='Twins',
#      Milwaukee='Brewers',
#      Seattle='Mariners',
#       Age = 23
#  )
# print(MLB_team)

# Employee = {"Name": "John", "Age": 29, "experience":4.6,"salary":25000,"Company":"GOOGLE"}

# print(type(Employee))

# print("printing Employee data .... ")
# print("Name:",Employee["Name"])#ask this  once
# print("Name : %s" %Employee["Name"])
# print("Age : %d" %Employee["Age"])
# print("Experience %f" %Employee["experience"])
# print("Salary : %d"%Employee["salary"])
# print("Company : %s" %Employee["Company"])
# D1={}
# D1[0] = 'Peter'
# D1[2] = 'Joseph'
# D1[4] = 'Ricky'
# print("\nDictionary after adding 3 elements: ")
# print(D1)
# Adding set of values with a single Key, The Emp_ages doesn't exist to dictionary
# Dict={}
# Dict['Emp_ages'] = 20, 33, 24
# print("\nDictionary after adding 3 elements: ")
# print(Dict)
# # Updating existing Key's Value
# Dict[3] = 'Dict as a Data type'
# print("\nUpdated key value: ")
# print(Dict)
# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
# print("printing Employee data .... ")
# print(Employee)
# print("Enter the details of the new employee....")
# Employee["Name"] = input("Name: ");
# Employee["Age"] = int(input("Age: "));
# Employee["salary"] = int(input("Salary: "));
# Employee["Company"] = input("Company:");
# print("printing the new data");
# print(Employee)
# Employee = {"Name": "John", "Age": 29, "salary":25000,"Company":"GOOGLE"}
# print(type(Employee))
# print("printing Employee data .... ")
# print(Employee)
# print("Deleting some of the employee data")
# del Employee["Name"]
# del Employee["Company"]
# print("printing the modified information ")
# print(Employee)
# print("Deleting the dictionary: Employee");
# del Employee
# print("Lets try to print it again ");
# print(Employee)
# y_dict = {'a': 10, 'b': 20, 'c': 30}
# print(y_dict.get('b'))
# d = {'a': 10, 'b': 20, 'c': 30}
# list(d.items())
# print(list(d.items())[1][0])
# print(list(d.items())[1][1])
# d = {'a': 10, 'b': 20, 'c': 30}
# print(list(d.keys()))
# print(d.keys())
# d = {'a': 10, 'b': 20, 'c': 30}
# print(list(d.values()))
# My_list1 = [ 'Python', 'C++', 'JavaScript']
# my_list2 = [1, 2, 3]
# print(My_list1, my_list2)
# my_list = ['p', 'r', 'o', 'b', 'l','e','m']
# subject = ['maths', 'science','social', ['kannada','english','hindi'], 'sanskrit']
#
# print (subject[3] [2])

# first item
# print(my_list[0])
#
# # third item
# print(my_list[2])
#
# # fifth item
# print(my_list[4])
# Negative indexing in lists
# my_list = ['p','r','o','b','e']
# re=my_list[:5]
# print(re)
# even = [2, 4, 6, 8]
# # even.reverse()
# nw=even[::-1]
# print(nw)

# # change the 1st item
# even[0] = 1
# print(even)
#
# # change 1nd to 3rd items
# even [1:4] = [3, 5, 7]
# print(even)
# a = "Python oPerators"
# b = {1, 'x', 2.0, 'y'}
#
# print("P" in a)
# print("p" in a)
#
# print("Python" not in a)
#
# print(1 in b)
# a1 = 3
# b1 = 3
# a2 = "Python"
# b2 = "python"
#
# a3 = [4, 5, 6]
# b3 = [4, 5, 6]
#
# print(a1 is not b1)
# print(a1 is b1)ask why
# print(a2 is not b2)
# print(a3 is b3)
# print(a3 is not b3) ask why
# a = 5
# b = 5.5
# sum = a + b
# print (sum)
# print (type (sum))
# e = "8"
# e = float(8)
# print ("After converting to float : ")
# print (e)
# print(type(e))







