#Write a program to print a factorial a number accepted by user.
num=int(input("Enter the number"))
factorial=1
for x in range(1,num+1):
    factorial=factorial*(x)
print(factorial)