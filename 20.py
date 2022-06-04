#Write a python program to sum the sequence:
#1 + 1/1! + 1/2! + 1/3! + …….. + 1/n!
n=int(input("Enter the number "))
a=1
print(a,end=" + ")
for i in range(1,n):
    print(a,"/",i,"!",end=" + ")