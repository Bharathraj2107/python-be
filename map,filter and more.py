# lst=['kousalya','bhavitha','bhuvan','namitha']
# lst_upper_case=list(map(str.upper,lst))
# print(lst_upper_case)
# circle_areas=[3.56,5.57,4.009,5.624,9.01344,3.2001]
# res=list(map(round,circle_areas,range(2,7)))
# print(res)
# strings=['a','b','c','d','e']
# numbers=[1,2,3,4,5]
# res=list(zip(strings,numbers))
# print(res)
# marks=[45,66,70,34,68,74,23,90,86]
# def sort_marks(marks):
#     return marks>70
# res=list(filter(sort_marks,marks))
# print(res)
# wrds=['hgflkjh','madam','mom','radar','mnbv']
# palindrome=list(filter(lambda word:word==word[::-1],wrds))
# print(palindrome)

# double of each numbers using map
# numbers=[1,2,3,4,5]
# double_numbers=list(map(lambda x:x*2,numbers))
# print(double_numbers)
from functools import reduce
# numbers=[1,2,3,4,5]
# def custom_sum(first,second):
#     return first+second
# result=reduce(custom_sum,numbers)
# print(result)
# numbers=[1,2,3,4,5]
# total=reduce(lambda x,y:x+y,numbers)
# print(total)
numbers=[1,7,3,9,5]
max_number=reduce(lambda x,y:x if x>y else y,numbers)
print(max_number)