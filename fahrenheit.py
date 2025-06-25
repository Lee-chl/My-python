print("본 프로그램은 섭씨를 화씨로 변환해주는 프로그램입니다.")
print("변환하고 싶은 섭씨 온도를 입력하세요.")

celisius = float(input())
fahrenheit = ((9/5) * celisius) + 32

print(f"섭씨 온도: {celisius:.3f}")
print(f"화씨 온도: {fahrenheit:.3f}")
