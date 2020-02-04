def check_zipcode(value):
    if value is not None:
        if len(value) == 6 and value[2] == '-':
            return True
        else:
            return False

