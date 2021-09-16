import os

subfolder_names = ['settings','mainapp','adminapp','authapp'] #имена подпапок
for subfolder_name in subfolder_names:
    os.makedirs(os.path.join('my_project',subfolder_name))

