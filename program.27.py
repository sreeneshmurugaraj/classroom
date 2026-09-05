n=int(input("Enter a value for n:"))
sum = 0
counter=1
while counter<=n:
    sum = sum + counter
    counter+=1
print("Sum of 1 until %d: %d" % (n,sum))



name = "Rajarajan"
mark = 98
print ("Name: %s and Marks: %d" %(name,mark))




MySubjects = ['Tamil', 'Hindi', 'Telugu', 'Maths']
print (MySubjects)
['Tamil', 'Hindi', 'Telugu', 'Maths']
del MySubjects[1]
print (MySubjects)
['Tamil', 'Telugu', 'Maths']





del MySubjects[1:3]
print(MySubjects)
['Tamil']



