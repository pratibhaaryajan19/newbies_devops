from collections import Counter
s1=[]
n=int(input("Number of elements: "))
for i in range(0,n):
    m=(int(input()))
    s1.append(m)
s2=Counter(s1)
print(s2)
k=0
if n==1:
    print("1")
else:
    for i in s1:
        if(s1[i]==1):
            k=k+1
    print(k)
