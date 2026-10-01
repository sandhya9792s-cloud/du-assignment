def square(a):
    return a**2
n=int(input("enter a value of n"))
sum=0
for i in range(1,n+1,1):
    sum=sum+square(i)
print("the sum of series",sum)