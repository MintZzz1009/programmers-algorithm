def solution(n):
    answer = 0
    for x in range(int(n ** 0.5) + 1):
        answer = -1
        if x ** 2 == n:
            answer = (x + 1) ** 2
            
    return answer