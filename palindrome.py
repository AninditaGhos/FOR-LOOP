n=input("enter no")
sum=""
for i in range (-1,0-len(n)-1,-1):
    k=n[i]
    sum=sum+k
print(sum)
if sum==n:
    print("Palindrome")
else:
    print("Not a palindrome")