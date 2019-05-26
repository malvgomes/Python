import re


def validate_pin(pin):
    return (len(pin) == 6 or len(pin) == 4) and not re.search("\D", pin)


print(validate_pin("12a67"))
