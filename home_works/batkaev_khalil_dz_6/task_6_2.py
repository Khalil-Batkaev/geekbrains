from task_6_1 import get_logs_from_file

ip_dict = {}
for ip in get_logs_from_file('logs_from_gb.txt', True):
    if ip not in ip_dict:
        ip_dict[ip] = 1
    else:
        ip_dict[ip] += 1
ip_spam = max(ip_dict, key=ip_dict.get)
quantity_request = ip_dict[ip_spam]
print(f'ip спамера: {ip_spam}, количество запросов: {quantity_request}')

# Проверка на наличие ещё одного спамера
check_dict = {ip_spam: quantity_request}
del ip_dict[ip_spam]
new_ip_spam = max(ip_dict, key=ip_dict.get)
new_quantity_request = ip_dict[new_ip_spam]

while new_quantity_request == quantity_request:
    print(f'ip спамера: {new_ip_spam}, количество запросов: {new_quantity_request}')
    check_dict[new_ip_spam] = new_quantity_request
    del ip_dict[new_ip_spam]
    new_ip_spam = max(ip_dict, key=ip_dict.get)
    new_quantity_request = ip_dict[new_ip_spam]

ip_dict.update(check_dict)
