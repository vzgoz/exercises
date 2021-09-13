import sys

# names = []
# with open ('users.csv','r',encoding='utf-8') as f:
#     for line in f:
#         names.append(line.replace('\n',' ').replace(',',' '))
#
#
# hobbies = []
# with open('hobby.csv', 'r',encoding='utf-8') as f:
#     for line in f:
#         hobbies.append(line.replace('\n',' '))
#
# result = dict(zip(names,hobbies))
# print(result)

with open ('users.csv','w+',encoding='utf-8') as f_user, open ('hobby.csv', 'w+',encoding='utf-8') as f_hobby:
    f_user.writelines([ 'Иванов,Иван,Иванович\n','Петров,Петр,Петрович\n', 'Ильин, Олег, Семенович\n'])
    f_hobby.writelines(['скалолазание','охота\n','горные лыжи\n'])
    f_user.seek(0)
    f_hobby.seek(0)

    content_user = f_user.read()
    users = content_user.splitlines()
    content_hobby = f_hobby.read()
    hobbies = content_hobby.splitlines()
    n = 0
    if len(hobbies) < len(users):
        n = len(users) - len(hobbies)
        for i in range (1, n + 1):
            hobbies.append(None)
        result = tuple(zip(users, hobbies))
        print(result)
    else:
        sys.exit(1)