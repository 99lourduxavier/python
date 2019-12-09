s=list(map(int,input().split()))
l=len(s)-1
for i in range(0,l):
    for j in range(l-i):
        if(s[j]>s[j+1]):
            s[j],s[j+1]=s[j+1],s[j]
print(*s)            
