data = ([1,2],[3,4],[5,6])
for value in zip(*data): #시퀀스 데이터 언 패킹은 *로
    print(value)  # (1, 3, 5) (2, 4, 6) 언패킹해서 출력

#dict 언패킹은 **로
data = {"b": 2, "a": 1, "c": 3}
print({**data})  # {'b': 2, 'a': 1, 'c': 3}