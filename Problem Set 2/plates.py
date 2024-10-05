def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # if len(s) < 2 or len(s) > 6:
    #     return False

    # if s[0].isalpha() == False or s[1].isalpha() == False:
    #     return False

    # i = 0
    # while i < len(s):
    #     if s[i].isalpha() == False:
    #         if s[i] == '0':
    #             return False
    #         else:
    #             break
    #     i += 1

    # for c in s:
    #     if c in ['.', ' ', '!', '?']:
    #         return False

    # return True


    import pytest


def is_valid(plate) -> bool:
    # vanity plates may contain a maximum of 6 characters
    # and a minimum of 2 characters
    if len(plate) < 2 or len(plate) > 6:
        return False

    state = 0
    for i, c in enumerate(plate):
        # vanity plates may contain...letters or numbers
        # No periods, spaces, or punctuation marks are allowed
        if not (c.isdecimal() or c.isalpha()):
            return False

        if state == 0:
            # All vanity plates must start with at least two letters
            if c.isdecimal():
                return False
            if i == 1:
                state = 1
        elif state == 1:
            # If we find a number, everything else needs to be numbers
            if c.isdigit():
                # First number used cannot be '0'
                if c == "0":
                    return False
                state = 2
        elif state == 2:
            # Letters after numbers is not allowed
            if c.isalpha():
                return False

    return True


main()
