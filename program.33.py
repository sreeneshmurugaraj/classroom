Myclass=['Raj','Sreenesh','sreepadh','Kala']
for i in range(len(Myclass)):
    print(Myclass[i])
A=int(input("Enter a number:"))
if A < (len(Myclass))and A > 0:
    print(Myclass[A-1])
else:
    print("wrong number")
