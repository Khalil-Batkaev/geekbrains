from os import stat, scandir
from os.path import join
from json import dump

dir_path = join('.', 'some_data_adv')
result_dict = {}
left_limit, right_limit, step, size_max = 0, 100, 10, 100000

while right_limit <= size_max:
    ext_list = list()
    for file in scandir(dir_path):
        if left_limit <= stat(file).st_size < right_limit:
            ext = file.name.rsplit('.', maxsplit=1)[-1]
            ext_list.append(ext)
    if ext_list:
        quantity = len(ext_list)
        unique_ext_list = list(set(ext_list))
        result_dict[right_limit] = [quantity] + [unique_ext_list]
    left_limit = right_limit
    right_limit *= step

with open('task_7_5_summary.json', 'w', encoding='utf-8') as f:
    dump(result_dict, f)
