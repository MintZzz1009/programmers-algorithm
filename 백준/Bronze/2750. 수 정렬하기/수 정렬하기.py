# input
n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    numbers.append(num)

# solution - bubble_sort
# for _ in range(n):
#     for i in range(n - 1):
#         if numbers[i] > numbers[i + 1]:
#             numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            
# solution - selection_sort
for start_index in range(len(numbers)):
    min_index = start_index
    for i in range(start_index, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
            numbers[min_index] = numbers[i]
    else:
        numbers[start_index], numbers[min_index] = numbers[min_index], numbers[start_index]
        
# output
for num in numbers:
    print(num)
