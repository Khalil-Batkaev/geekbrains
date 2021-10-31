def get_jokes_adv(n, lst_1, lst_2, lst_3, flag='no'):
    """
    Gives a random jokes. n is quantity of jokes. lst_1, lst_2, lst_3 are lists with words to jokes.
    If flag is 'yes' jokes will be unique
    """
    from random import choice, sample  # Записал импорт в тело функции, чтобы можно было запускать её в любом месте
    jokes = []
    if flag == 'no':
        for _ in range(n):
            joke = ' '.join([choice(lst_1), choice(lst_2), choice(lst_3)])
            jokes.append(joke)
    else:
        if min(len(lst_1), len(lst_2), len(lst_3)) < n:
            n = min(len(lst_1), len(lst_2), len(lst_3))
            print('Количество уникальных шуток не может быть больше количества переданных слов, т.е.', n)
        _lst_1, _lst_2, _lst_3 = sample(lst_1, n), sample(lst_2, n), sample(lst_3, n)
        for i in range(n):
            joke = ' '.join([_lst_1[i], _lst_2[i], _lst_3[i]])
            jokes.append(joke)
    print(jokes)


nouns = ['автомобиль', 'лес', 'огонь', 'город', 'дом']
adverbs = ['сегодня', 'вчера', 'завтра', 'позавчера', 'ночью']
adjectives = ['веселый', 'яркий', 'зеленый', 'утопичный', 'мягкий']

get_jokes_adv(4, nouns, lst_3=adjectives, lst_2=adverbs)
get_jokes_adv(6, nouns, adverbs, adjectives)
get_jokes_adv(4, nouns, lst_3=adjectives, lst_2=adverbs, flag='yes')
get_jokes_adv(6, nouns, adverbs, adjectives, 'yes')
