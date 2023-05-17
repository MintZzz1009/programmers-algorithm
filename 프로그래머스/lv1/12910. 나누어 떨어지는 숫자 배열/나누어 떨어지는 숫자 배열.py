def solution(arr, divisor):
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
            
    if len(answer) != 0:
        # 오름차순 정렬 - merge_sort
        answer = merge_sort(answer)
        
    else:
        answer.append(-1)
    
    return answer

def merge_sort(arr):
    mid = len(arr) // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    merge_sorted_arr = merge(left_arr, right_arr)
    return merge_sorted_arr

def merge(left_arr, right_arr):
    merged_array = []
    left_arr_index = 0
    right_arr_index = 0
    
    while left_arr_index < len(left_arr) and right_arr_index < len(right_arr):
        if left_arr[left_arr_index] < right_arr[right_arr_index]:
            merged_array.append(left_arr[left_arr_index])
            left_arr_index += 1
            
        if right_arr[right_arr_index] < left_arr[left_arr_index]:
            merged_array.append(right_arr[right_arr_index])
            right_arr_index += 1
        
        if right_arr[right_arr_index] == left_arr[left_arr_index]:
            merged_array.append(left_arr[left_arr_index])
            left_arr_index += 1
            right_arr_index += 1
            
    while left_arr_index < len(left_arr):
        merged_array.append(left_arr[left_arr_index])
        left_arr_index += 1
    
    while right_arr_index < len(right_arr):
        merged_array.append(right_arr[right_arr_index])
        right_arr_index += 1
        
    return merged_array
        
            
        