import heapq

def solution(s):
    answer = ''
    parse_number_list = list(map(int, s.split()))
    max_num, min_num = parse_number_list[0], parse_number_list[0]

    # heap으로 바꿔본다면?
    # for num in parse_number_list:
    #     if num < min_num:
    #         min_num = num
    #     if num > max_num:
    #         max_num = num

    min_heap = []
    max_heap = []
    
    for num in parse_number_list:
        heapq.heappush(min_heap, num)
        heapq.heappush(max_heap, num * -1)
        
    min_num = heapq.heappop(min_heap)
    max_num = heapq.heappop(max_heap) * -1

    answer = str(min_num) + ' ' + str(max_num)
    return answer

