class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        for _ in self.my_list:
            for i in _:
                print(f'{i:4}', end='')
            print()
        return ''


    def __add__(self, other):
        for i in range (len(self.my_list)):
            for el in range (len(other.my_list[i])):
                self.my_list[i][el] = self.my_list[i][el] + other.my_list[i][el]
        return Matrix.__str__(self)


result = Matrix([[-1,0,1],[-1,0,1],[0,1,-1],[1,1,-1]])
new_result = Matrix([[-4,0,4],[-4,0,4],[0,4,-4],[4,4,3]])
print(result.__add__(new_result))