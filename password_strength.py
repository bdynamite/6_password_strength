import re


def check_case_sensitivity(password):
    if password.islower() or password.isupper():
        return 1
    return 2


def check_digits(password):
    if re.search(r'\d', password):
        return 1
    return 0


def check_special_chars(password):
    if re.search(r'[!@#$%&]', password):
        return 1
    return 0


def check_length(password):
    if len(password) < 10:
        return 1
    elif len(password) < 14:
        return 2
    elif len(password) < 18:
        return 3
    return 4


def get_password_strength(password):
    strength = 2
    strength += check_case_sensitivity(password)
    strength += check_digits(password)
    strength += check_special_chars(password)
    strength += check_length(password)
    return strength


def print_error(error):
    print('Invalid password ({})'.format(error))


def check_password(password):
    if len(password) < 6:
        print_error('length less then 6')
        return False
    if password.isdigit():
        print_error('only digits')
        return False
    if re.search(r'\s', password):
        print_error('whitespace')
        return False
    return True


if __name__ == '__main__':
    password = input('input password: ')
    if check_password(password):
        print('password strength is {}/10'.format(get_password_strength(password)))
