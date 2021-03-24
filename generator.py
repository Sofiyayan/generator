import string
import itertools


def validator(length: int):
    if length < 8:
        raise Exception("The length of the password should be at least 8 characters")


def possible_password(length: int):
    all_char = "".join(
        [
            string.ascii_letters,
            str(string.punctuation.replace(">", "")).replace("<", ""),
            "0123456789",
        ]
    )
    possibles = itertools.permutations(all_char, length)
    for pw in possibles:
        yield pw


def password(length: int):
    checker = possible_password(length)
    lower = set(string.ascii_lowercase)
    upper = set(string.ascii_uppercase)
    number = set("0123456789")
    punc = set(str(string.punctuation.replace(">", "")).replace("<", ""))
    for pw in checker:
        intersection = (
            set(pw).intersection(lower)
            and set(pw).intersection(upper)
            and set(pw).intersection(number)
            and set(pw).intersection(punc)
        )
        if bool(intersection):
            yield "".join(pw)


if __name__ == "__main__":
    length_input = int(input("Please input the length of the password: ").strip())
    validator(length_input)
    current_password = password(length_input)
    print(next(current_password))
