#Write a program to print the following series till n terms.
#2 , 22 , 222 , 2222 _ _ _ _ _ n terms
num=int(input("Enter the number "))
for x in range(1,num+1):
    print("2"*x,end=" , ")