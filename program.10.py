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







str1=input("Enter a string: ")
str2="aAeEiIoOuU"
v,c=0,0
for i in str1:
    if i in str2:
        v+=1
    elif i.isalpha():
        c+=1
        print ("The given string contains { } vowels and { } consonants",format(v,c))
