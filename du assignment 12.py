#WAP for series 1-2+3-4+5____-10.
sum=0
for i in range(1,11,1):
    if i%2==0:
        sum=sum-i
    else:
        sum=sum+i
print("sum=",sum)
