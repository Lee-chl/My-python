def spam(eggs: list[int]) -> None:  # 타입 힌트 적용
    """_summary_

    Args:
        eggs (list[int]): 리스트 타입의 eggs 매개변수
    """
    eggs.append(1)  # 기존 객체에 1 추가
    eggs.append(5)  # 기존 객체에 5 추가
    eggs = [2, 3]  # 새로운 객체 생성
    print(eggs)


ham = [0]
spam(ham)
print(ham)
