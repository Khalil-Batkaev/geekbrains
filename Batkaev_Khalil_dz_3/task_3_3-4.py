def thesaurus(*args):
    """Give a dictionary of people's names. Key is the first char of the name"""
    names = {}
    args = sorted(args)
    for name in args:
        if name[0] not in names:
            names[name[0]] = [name]
        else:
            names[name[0]] += [name]
    print(names)


def thesaurus_adv(*args):
    """Give a dictionary of people's full names. The keys are the first char of the surname and name"""
    args = sorted(args)
    full_names = {}
    keys = []
    for full_name in args:
        first_name, last_name = full_name.split()
        keys.append(last_name[0])
    keys.sort()
    for key in keys:
        names = {}
        for full_name in args:
            first_name, last_name = full_name.split()
            if last_name.startswith(key):
                if first_name[0] not in names:
                    names[first_name[0]] = [full_name]
                else:
                    names[first_name[0]] += [full_name]
        full_names[key] = names

    print(full_names)


thesaurus('Иван', 'Павел', 'Мария', 'Сергей', 'Маша', 'Саша', 'Роман')
thesaurus_adv("Иван Сергеев", "Алла Сидорова", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Маша Ильина",
              "Наталья Илюхина", "Анна Савельева", "Василий Суриков", "Павел Антонов")
