def fact(n,b):
    ans=0
    for s in range (n,b+1):
        ans+=s
    return ans

n=int(input())
b=int(input())
for z in range(n,b):
    print(n,'+',b,fact(n,b))
