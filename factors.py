from re import I


n=int(input("enter no"))
perfect_no=0
for i in range(1,n):
    if n%i==0:
        perfect_no=perfect_no+i
print("perfect_no")
if perfect_no==n:
    print("perfect_no")
else:
    print("not perfect_no")            