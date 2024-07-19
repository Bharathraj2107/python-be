# My_list1 = [ 'Python', 'C++', 'JavaScript']
# my_list2 = [1, 2, 3]
# print(My_list1, my_list2)
# my_list = ["mouse", [8, 4, 6], ['a'] ]
# print(my_list)
# my_list = ['p', 'r', 'o', 'b', 'l','e','m']
# subject = ['maths', 'science','social', ['kannada','english','hindi'], 'sanskrit']
#
# print (subject[3] [2])
#
# # first item
# print(my_list[0])
#
# # third item
# print(my_list[2])
#
# # fifth item
# print(my_list[4])
# my_list = ['p','r','o','b','e']
#
# # last item
# print(my_list[-1])
#
# # fifth last item
# print(my_list[-5])
# List slicing in Python

# my_list = ['p','r','o','g','r','a','m','m','I','I','n','g']
# print(len(my_list))

# elements from index 2 to index 4 (it will read (n-1) logic)
# print(my_list[2:5])


# elements from index 5 to end
# print(my_list[5:])

# elements beginning to end
# print(my_list[:])
# print(my_list[:5])
# print(my_list[-9: -7])
# Correcting mistake values in a list
# even = [2, 4, 6, 8]
# print(even)
# # change the 1st item
# even[0] = 1
# print(even)
#
# # change 1nd to 3rd items
# even [1:4] = [3, 5, 7]
# print(even)
# even = [1, 3, 5]
# even.append( [7,8,9] )
# print(even)
# even.extend([9, 11, 13])
# print(even)
# my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# # delete one item through index
# del my_list[2]
# print(my_list)
#
# # delete multiple items
# del my_list[1:4]
# print(my_list)
#
# # delete the entire list
# del my_list
# print(my_list)
# my_list = ['p','r','o','b', ['l','u','p'], 'e','m']
# # my_list.remove('m')
# # print(my_list)
#
# print(my_list.pop(3))
# print(my_list)
#
# my_list.clear()
# print(my_list)
# pow2 = [ 2 ** x for x in range(10) ]
# print(pow2)
# # The above code is equivalent to:
# pow2 = []
# for x in range(10):
#    pow2.append(2 ** x)
# print(pow2)
# for fruit in ['apple','banana','mango']:
#     print("I like",fruit)
# my_list = ['p', 'r', 'o', 'b', 'l', 'A', 'm']
#
# print('p' in my_list)
#
# print('a' in my_list)
#
# print('c' not in my_list)
# len(list)
# Example:
# cars = ['Ford', 'Volvo', 'BMW', 'Tesla']
# #find length of list
# length = len(cars)
# print('Length of the list is :', length)
# mylist = [21, 5, 8, 52, 21, 87, 52]
# #reverse list
# mylist.reverse()
# #print the list
# print(mylist)
# mylist = [21, 5, 8, 52, 21, 87, 52]
# mylist.sort(reverse=True)
# print(mylist)
print("-----------------------------------------")
# my_tuple = (2, "Hello", 3.4)
# print(my_tuple)
# my_tuple = 3, 4.6, "dog"
# # print(my_tuple)
# a, b, c = my_tuple
# print(a)
# print(b)
# print(c)
num_tuple = (2, 4, 5, 7, 8, 10,17,23,45,23)
# print(num_tuple[2:5])
# print(num_tuple[4:] )
# print(num_tuple[-3:] )
# print(num_tuple[2:5] )
#negative Index:
# print(num_tuple [-6:-1])
# print(num_tuple [-6])
# nested tuple
# n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
# print(n_tuple[0][3])
# print(n_tuple[1][1])
# first_names = ('Anil', 'Sarah', 'Mehta', 'Arjun')
# last_names = ('Narang', 'Smith', 'Raj', 'Gowda')
# ages = (49, 55, 39, 33)
# res = zip(first_names, last_names,ages)
# # print( res)
# # print("------------------------------------------------")
# customers = tuple(res)
# # print(customers)
# first_name, last_name, age = customers[2]
# print(first_name, last_name,   ','  , age,   'years old')
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
# Tuple_a = (1, 2)
# Tuple_b = ('x', 'y')
# Tuple_c = Tuple_a + Tuple_b
# print(Tuple_c)
# tuple_a = (1, 'x', 1, 1, 'x')
# print(tuple_a.count('x'))
# print(tuple_a.count(1))
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
# MLB_team = {
#  'Colorado' : 'Rockies',
# 'Boston'  : 'Red Sox',
#  'Minnesota': 'Twins',
#  'Milwaukee': 'Brewers',
#  'Seattle'  : 'Mariners'
#
#  }
# print(MLB_team)
# MLB_team = dict ( [
#      ('Colorado', 'Rockies'),
#      ('Boston', 'Red Sox'),
#      ('Minnesota', 'Twins'),
#      ('Milwaukee', 'Brewers'),
#      ('Seattle', 'Mariners'),
# ] )
# print(MLB_team)
# Employee = {"Name": "John", "Age": 29, "experience":4.6,"salary":25000,"Company":"GOOGLE"}
#
# print(type(Employee))
#
# print("printing Employee data .... ")
# print("Name:" ,Employee["Name"])
# print("Age : %d" %Employee["Age"])
# print("Experience %f" %Employee["experience"])
# print("Salary : %d" %Employee["salary"])
# print("Company : %s" %Employee["Company"])
# D1={}
# D1[0] = 'Peter'
# D1[2] = 'Joseph'
# D1[4] = 'Ricky'
# D1[4]='sandy'
# print("\nDictionary after adding 3 elements: ")
# print(D1)
# Dict={}
# Dict['Emp_ages'] = 20, 33, 24
# print("\nDictionary after adding 3 elements: ")
# print(Dict)
# my_dict = {'a': 10, 'b': 20, 'c': 30}
# print(my_dict.get('b'))
# d = {'a': 10, 'b': 20, 'c': 30}
# list(d.items())
# print(list(d.items())[1][0])
# print(list(d.items())[1][0])
# a=set('hello')
# print(a)
# myset = {"apple", "banana", "cherry"}
# print(len(myset))
# print(myset)
# myset.add("orange")
# print(myset)
# myset = {"apple", "banana", "cherry",}
# myset.update( ["orange", "mango", "grapes"] )
# print(myset)
# My_Set={1,'s',7.8}
# My_Set.update([2,4.6,1,'r'])
# print(My_Set)
# myset = {4, 2, 5, 1, 3}
# print(sorted(myset))
# print(myset.sort())
# set_x = set(["green", "blue"])
# set_y = set(["blue", "yellow"])
# set_z = set_x & set_y
# print(set_z)
# A = {1, 2, 3, 4, 5}
# B = {4, 5, 6, 7, 8}
# print(A - B)
# A.update([6,7])
# print(A)
# a={1, 2,5, 4.6, 7.8, 'r', 's'}
# b=frozenset(a)
# b.update([8,9])
# print(b)
# gen = ['pop', 'rock', 'jazz']
#
# # iterate over the list using index
# for i in range(len(gen)):
#     print("I like", gen[i])
# digits = [0, 1, 5]
#
# for i in digits:
#     print(i)
# else:
#     print("No items left.")
# student_name = input("Enter the student name:: ")
#
# marks = {'James': 90, 'Jules': 55, 'Arthur': 77}
#
# for student in marks:
#     if student == student_name:
#         print(marks[student])
#
# else:
#     print(' The marks of the students is displayed and no more entry to display.')
# for i in range(1, 51):
#     if(i%5==0):
#         print(i)
# else:
#     print("this is not printed because for loop is terminated because of break but not due to fail in condition")
# num = 0
#
# while num < 3:
# 	num += 1
# 	print('num = ', num)
# else:
#     print('else block executed')
import array as arr
# numbers = arr.array('i',[10,20,30])
# print(numbers)
# a=arr.array( 'd', [1.1 , 2.1 ,3.1] )
# print(a[1])
# a=arr.array('d', [1.1 , 2.1 ,3.1] )
# a.append(3.4)
# print(a)
#
# a=arr.array('d', [1.1 , 2.1 ,3.1] )
# a.extend([4.5,6.3,6.8])

# a=arr.array('d', [1.1 , 2.1 ,3.1] )
# a.insert(2,3.8)
# print(a)
# a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# c=arr.array('d')
# c=a+b
# print("Array c = ",c)
# a=arr.array('d',[1.1 , 2.1 ,3.1,2.6,7.8])
# a.reverse()
# print(a)
# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
#
# T.insert(2, [0,5,11,13,6])
#
# for r in T:
#    for c in r:
#       print(c,end = " ")
#    print()
from numpy import reshape,arange,ones,zeros,eye
# a = ones((3, 4), float)
# print(a)
# b =eye(3,dtype=int)
# print(b)
# a=[1,2,3,4,5,6]
# b=reshape(a,(2,3))
# print(b)
# even = [1, 3, 5]
# even.append( [7,8,9] )
# print(even)
# even.extend([9, 11, 13])
# print(even)
# Deleting list items
my_list = ['p', 'r', 'o', 'b', 'l', 'e', 'm']
# delete one item through index
my_list.insert(1,5)
print(my_list)




