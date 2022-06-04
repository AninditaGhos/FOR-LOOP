#Write a program to display all even numbers that fall between two numbers
# (exclusive both numbers) entered by user.
num=int(input("ENter the number "))
num1=int(input("Enter the number "))
for x in range(num,num1+1,2):
    print(x)