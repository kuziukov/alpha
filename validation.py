import trafaret as t


def validation_email(email):
    try:
        t.Regexp(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)").check(email)
    except:
        raise t.DataError("email is not valid.")


def validation_phone(number):
    try:
        t.Regexp(r"^(\d{10})(?:\s|$)").check(number)
    except:
        raise t.DataError("phone number is not valid.")


