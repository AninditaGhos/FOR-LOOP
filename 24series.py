#Write a program to print the following series till n terms.1 4 9 16 25 _ _ _ _ _ n terms
n=int(input("Enter the number "))
for x in  range(1,n+1):
    print(x*x,end=" ")