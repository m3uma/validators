def check_adress(adress):
    if adress is not None:
        if len(adress) >= 1 \
                and any(x.isdigit() for x in adress):
            return True
        else:
            return False

