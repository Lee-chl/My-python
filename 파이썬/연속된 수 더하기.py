a=int(input())
b=int(input())
def hap(a,b):
      ans=0
      if a<b:
            for s in range(a,b+1):
                  ans+=s
            return ans
      elif a>b:
            for s in range(b,a+1):
                  ans+=s
            return ans
      else:
            return a

for b in range(a,b+1):
      print(b,'+',end='')
print('=',hap(a,b))


