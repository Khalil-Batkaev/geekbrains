from os import mkdir, walk
from os.path import join, exists
from shutil import copytree

project_path = join('.', 'my_project')
templates_path = join(project_path, 'templates')
if not exists(templates_path):
    mkdir(templates_path)
for root, dirs, files in walk(project_path):
    if root.endswith('templates'):
        copytree(root, templates_path, dirs_exist_ok=True)
