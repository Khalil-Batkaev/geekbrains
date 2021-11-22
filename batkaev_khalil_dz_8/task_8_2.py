import re

re_pattern = re.compile(''' 
                            ((?:(?:\d{1,3}\.){3}\d{1,3})|                   # re_ip_v4
                            (?:(?:\w{3,4}:{1,2}){4,7}(?:\w{1,4})))          # re_ip_v6
                            (?:(?:\s+-){2}\s)                               # trash
                            (\[\d{2}/\w+/\d{4}(?::\d{2}){3}\s\+\d{4}])      # re_datetime
                            \s                                              # trash
                            (?:"([A-Z]{3,})\s)                              # re_request
                            ((?:/[a-z]+){2}_\d)                             # re_resource
                            (?:\s\w+/\w\.\w"\s)                             # trash  
                            (?:(\d{3})\s                                    # re_code
                            (\d+)?)                                         # re_size
                        ''', re.X)


def parser_logs(file):
    with open(file, 'tr', encoding='utf-8') as f:
        logs_set = set()
        for line in f:
            logs = re.findall(re_pattern, line)
            logs_set.add(*logs)
        return list(logs_set)


print(parser_logs('logs_from_gb.txt'))


