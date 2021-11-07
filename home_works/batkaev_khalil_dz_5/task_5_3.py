def tutors_with_klasses(tutors_list, klasses_list):
    for i, tutor in enumerate(tutors_list):
        if i < len(klasses_list):
            klass = klasses_list[i]
        else:
            klass = None
        yield tutor, klass


def print_tutors_with_klasses(tutors_list, klasses_list, tutors_gen):
    print(f'Ученики: {tutors_list}', f'Классы: {klasses_list}', f'Тип объекта: {type(tutors_gen)}',
          'Все значения генератора:', sep='\n')
    for el in tutors_gen:
        print(el)


tutors_1 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Маша', 'Слава']
klasses_1 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
tutors_gen_1 = tutors_with_klasses(tutors_1, klasses_1)

tutors_2 = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses_2 = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
tutors_gen_2 = tutors_with_klasses(tutors_2, klasses_2)

print_tutors_with_klasses(tutors_1, klasses_1, tutors_gen_1)
print_tutors_with_klasses(tutors_2, klasses_2, tutors_gen_2)