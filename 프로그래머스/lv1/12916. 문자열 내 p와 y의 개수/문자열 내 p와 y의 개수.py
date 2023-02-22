def solution(s):
    p_count, y_count = 0, 0
    for char in s:
        if char == 'p' or char =='P':
            p_count += 1
        elif char == 'y' or char =='Y':
            y_count += 1
    return p_count == y_count
        