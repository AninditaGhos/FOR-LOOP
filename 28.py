#Accept two numbers from the user and display sum of even numbers between them(including both)
num=int(input("Enter the number "))
num1=int(input("Enter the number "))
sum=0
for x in range(num,num1+1):
    if x%2==0:
        sum=sum+x
print(sum)