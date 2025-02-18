import hashlib

def hash_password(password):
    md5 = hashlib.md5(password.encode('utf-8'))
    if len(password) >= 7 \
            and any(x.isupper() for x in password) \
            and any(x.islower() for x in password) \
            and any(x.isdigit() for x in password) \
            and any(x for x in password if x in '!@#$%^&*()_+-={}[]|\:;\'<>?,./"'):
        return md5.hexdigest()

def check_password(psw):
    if len(psw) >= 7 \
            and any(x.isupper() for x in psw) \
            and any(x.islower() for x in psw) \
            and any(x.isdigit() for x in psw) \
            and any(x for x in psw if x in '!@#$%^&*()_+-={}[]|\:;\'<>?,./"'):
        return True
    else:
        return False