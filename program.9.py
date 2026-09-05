A=int(input("Enter a number for A:"))
if A%2==0:
    print("A is Even")
else:
    print("Give a real number or it is odd")



A=int(input("Enter a number for A:"))
B=int(input("Enter a number for B:"))
C=int(input("Enter a number for C:"))
if A<B and A<C:
    print("A is the smallest number")
elif B<A and B<C:
    print("B is the smallest number")
elif C<A and C<B:
    print("C is the smallest number")
else:
    print("Give three diffrent numbers")
