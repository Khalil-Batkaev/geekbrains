from os.path import join, exists
from os import mkdir

dir_names = ['settings', 'mianapp', 'authapp', 'adminapp']

project_path = join('.', 'my_project')
if not exists(project_path):
    mkdir(project_path)
for dir_name in dir_names:
    dir_path = join(project_path, dir_name)
    if not exists(dir_path):
        mkdir(dir_path)
