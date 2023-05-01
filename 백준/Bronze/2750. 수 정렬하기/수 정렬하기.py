# input
n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

# merge_sort
def merge_sort(array):
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    array1 = merge_sort(array[:mid])
    array2 = merge_sort(array[mid:])
    return merge(array1, array2)

def merge(array1, array2):
    result = []
    array1_crt_index = 0
    array2_crt_index = 0
    while array1_crt_index < len(array1) and array2_crt_index < len(array2):
        if array1[array1_crt_index] < array2[array2_crt_index]:
            result.append(array1[array1_crt_index])
            array1_crt_index += 1
        else:
            result.append(array2[array2_crt_index])
            array2_crt_index += 1
     
    if array1_crt_index == len(array1):
        while array2_crt_index < len(array2):
            result.append(array2[array2_crt_index])
            array2_crt_index += 1
        
    if array2_crt_index == len(array2):
        while array1_crt_index < len(array1):
            result.append(array1[array1_crt_index])
            array1_crt_index += 1
            
    return result


numbers = merge_sort(numbers)

# output
for num in numbers:
    print(num)

    