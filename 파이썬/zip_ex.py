alist = [1, 2, 3]
blist = [4, 5, 6]

print([[a,b] for a,b in zip(alist, blist)])  # [[1, 4], [2, 5], [3, 6]] 
# zip은 두 개의 리스트를 묶어줌
print([c for c in zip(alist, blist)]) #튜플 타입으로 묶어주는 법

for i, values in enumerate(zip(alist, blist)):
    print(i, values)  # 0 [1, 4] 1 [2, 5] 2 [3, 6] 인덱스 번호와 함께 출력  