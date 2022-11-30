# Q1.
numbers = [1,2,3,4,5,6]
print('::'.join(map(str, numbers)))


# Q2.
numbers = list(range(1, 10 + 1))
print("# 홀수만 추출하기")
print(list(filter(lambda n: n % 2 == 1, numbers)))

print("# 3이상, 7 미만 추출하기")
print(list(filter(lambda n: n >=3 and n < 7, numbers)))

print("# 제곱해서 50 미만 추출하기")
print(list(filter(lambda n: n ** 2 < 50, numbers)))

