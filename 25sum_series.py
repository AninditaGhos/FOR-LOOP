#Write a program to find the sum of following series
#1 + 8 + 27 …………n terms
a=0
n=int(input("Enter the numbere "))
for x in range (1,n+1):
    a=a+x**3
print(a)