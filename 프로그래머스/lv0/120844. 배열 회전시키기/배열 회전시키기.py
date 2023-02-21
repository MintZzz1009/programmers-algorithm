def solution(numbers, direction):
    answer = []
    if direction == 'right':
        # last = numbers.pop()
        # numbers.insert(0, last)
        last = [numbers[-1]]
        rest = numbers[:-1]
        answer = last + rest
    else:
        # first = numbers.pop(0)
        # numbers.append(first)
        first = [numbers[0]]
        rest = numbers[1:]
        answer = rest + first
    return answer