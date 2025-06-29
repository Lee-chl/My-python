import pprint


result = [i for i in range(10) if i % 2 == 0] #if해서 조건문 넣어서 사용 가능 (필터)
print(result)

word_1 = "teamlab"
word_2 = "technology"
result = [i+j for i in word_1 for j in word_2] # for i in word_1: for j in word_2: j가 i에 append()
pprint.pprint(result)

words = "The quick brown fox jumps over the lazy dog".split()
pprint.pprint([[w.upper(), w.lower(), len(w)] for w in words]) #[[]] 하면 ]요 부분이 먼저 실행]