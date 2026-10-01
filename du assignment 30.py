#WAP to calculate GCD of two numbers.
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
GCD=1
smaller=0
if num1<num2:
    smaller=num1
else:
    smaller=num2
for i in range(1,smaller+1):
    if num1%i==0 and num2% i==0:
        GCD=i
print("GCD of two entered no. is", GCD)