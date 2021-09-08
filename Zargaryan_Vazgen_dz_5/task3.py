tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей','Дмитрий', 'Борис', 'Елена',]
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

def my_func():
    students = zip(tutors, klasses[:len(tutors)])
    for i in students:
        yield i


student = my_func()
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))
print(next(student))

