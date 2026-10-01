#WAP to take input no. from the user till the user inter 0 and add all the no.
sum=0
num=int(input("enter a number:"))
while num!=0:
    sum=sum+num
    num=int(input("enter a number"))
print("sum=",sum)
