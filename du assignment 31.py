for i in range(3):
    print(i)

    for i in "Umbrella":
        print(i)
#WAPto check whether the word contain 'e' or not.
word=input("enter the word")
for i in word:
    if i=='e' or i=='E':
        print("word has e")
        break
#for word count.
total=0
for line in open('words.txt'):
    word=line.strip()
    print(word)
    total=total+1
print("no. of words",total)

