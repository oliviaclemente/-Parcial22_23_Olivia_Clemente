def print_multiples(lst):
    for num in lst:
        if num % 10 == 0 and num < 200:
            print(num)


nums=[18, 50, 210, 80, 145, 333, 70, 30]
print_multiples(nums)