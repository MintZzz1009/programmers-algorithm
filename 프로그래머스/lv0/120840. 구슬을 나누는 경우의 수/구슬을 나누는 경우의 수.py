def solution(balls, share):
    # 5(5-0) 4(5-1) 3(5-2)
    # 3(1+2) 2(1+1) 1(1+0)
    up, down = 1, 1
    for i in range(share):
        up *= balls - i
        down *= 1 + i
    answer = up / down
    return answer