#세수 중에서 가장 큰수와 가장 작은 수를 찾는 함수를 포함한 프로그램을 작성하시오.
#6가지종류


def f(a,b,c):
    return(w(a,b,c),g(a,b,c))

def w(a,b,c):
    if a>b>c:
        return a
    elif a>c>b:
        return a
    elif b>c>a:
        return b
    elif b>a>c:
        return b
    elif c>b>a:
        return c
    elif c>a>b:
        return c

def g(a,b,c):
    if a<b<c:
        return a
    elif a<c<b:
        return a
    elif b<c<a:
        return b
    elif b<a<c:
        return b
    elif c<b<a:
        return c
    elif c<a<b:
        return c

print(f(1,2,3))
print(f(1,3,2))
print(f(2,1,3))
print(f(2,3,1))
print(f(3,1,2))
print(f(3,2,1))
