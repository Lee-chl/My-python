print("당신이 태어난 년도를 입력하세요")
brith_year = int(input())
age = 2025 - brith_year + 1
message = ""

if age < 26 and age > 19:
    message = "대학생"
elif age < 20 and age > 16:
    message = "고등학생"
elif age < 17 and age > 13:
    message = "중학생"
elif age < 14 and age > 7:
    message = "초등학생"
else:
    message = "학생이 아닙니다."

print(message)