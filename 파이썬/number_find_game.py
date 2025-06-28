import random
print("숫자를 맞춰보세요(1 ~ 100)")

num = random.randint(1, 100)

while True:  
    input_num = int(input())  
    if input_num < 1 or input_num > 100:
        print("1부터 100 사이의 숫자를 입력해주세요.")
    elif input_num < num:
        print("숫자가 너무 작습니다.")
    elif input_num > num:
        print("숫자가 너무 큽니다.")
    else:
        print(f"정답입니다. 입력한 숫자는 {input_num}입니다.")
        break
