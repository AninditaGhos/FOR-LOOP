#Write a program to accept 10 numbers from the user and display it’s average
b=int(input("Enter the number "))
a=0
for x in range(1,b+1):
    num=int(input("Enter the number "))
    a=a+x
average=a/10
print(average)