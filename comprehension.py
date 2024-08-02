# city1=["paris","london","berlin","Tokyo","sydney"]
# city2=[]
# city2=[x for x in city1]
# print(city2)
# numbers=[1,2,3,4,5,6,7,8,9,10]
# even_no=[]
# even_no=[i for i in numbers if i%2==0]
# print(even_no)
# list1=['q','a','t','d','a','f','e']
# list2=['a','e','i','o','u']
# result=[i for i in list1 for j in list2 if i==j]
# print(result)
# words=["filtering","words","based","on","length"]
# five_lttr=[word for word in words if len(word)==5]
# print(five_lttr)
# my_fruit=['apple','banana','orange','mango']
# my_fruit2=[i[0] for i in my_fruit]
# print(my_fruit2)
# mixed_list=['apple','banana',12,15,7,2,3,'orange','mango']
# #if type is equal to int then append square of the number
# #othwersie append first character of string
# mixed_list2=[i**2 if type(i)==int else i[0] for i in mixed_list]
# print(mixed_list2)
#using list comprehension with functions
# def power(x):
#     return x**2
# p_num=[]
#
# for x in range(1,10):
#     p_num.append(power(x))
# print(p_num)
#with compression
# def power(x):
#     return x**2
# p_num=[power(x) for x in range(1,10)]
# print(p_num)
# nested list compression
# res=[(x,y) for x in [1,2,3] for y in[3,1,4] if x!=y]
# print(res)
# nstd
# nstd=[[1,2],[3,4],[5,6]]
# elements=[element for pair in nstd for element in pair]
# print(elements)
# list1=[1,2,3]
# list2=["a","b","c"]
# pairs=[(x,y) for x in list1 for y in list2]
# print(pairs)

# list1=[1,2,3,4,5]
# list2=[3,4,5,6,7]
# setel=set((x,y) for x in list1  for y in list2 if x==y)
# print(setel)
list1=["abc","def","ghi"]
list2=["jkl","mno","pqr"]
# def sumindex(list1,list2):
#     for x in list1:
#      for y in list2:
#         print(list1.index(x)+list2.index(y))
# sum_ind=(sumindex(list1,list2))
# print(sum_ind)

# sum_ind=[list1.index(x)+list2.index(y) for x in list1 for y in list2]
# print(sum_ind)

# merge=[ (x,y)for x in list1 for y in list2]
# print(merge)
# def fact(n):
#     if n==1:
#         return 1
#     else:
#       return n*fact(n-1)
#
# f_num=[fact(n) for n in range(1,11)]
# print(f_num)

# binary_num=[bin(n) for n in range(1,11)]
# print(binary_num)
# list1=[3,6,9]
# list2=[5,10,15]
# list3=[(x,y) for x in list1 for y in list2 if x!=y]
# print(list3)
# print("set compression")
# words=['apple','banana','cherry','pmpkn','']
# vowels={'a','e','i','o','u'}
# vowel_words={word for word in words if any(letter in vowels for letter in word)}
# # print(vowel_words)
# mylist=[1,2,3,4,5,6,7,8,9,10]
# newset={element*3 for element in mylist}
# print("The existing list is ",mylist)
# print("the newly created is set is",newset)

# myset={1,2,3,4,5,6,7,8,9,10}
# newset={element **2 for element in myset}
# print("The existing list is ",myset)
# print("the newly created is set is",newset)

# fear="the only thing we have to fear is fear itself"
# res=len({w for w in fear.split() if 't' not in w})
# print(res)

# set of reversed strings from another set
# words={"apple","banana","cherry"}
# reversed_words={word[::-1] for word in words}
# print(words)
# print(reversed_words)

# to get only digits from the string
# string="12345Hello67890"
# digits={char for char in string if char.isdigit()}
# print(digits)

# numbers=[1,2,3,4,5]
# squared_numbers={x**2 for x in numbers}
# print(squared_numbers)

# def is_primr(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# prime_numbers={x for x in range(1,52) if is_primr(x)}
# print(prime_numbers)
#set of even numbers and squares and odd numbers cubed from 1 to 10
# result={x**2 if x%2==0 else x**3 for x in range(1,11)}
# print(result)
#
# # set of unique numbers from a list
# numbers=[1,2,3,2,4,5,1]
# unique_numbers={x for x in numbers}
# print(numbers)
# print(unique_numbers)

#set of square roots from a set of numbers
# import math
# num={1,4,9,16,25}
# num_sqrt={math.sqrt(x) for x in num}
# print(num)
# print(num_sqrt)

# print("dictionary")
# #dictionary of squares of numbers from 1 to 10
# squares={x:x**2 for x in range(1,11)}
# print(squares)

#dictionary of even numbes as keys and their squares as values
# even_squared={x:x**2 for x in range(0,21) if x%2==0}
# print(even_squared)

#dictionary of words and their lenghts from a sentence
# words="python is awesome"
# word_lengths={word:len(word) for word in words.split()}
# print(word_lengths)
#dictionary of numbers and their cubes
# numbers=[1,2,3,4,5]
# cubes={x:x**3 for x in numbers}
# print(cubes)

#dictionary of numbers and their prime values
# def is_prime(n):
#     if n<=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#     return True
# numbers=[1,2,3,4,5,6,7,8,9,10]
# print_status={x:is_prime(x) for x in numbers}
# print(print_status)

#dictionary of words and the count of vowels from a list of strings
# words=['apple','banana','cherry']
# vowel_counts={word:sum(1 for char in word if char.lower() in 'aeiou') for word in words}
# print(vowel_counts)

#dictionary of words and there reversed form
# words=['apple','banana','cherry']
# reversed_words={word:word[::-1] for word in words}
# print(reversed_words)

#create a dictionary of numbers and their parity even or odd
# numbers=[1,2,3,4,5,6,7,8,9,10]
# pair_num={x:'even' if x%2==0 else 'odd' for x in numbers}
# print(pair_num)

#create a dictionary of numbers and their factorials
# import math
# numbers=[1,2,3,4,5]
# factorials={x:math.factorial(x) for x in numbers}
# print(factorials)
