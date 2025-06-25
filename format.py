print('%s %s' % ('one','two'))
print('{} {}'.format('one','two'))

number = 3
name = "apple"

print("i eat %d apple" % number)

print("i eat %5d %s" % (number,name))


#f-string 방법
print(f"i eat {number:5} {name}")
# 왼쪽 정렬 
print(f"i eat {number:<5} {name}")
#별표 채우기
print(f"i eat {number:*<5} {name}")
print(f"i eat {number:*>5} {name}")
# 가운데 정렬
print(f"i eat {number:^5} {name}")