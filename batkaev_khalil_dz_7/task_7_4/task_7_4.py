from os import stat, scandir
from os.path import join

dir_path = join('.', 'some_data')
size_dict = {}
left_limit, right_limit, step, size_max = 0, 100, 10, 100000

while right_limit <= size_max:
    for file in scandir(dir_path):
        if left_limit <= stat(file).st_size < right_limit:
            if right_limit not in size_dict:
                size_dict[right_limit] = 1
            else:
                size_dict[right_limit] += 1
    left_limit = right_limit
    right_limit *= step

print(size_dict)
