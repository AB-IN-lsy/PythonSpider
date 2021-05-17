cnt=0
n,m=map(int,input().split())
for i in range(pow(10, n-1),pow(10,n)):
    lst=list(str(i))
    lst=[int(j) for j in lst]
    ans=sum(lst)
    if ans==m:
        cnt+=i
print(cnt)