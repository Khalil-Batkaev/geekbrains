def num_translate_adv(number, number_dict):
    """Gives Russian translation of numbers 0-10"""
    num = number.lower()
    if number == number.title():
        return number_dict.get(num.title())
    else:
        return number_dict.get(num)


num_dict = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'
}

print(num_translate_adv('one', num_dict))
print(num_translate_adv('Two', num_dict))
print(num_translate_adv('eleven', num_dict))
