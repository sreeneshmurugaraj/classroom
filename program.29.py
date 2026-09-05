def printnames (*name):
    for n in name:
        print(n)
    return
# now invoking the printnos() function
print ('Printing two values')
printnames ('sreenesh','sreepadh')
print ('Printing three values')
printnames ('raj','kala','grandparents')





sum = lambda arg1, arg2: arg1 + arg2
a=int(input("enter a number:"))
b=int(input("enter a number:"))
print ('The Sum is :', sum(a,b))
print ('The Sum is :', sum(-30,40))
