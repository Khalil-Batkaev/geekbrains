import re

re_pattern = re.compile('''
                           ((?:(?:\d{1,3}\.){3}\d{1,3})|                # re_ip_v4
                           (?:(?:\w{3,4}:{1,2}){4,7}(?:\w{1,4})))|      # re_ip_v6
                           (\[\d{2}/\w+/\d{4}(?::\d{2}){3}\s\+\d{4}])|  # re_datetime
                           (?:"([A-Z]{3,})\s)|                          # re_request
                           ((?:/[a-z]+){2}_\d)|                         # re_resource
                           (?:\s(\d{3})\s(\d+)?)                        # re_code_re_size
                        ''', re.X)


def parser_logs(file):
    with open(file, 'tr', encoding='utf-8') as f:
        for line in f:
            match = re.findall(re_pattern, line)
            logs_list = list()
            for i, el in enumerate(match):
                logs_list.append(el[i])
                if i == 4:  # Делим на части re_code_re_size и добавляем re_size
                    logs_list.append(el[i + 1])
                    break
            yield tuple(logs_list)


logs = list(set(parser_logs('logs_from_gb.txt')))
print(logs)
