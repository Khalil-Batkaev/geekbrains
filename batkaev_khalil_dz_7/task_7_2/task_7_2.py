from os.path import join, exists
from os import mkdir

with open('config_2.yaml', 'r', encoding='utf-8') as f:
    dir_list = ['.', f.readline().strip()[:-1]]
    for line in f:
        dir_path = join(*dir_list)
        if not exists(dir_path):
            mkdir(dir_path)
        if ':' in line:
            if not line.count(' ') - len(dir_list):
                del dir_list[-1]
                dir_list.append(line.strip()[2:-1])
            elif len(dir_list) > line.count(' '):
                marker = int(line.count(' ') - len(dir_list)) - 1
                del dir_list[marker:]
                dir_list.append(line.strip()[2:-1])
            else:
                dir_list.append(line.strip()[2:-1])
        else:
            file_path = join(dir_path, line.strip()[2:])
            with open(file_path, 'w', encoding='utf-8') as file_create:
                pass
