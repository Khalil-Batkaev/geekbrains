from os import stat, scandir
from os.path import join
from json import dump

dir_path = join('.', 'some_data_adv')
result_dict = {}
left_limit, right_limit, step, size_max = 0, 100, 10, 100000
# Если не известен потенциально максимальный размер файлов
# size_max = (stat(max(scandir(dir_path), key=lambda x: stat(x).st_size)).st_size) + 10000

while right_limit <= size_max:
    ext_set = set()
    count = 0
    for file in scandir(dir_path):
        if left_limit <= stat(file).st_size < right_limit:
            ext = file.name.rsplit('.', maxsplit=1)[-1]
            ext_set.add(ext)
            count += 1
    if ext_set:
        ext_list = list(ext_set)
        result_dict[right_limit] = [count] + [ext_list]
    left_limit = right_limit
    right_limit *= step

with open('task_7_5_summary.json', 'w', encoding='utf-8') as f:
    dump(result_dict, f)
