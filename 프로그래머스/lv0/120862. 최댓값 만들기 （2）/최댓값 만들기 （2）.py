def solution(numbers):
    answer = []
    for n in numbers:
        numbers.remove(n)
        for m in numbers:
            answer.append(n * m)
    return max(answer)