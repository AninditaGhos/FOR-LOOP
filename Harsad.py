n=input("enter no")
b=len(n)
i=0
sum=0
while i<b:
    d=int(n[i])
    sum=sum+d
    i=i+1
print(sum)
if int(n)%sum==0:
    print("it is harshad no")
else:
    print("not harshad no")        