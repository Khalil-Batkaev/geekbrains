import re


def email_valid(email):
    re_name = r"(\w+[\.\+'_-]?\w+)+@(\w+[\.-]?\w+)+\.\w{2,}"
    is_valid = False
    if re.fullmatch(re_name, email, re.ASCII):
        is_valid = True
        return is_valid
    else:
        print('wrong email: ', email)
        raise ValueError


def email_parse(email):
    email_dict = dict()
    if email_valid(email):
        username, domain = re.split(r"@", email)
        email_dict[username] = domain
    return email_dict


try:
    print(email_parse("test@yandex.ru"))
    print(email_parse("123@yandex.google.com"))
    print(email_parse("batkaev.khalil@google-yandex.ru"))
    print(email_parse("batkaev_khalil@google.yandex.info"))

    print(email_parse("тест@yandex.ru"))
    print(email_parse("1$23@yandex.info"))
    print(email_parse("123@yandex.i"))
except ValueError:
    pass

# Совсем не уверен, но можно ли так делать?

# def email_valid(func):
#     def wrapper(email):
#         re_name = r"\w+(\.?\+?'?-?)\w+@\w+\.?-?\w+\.\w{2,}"
#         if re.fullmatch(re_name, email, flags=re.ASCII):
#             username, domain = re.split(r"@", email)
#             return username, domain
#         else:
#             print('wrong email: ', email)
#             raise ValueError
#     return wrapper
#
# @email_valid
# def email_parse(email):
#     email_dict = dict()
#     email_dict[username] = domain
#     return email_dict
