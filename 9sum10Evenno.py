#write a program to print a sum of 10 Even numbers.
sum=0
for x in range(1,21):
    if x%2==0:
        sum=sum+x
print(sum)