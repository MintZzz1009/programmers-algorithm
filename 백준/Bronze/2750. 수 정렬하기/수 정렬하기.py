# 입력
n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)


# solution
for _ in range(n):
    for i in range(n - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]


# 출력
for num in numbers:
    print(num)
