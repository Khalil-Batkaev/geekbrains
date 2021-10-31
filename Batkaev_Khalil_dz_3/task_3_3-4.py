def thesaurus(*args):
    """Gives a dictionary of some people's names. Key is the first char of the name"""
    names = {}
    for name in args:
        if name[0] not in names:
            names[name[0]] = [name]
        else:
            names[name[0]] += [name]
    print(names)


thesaurus('Иван', 'Мария', 'Сергей', 'Маша', 'Саша', 'Роман')
