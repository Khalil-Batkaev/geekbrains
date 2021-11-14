def is_valid_logs(check_ip, check_command, check_path):
    """
    Check logs for correct. Use the param.
    :param check_ip: ip of request for check
    :param check_command: request to server for check
    :param check_path: path of request for check
    """
    is_valid = False
    if (check_ip.count('.') == 3 or 5 <= check_ip.count(':') <= 7) \
            and check_command == check_command.upper() and check_path.count('/') == 2:
        is_valid = True
    else:
        print(f'Ошибка в данных {check_ip, check_command, check_path}')
    return is_valid


def get_logs_from_file(file_to_read, is_only_ip=False):
    """
    Give the elements from the marked file
    :param file_to_read: file with logs to edit
    :param is_only_ip: give only list with ip if True
    """
    with open(file_to_read, 'tr', encoding='utf-8') as f:
        for line in f:
            if is_only_ip:
                ip, *_ = line.split()
                yield ip
            else:
                ip, *text = line.split()
                if len(text[4]) >= 1:
                    command = text[4][1:]
                else:
                    print(f'Ошибка в данных: не верный запрос в строке {line}')
                path = text[5]
                if is_valid_logs(ip, command, path):  # Проверка на соответсвие данных
                    yield ip, command, path


if __name__ == '__main__':
    logs_list = [line for line in get_logs_from_file('logs_from_gb.txt')]
    print(logs_list)
