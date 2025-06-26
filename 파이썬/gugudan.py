print("구구단 몇 단을 게산할까요??")
num = int(input())
print(f"{num}단을 계산합니다.")

for i in range(1,10):
    result = num * i
    print(f"{num} X {i} = {result}")