import re
# message="I like Football"
# x=re.search("F",message)
# print(x.start())
# #find all
# message="Hagi is a perfect footballer.Hagi is from romania"
# y=re.findall("Hagi",message)
# print(y)
#split()
# message="I like footbal Basketball volleyball"
# x=re.split("\s",message,2)
# print(x)
#sub
# message="I like Football and cricket"
# x=re.sub("\s","-",message)
# print(x)
# y=re.sub("\s","-",message,1)#here from 1 position there will be no - means after 2 word there is no - based on 0 index
# print(y)
# pattern="python"
# text="I write code in python"
# match=re.search(pattern,text)
# print("Match found",bool(match))

# pattern="a"
# text="I love to code in python and it's amazing!"
# matches=re.findall(pattern,text)
# print("matches found",len(matches))

# pattern="\s"
# text="I like python and it's amazing!"
# matches=re.split(pattern,text)
# print("split.text:",matches)

# pattern="python"
# replacement="java"
# text="python is fun"
# substituted_text=re.sub(pattern,replacement,text)
# print("substituted text:",substituted_text)

#using * to match zero or more occurences of a character
#here py. here . means any 1 character
# pattern="py.*n"
# count=0
# text=["python coding","pyt3on","java","pyt40n","py@#n","pyn"]
# for i in text:
#     if(re.findall(pattern,i)):
#         count+=1
# print("matches found",count)

#using + to match one or more occurences of a character
# pattern="py.+n"
# count=0
# text=["python coding","pyt3on","java","pyt40n","py@#n","pyn"]
# for i in text:
#     if(re.findall(pattern,i)):
#         count+=1
# print("matches found",count)

# #using ? to match zero or one occurences of a character
# pattern="py.?n"
# count=0
# text=["python coding","pyt3on","java","pyt45n","py@#n","pyn","pynn"]
# for i in text:
#     if(re.findall(pattern,i)):
#         count+=1
# print("matches found",count)
#using [] to create a character set
#here it matchesh within squre brcaket
# pattern="[Pp]ython"
# text="i write code in python and python!"
# matches=re.findall(pattern,text)
# print("matches found:",len(matches))

#using {}to specify the number of occurences of a character
# pattern="py{1,2}n"
# text="I love pyn, pyyn, and pyyyn!"
# matches= re.findall(pattern,text)
# print("matches found:",len(matches))

# using \d to match digits
# pattern="\d+"
# text="My phone number is 123-456-7890."
# matches=re.findall(pattern,text)
# print(matches)
# print("matches found",len(matches))

#using w to match alphanumeric characters
#due to space it splits here it counts character i_love and python so 2
# pattern="\w+"
# text="I_love_  python!"
# matches=re.findall(pattern,text)
# print(matches)
# print("matches found",len(matches))

# using \s to match whitesapce characters
# pattern="\s+"
# text="i love python"
# matches=re.findall(pattern,text)
# print("matches found:",len(matches))

#using | as an OR operator#number of matches python or java
# pattern="python|java"
# text="I write code in python and java!"
# matches=re.findall(pattern,text)
# print("matches found",len(matches))

# using() to group patterns to group separately
# pattern="(\d{3})-(\d{3})-(\d{3})"
# text="my phone number is 123-456-7890."
# match=re.search(pattern,text)
# if match:
#     print("area code",match.group(1))
#     print("Local Exchange", match.group(2))
#     print("Line number", match.group(3))

# import glob
# print(glob.glob('*.py'))