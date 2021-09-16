import os


settings_file_names = ['__init__.py', 'dev.py', 'prod.py']
for file in settings_file_names:
    result = open(os.path.join('my_project/settings',file),'a')

mainapp_files = ['__init__.py', 'models.py', 'views.py']
for file in mainapp_files:
    result = open(os.path.join('my_project/mainapp',file),'a')

templ_main = 'my_project/mainapp/templates/mainapp'
if not os.path.exists(templ_main):
    os.mkdir(templ_main)


authapp_files = ['__init__.py', 'models.py', 'views.py']
for file in authapp_files:
    result = open(os.path.join('my_project/authapp',file), 'a')

templ_auth = 'my_project/authapp/templates/authapp'
if not os.path.exists(templ_auth):
    os.mkdir(templ_auth)

template_files = ['base.html', 'index.html']
for file in template_files:
    result_auth = open(os.path.join(templ_auth,file),'a')
    result_main = open(os.path.join(templ_main,file),'a')
