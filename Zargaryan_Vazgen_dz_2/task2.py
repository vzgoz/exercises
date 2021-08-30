words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


result = []
for i in words: # Поиск чисел в списке и добавление к ним ковычек
    if i.isdigit() or i.count('+'):
        new_i = int(i)
        new_i = f'"{new_i:02d}"'
        result.append(new_i)

str_words = ' '.join(words) # Перевод списка в строку и отделение элементов пробелом

replace_first = str_words.replace('5',result[0]) # Заменя первого числа
replace_second = replace_first.replace('17',result[1]) # Замена второго числа
replace_third = replace_second.replace('+5',result[2]) # Замена третьего числа

print(replace_third)