t=int(raw_input())
count=0
n=map(int,raw_input().split())
for i in range (0,t):
    if (n[i] < 300000000):
        count+=1
print count
