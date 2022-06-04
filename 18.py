#Write a program to add first n terms of the following series using a while loop :
# 1/1! + 1/2! + 1/3! + …….. + 1/n!
n=int(input("Enter the number "))
a=1
for i in range(1,n):
    print(a,"/",i,"!",end=" + ")