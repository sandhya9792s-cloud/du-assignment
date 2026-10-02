#write into a file.
def main():
    city=['jaipur','mumbai','delhi']
    f1=open('cities.txt','r')
    s1=f1.readlines()
    f1.close()
print()

#list chompriesion.
a=[1,2,3,4,5]
b=[]
for val in a:
    b.append(val*val)
print(b)

a=[1,2,3,4,5]
b=[val*val for val in a]
print(b)

a=[1,2,3,4,5]
res=[val for val in b if val>10]
print(res)
