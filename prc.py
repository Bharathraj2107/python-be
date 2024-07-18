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
# print(num_tuple[:3] )
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






