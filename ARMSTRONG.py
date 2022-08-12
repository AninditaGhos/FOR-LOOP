n=input("enter no")
b=len(n)
sum=0
for i in range (0,b):
    k=int(n[i])**b
    sum=sum+k
print(sum)
if sum==int(n):
    print("Aramstorng")
else:
    print("not Ararmstorng")    
