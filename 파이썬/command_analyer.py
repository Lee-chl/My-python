import csv

def getKey(item): #정렬을 위한 함수
    return item[1]

command_data = [] # 파일 읽어오기

with open("command_data.csv", "r",encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile,delimiter=',',quotechar='"')
    for row in reader:
        command_data.append(row)

command_counter = {} # dict 생성, 아이디를 key값, 입력줄 수를 value값
for data in command_data: # list 데이터를 dict로 변경
    if data[1] in command_counter.keys(): # 아이디가 이미 key값으로 변경되었을 때 
        command_counter[data[1]] += 1 # 기존 출현한 아이디
    else:
        command_counter[data[1]] = 1 # 처음 나온 아이디

dictlist = [] #dict를 list로 변경
for key, value in command_counter.items():
    temp = {key,value}
    dictlist.append(temp)

sorted_dict = sorted(dictlist, key=getKey, reverse=True) # 리스트를 입력 줄 수로 정렬
print(sorted_dict[:100]) # 상위 100개만 출력

#Count 사용하면 더 간단하게 작성 가능
# from collections import Counter   
# sorted(Counter(command_data).items(), key=lambda x: x[1], reverse=True)