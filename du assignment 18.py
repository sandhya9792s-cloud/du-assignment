def prime(n):
    if n<=1 :
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
num=int(input("enter a num:"))
if prime(num):
    print("prime number")
else:
    print("not a prime number")