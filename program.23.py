a=int(input("enter a number:"));
if a%2==0:
    print("Its a Even number");
elif a%2:
     print("Its a odd number");
else:
    print("Give a real number");
isPrime='Y';
if a<=1:
    print("not valid number to check");
else:
    for i in range(2,a):
        if a%i==0:
            isPrime='N';
if isPrime=='N':
    print("Its NOT a prime number");
else:
    print("Its a prime number");

    
