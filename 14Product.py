#Write a program to find to product of the digits of a number accepted from the user.
num=input("ENter the number ")
product=1
for x in (num):
    product=product*int(x)
print(product)