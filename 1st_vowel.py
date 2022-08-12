num=input("Enter the name ")
i=0
a="A","E","I","O","U","a","e","i","o","u"
while i<len(num):
    if num[i] in  a:
        print(num[i])
    i+=1
J=0
while J<len(num):
    if num[J] not in a:
        print(num[J])
    J+=1