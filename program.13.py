str1=input("Enter a string:")
str2=''
index=-1
for i in str1:
    str2+=str1[index]
    index-=1
print("The given string={}\n The Reversed string ={}".format(str1,str2))
if(str1==str2):
    print("Hence,the given string is Palindrome")
else:
    print("Hence, the given is not a palindrome")



A=input("Enter leap year or year:")
if A=="year":
    print("A year has 365 days.")
elif A=="leap year":
    print ("A leap year has 366 days.")
else:
    print("Enter leap year or year")




str1='*'
i=5
while i>=1:
    print(str1*i)
    i-=1
