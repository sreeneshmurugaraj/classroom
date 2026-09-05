A=int(input("Enter a value for A:"))
B=int(input("Enter a value for B:"))
if A and B:
    print(B,A)









num = int(input("Enter a number: "))

reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10
print("Reversed number:", reverse)
