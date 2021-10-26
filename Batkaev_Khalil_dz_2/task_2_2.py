print('Решение задачи с созданием нового списка')
print()

lst_to_edit = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+7', 'градусов']
lst_after_edit = []
numbers = []

for text in lst_to_edit:
    if text.isdigit():
        lst_after_edit.extend(['"', f'{int(text):02d}', '"'])
        numbers.append(f'{int(text):02d}')
    elif '+' in text or '-' in text:
        lst_after_edit.extend(['"', f'{int(text):+03d}', '"'])
        numbers.append(f'{int(text):+03d}')
    else:
        lst_after_edit.append(text)

text = ' '.join(lst_after_edit)

for number in numbers:
    text = text.replace(f'" {number} "', f'"{number}"')

print(lst_to_edit)
print(lst_after_edit)
print(text)

print()
print('Решение задачи без создания нового списка')
print()

lst_result = ['примерно в', '23', 'часа', '8', 'минут', '03', 'секунд', 'температура', 'воздуха', 'была', '-5',
              'градусов Цельсия', 'темп', 'воды', '+12', 'градусов', 'Цельсия']
numbers_result = []
limit_lst = len(lst_result)
print(lst_result)

for i in range(limit_lst):
    if lst_result[i].isdigit():
        lst_result.extend(['"', f'{int(lst_result[i]):02d}', '"'])
        numbers_result.append(f'{int(lst_result[i]):02d}')
    elif '+' in lst_result[i] or '-' in lst_result[i]:
        lst_result.extend(['"', f'{int(lst_result[i]):+03d}', '"'])
        numbers_result.append(f'{int(lst_result[i]):+03d}')
    else:
        lst_result.append(lst_result[i])

lst_result = lst_result[limit_lst:]
text_result = ' '.join(lst_result)

for number in numbers_result:
    text_result = text_result.replace(f'" {number} "', f'"{number}"')

print(lst_result)
print(text_result)
