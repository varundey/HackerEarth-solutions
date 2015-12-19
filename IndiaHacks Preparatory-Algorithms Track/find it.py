n=input()
l=map(int,raw_input().split())
m=input()
x=map(int,raw_input().split())
d1={}
d2={}
for j in x:
    d1[j]=0
    try:
        d2[j]+=1
    except KeyError:
        d2[j]=1
for i in l:
    try:
        d1[i]+=1
    except KeyError:
        d1[i]=1
ans=[]
for i in d2:
    if d2[i]>d1[i]:
        ans.append(i)
ans=sorted(ans)
for i in ans:
    print i,
print
