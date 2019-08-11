a=int(input('평소점수는?'))
b=int(input('중간점수는?'))
c=int(input('기말점수는?'))

d=a+b+c
d<=100


if d>=90:
    print('총점은',d,'학점은','A')
elif d>=80:
    print('총점은',d,'학점은','B')
elif d>=70:
    print('총점은',d,'학점은','C')
elif d>=60:
    print('총점은',d,'학점은','D')
else:
    print('총점은',d,'학점은','F')
