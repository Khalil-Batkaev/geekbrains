import re


def email_valid(func):
    def wrapper(email):
        re_name = r"\w+(\.?\+?'?-?)\w+@\w+\.?-?\w+\.\w{2,}"
        if re.fullmatch(re_name, email, re.ASCII):
            result = func(email)
            return result
        else:
            msg = f'wrong email: {email}'
            raise ValueError(msg)
    return wrapper


@email_valid
def email_parse(email):
    email_dict = dict()
    username, domain = re.split(r"@", email)  # или re.search(r"\w+(\.?\+?'?-?)\w+", email)[0], re.search(r"\w+\.?-?\w+\.\w{2,}", email)[0]
    email_dict[username] = domain
    return email_dict


print(email_parse("test@yandex.ru"))
print(email_parse("123@yandex.google.com"))
print(email_parse("batkaev.khalil@google-yandex.ru"))
print(email_parse("batkaev_khalil@google.yandex.info"))

print(email_parse("тест@yandex.ru"))
print(email_parse("1$23@yandex.info"))
print(email_parse("123@yandex.i"))