#Write a program to display sum of odd numbers and even numbers separately that 
# fall between two numbers accepted from the user.(including both numbers) 100 and 500.
A=int(input("Enter the  number "))
B=int(input("Enter the  number "))
a=0
b=0
for x in range(A,B+1):
    if x%2==0:
        a=a+x
    elif x%2!=0:
        b=b+x
print(a)
print(b)