ex= [1,2,3,4,5]
print([value**2 if value %2 == 0 else value for value in ex])

# reduce ex map 과 달리 list에 똑같은 함수 적용해서 통합
from functools import reduce
reduce_ex = [1,2,3,4,5]
print(reduce(lambda x, y: x + y, reduce_ex))  # 15