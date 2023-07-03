import os


if __name__ == '__main__':
    s = input()
    is_alnum = False
    has_alphabetical_chars = False
    has_digits = False
    has_lowercase = False
    has_uppercase = False
    for ch in s:
        if ch.isalnum():
            is_alnum = True
        if ch.isalpha():
            has_alphabetical_chars = True
        if ch.isnumeric():
            has_digits = True
        if ch.islower():
            has_lowercase = True
        if ch.isupper():
            has_uppercase = True

    print(f"{is_alnum}\n{has_alphabetical_chars}\n{has_digits}\n{has_lowercase}\n{has_uppercase}")