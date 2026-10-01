#reversive funtion.
def fact(n):
    if n==1:
        return 1
    else:
        fact=n*fact(n-1)
n=int(input("enter no."))
print("the fectorial of",fact(n))
