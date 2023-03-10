def solution(a, b):
    answer = 0
    
    if a - b < 0:
        start, end = a, b 
    else: start, end = b, a
        
    for num in range(start, end + 1):
        answer += num
    return answer