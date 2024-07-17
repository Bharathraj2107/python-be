import array as arr
#numbers=arr.array('i',[10,20,30,40,50])
#print(numbers)
#print("------------------------------------")
# for x in numbers:
#   print(x)
# a=arr.array('d', [1.1,2.1,3.1] )
# print(a[1])
# a=arr.array('d', [1.1,2.1,3.1] )
# print(len(a))
# a=arr.array('d', [1.1,2.1,3.1] )
# a.append(3.4)
# print(a)
# a.extend([4.5,6.3,6.8])
# print(a)
# a=arr.array('d',[1.1,2.1,3,1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# a.insert(1,3.8)
# print(a)
#in one dimensional array + will concatinate
# a=arr.array('d',[1.1,2.1,3,1,2.6,7.8])
# b=arr.array('d',[3.7,8.6])
# c=arr.array('d')
# c=a+b
# print("array c=",c)
#find the sum of all array elements
# sum=0
# a=arr.array('i',[1,2,3,4,5])
# for x in a:
#     sum+=x
# print(sum)
# for i in a:
#      c+=i
# print(c)
#reverse an aray
# a=arr.array('i',[1,2,3,4,5])
# print(a[::-1])
#even number and sum
# sum=0
# a=arr.array('i',[1,2,3,4,5,6])
# for x in a:
#     if x%2==0:
#         sum+=x
# print(sum)
#alicing to an array
# a=arr.array('i',[1,2,3,4,5,6])
# print(a[1:3])
# a=arr.array('i',[9,2,3,4,5,6])
# a.remove(9)
# print(a)
# a=arr.array('i',[2,3,4,5,6])
# for s in a:
#     st=s*s
#     print("square",st)
#     cu = s * s * s
# print("cubes",cu)
a=arr.array('i',[2,3,4,5,6])
max=a[0]
min=a[0]
for x in a:
    if x>max:
        max = x
    if x< min:
        min=x
print("the largest is ",max)
print("the smallest is ",min)
# min=min(a)
# print(min)
# max=max(a)
# print(max)
