import re


def get_password_strength(password):
    answer = 0
    if len(password) > 6:
        answer += 1
    if re.search(r'[a-z]', password):
        answer += 1
    if re.search(r'[A-Z]', password):
        answer += 1
    if re.search(r'\d', password):
        answer += 1
    if re.search(r'[!@#$%&]', password):
        answer += 1
    if len(password) > 10:
        answer *= 2
    return answer


if __name__ == '__main__':
    password = input('input password: ')
    print(get_password_strength(password))
