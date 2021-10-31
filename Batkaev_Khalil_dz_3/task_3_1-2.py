def num_translate_adv(number):
    """Gives Russian translation of numbers 0-10"""

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

    if number == number.title():
        print(num_dict.get(number.lower()).title())
    else:
        print(num_dict.get(number.lower()))

num_translate_adv('пять')