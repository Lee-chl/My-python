def findmm(a,b,c):
    max=min=a
    if max<b:
        max=b
    elif min>b:
        min=b
    if max<c:
        max=c
    elif min>c:
        min=c
    return max,min

s=int(input())
t=int(input())
w=int(input())
x,y =findmm(s,t,w)
print("최대값=",x)
print("최소값=",y)
