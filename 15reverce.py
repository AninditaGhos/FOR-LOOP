#write a program to reverse the number accepted from the user.
num=input("Enter the number ")
rev=""
i=0
for i in  range(len(num),0,-1):
    rev=rev+num[i-1]
print(rev)
