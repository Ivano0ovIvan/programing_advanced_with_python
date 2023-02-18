from re import findall


def email_validator(email):
    try:
        if current_email.count('@') > 1:
            raise MoreThanOneAtSymbolError
        if findall(pattern_for_name, current_email)[0] != current_email.split('@')[0]:
            raise InvalidNameError('Name must contain only letters, numbers, dots and underscores')
        if len(current_email.split('@')[0]) < 4:  # 4 is the minimum length for the name
            raise NameTooShortError("Name must be more than 4 characters")
        if '@' not in current_email:
            raise MustContainAtSymbolError("Email must contain @")
        if findall(pattern_for_domain, current_email)[-1] not in valid_domains:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    except IndexError:
        print('Invalid email address!')

    else:
        print('Email is valid')


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


pattern_for_name = r'[\w+\.]+'
pattern_for_domain = r'\.[a-z]+'

valid_domains = ['.com', '.net', '.bg', '.org']

current_email = input()

while current_email != 'End':
    email_validator(current_email)

    current_email = input()
