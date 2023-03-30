nums=[18, 50, 210, 80, 145, 333, 70, 30]

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        mid = len(lst) // 2
        left = merge_sort(lst[:mid])
        right = merge_sort(lst[mid:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def print_and_sort(lst):
    lst_sorted = merge_sort(lst)
    for num in lst_sorted:
        if num % 10 == 0 and num < 200:
            print(num)
        elif num >= 300:
            break

print_and_sort(nums)  # imprime 10, 20, 30 y detiene la ejecución en 301
