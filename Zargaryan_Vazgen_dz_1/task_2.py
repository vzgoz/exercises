cube = []
for number in range(0, 1001):
    if number % 2 != 0:
        cube.append(number ** 3)

print(cube)




# А. Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
numbers_sum = 0
for number in cube:
    sum = 0
    number_test = number
    while number_test:
        last_number = number_test % 10
        number_test = number_test // 10
        sum = sum + last_number
    if sum % 7 == 0:
        numbers_sum = numbers_sum + number

print(numbers_sum)



#Б. К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.

for number in range(len(cube)):
    cube[number] += 17
numbers_sum = 0
for number in cube:
    sum = 0
    number_test = number
    while number_test:
        last_number = number_test % 10
        number_test = number_test // 10
        sum = sum + last_number
    if sum % 7 == 0:
        numbers_sum = numbers_sum + number

print(numbers_sum)



