import re
import getpass
import bisect

MINIMUM_STRENGTH_OF_VALID_PASS = 2
LENGTH_BREAKPOINTS = [10, 14, 18]


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
    return range(1, 5)[bisect.bisect(LENGTH_BREAKPOINTS, len(password))]


def get_password_strength(password):
    strength = MINIMUM_STRENGTH_OF_VALID_PASS
    strength += check_case_sensitivity(password)
    strength += check_digits(password)
    strength += check_special_chars(password)
    strength += check_length(password)
    return strength


def check_password(password):
    if len(password) < 6:
        print_strength(error='length less then 6 chars')
        return False
    if password.isdigit():
        print_strength(error='only digits')
        return False
    if re.search(r'\s', password):
        print_strength(error='whitespace')
        return False
    return True


def print_strength(strength_value=0, error=None):
    if error:
        print('Invalid password ({})'.format(error))
    print('Password strength is {}/10'.format(strength_value))


if __name__ == '__main__':
    password = getpass.getpass('Input password: ')
    if check_password(password):
        print_strength(strength_value=get_password_strength(password))
