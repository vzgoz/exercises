def thesaurus(*names):
    list_name = [*names]
    dictionary = {}
    for name in list_name:
        name.capitalize()
        char = name[0]
        dict_1 = {char : name}
        dictionary.update(dict_1)

    return dictionary

print(thesaurus('Мария','Олег','Иван'))