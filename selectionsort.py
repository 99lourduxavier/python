s=list(map(int,input().split()))
l=len(s)
for i in range(l):
    for j in range(i+1,l):
        if(s[i]>s[j]):
            s[i],s[j]=s[j],s[i]
print(*s)            
