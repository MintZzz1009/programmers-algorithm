def solution(x):
    answer = False
    sum_x = sum([int(num) for num in list(str(x))])
    if x % sum_x == 0:
        answer = True
    return answer