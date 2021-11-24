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
    re_name = r"(\w+(?:\.?\+?'?-?)\w+)@(\w+\.?-?\w+\.\w{2,})"
    email_dict = dict()
    match = re.findall(re_name, email)
    username, domain = match[0][0], match[0][1]
    email_dict['username'] = username
    email_dict['domain'] = domain
    return email_dict


print(email_parse("test@yandex.ru"))
print(email_parse("123@yandex.google.com"))
print(email_parse("batkaev.khalil@google-yandex.ru"))
print(email_parse("batkaev_khalil@google.yandex.info"))

print(email_parse("тест@yandex.ru"))
print(email_parse("1$23@yandex.info"))
print(email_parse("123@yandex.i"))