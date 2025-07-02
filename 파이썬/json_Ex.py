import json

with open("json_ex.json","r",encoding="utf-8") as f:  # json 파일을 읽기 모드로 열기
    contents = f.read()  # 파일의 내용을 읽어오기
    json_data = json.loads(contents)  # JSON 문자열을 파이썬 객체로 변환

print("JSON Data:", json_data)  # JSON 데이터 출력
for employee in json_data['employees']:  # employees 키에 해당하는 리스트를 순회
    print(employee)

#쓰기
dict_data = {'firstName':'Zara', 'lastName':'Smith', 'age':30, 'city':'New York'}
with open("jsonex.json","w") as f:
    json.dump(dict_data,f)