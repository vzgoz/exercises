def odd_nums(max_num):
    for num in range(1, max_num + 1):
        if num % 2 != 0:
            yield num


print(list(odd_nums(15)))

odd_to_15 = odd_nums(15)

print(list(odd_to_15))

