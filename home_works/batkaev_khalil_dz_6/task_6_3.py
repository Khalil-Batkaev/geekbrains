from itertools import zip_longest


def get_data_from_file(file_to_read, is_need_parsing=False):
    """
    Give the element from the marked file
    :param file_to_read: file with logs to edit
    :param is_need_parsing: do parsing of string if True
    """
    with open(file_to_read, 'tr', encoding='utf-8') as f:
        if not is_need_parsing:
            for line in f:
                yield line.strip()
        else:
            for full_name in f:
                last_name, first_name, patronymic = full_name.split(', ')
                initials = last_name[:1] + first_name[:1] + patronymic[:1]
                yield initials


users = [name for name in get_data_from_file('task_3_users.csv', True)]
hobbies = [hobby for hobby in get_data_from_file('task_3_hobby.csv')]
with open('task_3_rezult.txt', 'tw', encoding='utf-8') as f:
    if len(users) > len(hobbies):
        hobbies_dict = dict(zip_longest(users, hobbies, fillvalue=None))
        f.write(str(hobbies_dict))
    else:
        hobbies_dict = dict(zip(users, hobbies))
        f.write(str(hobbies_dict))
        exit(1)
