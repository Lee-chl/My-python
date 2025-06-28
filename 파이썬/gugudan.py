num = 1

while num !=0:
    print("구구단 몇 단을 게산할까요?? [0 입력 시 종료]")
    num = int(input())

    if num == 0:
        print("구구단 계산을 종료합니다.")
        break
    elif num < 1 or num > 9: 
        print("0단 부터 9단까지의 구구단만 계산할수 있습니다.")
        continue

    print(f"{num}단을 계산합니다.")
    for i in range(1,10):
        result = num * i
        print(f"{num} X {i} = {result}")
