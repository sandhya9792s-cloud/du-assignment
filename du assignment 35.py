#count the no. of times 't' or'T' apperes in string.
def main():
    count=0
    name=input("enter string")
    for ch in name:
        if ch=='t' or ch=='T':
            count=count+1
    print("no. of counts",count)
    
    