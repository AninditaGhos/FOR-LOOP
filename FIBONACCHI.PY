num=int(input("enter no"))
j=1
k=0
for i in range (0,num+1):
    i=j
    j=k
    print(k,end=",")
    k=i+j 
    