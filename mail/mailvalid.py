def validate_mail(value):
    if value.count('.') < 1 and value.count('@') < 1:
        return False
    else:
        return True