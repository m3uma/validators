# weryfikacja numeru dowodu osobistego

letter_values = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ";
letter_values_len = 36;

def get_letter_value(letter):
    for i in range(0, letter_values_len):
        if letter == letter_values[i]:
            return i
    return -1


def check_id(id_number):
    # nieprawidlowa dlugosc
    if len(id_number) != 9:
        return False
    # nieprawidlowa seria dowodu
    for i in range(0, 3):
        if get_letter_value(id_number[i]) < 10:
            return False
    # nieprawidlowy numer dowodu
    for i in range(3, 9):
        if get_letter_value(id_number[i]) < 0 \
                or get_letter_value(id_number[i]) > 9:
            return False

    checkSum = 7 * get_letter_value(id_number[0]);
    checkSum += 3 * get_letter_value(id_number[1]);
    checkSum += 1 * get_letter_value(id_number[2]);
    checkSum += 7 * get_letter_value(id_number[4]);
    checkSum += 3 * get_letter_value(id_number[5]);
    checkSum += 1 * get_letter_value(id_number[6]);
    checkSum += 7 * get_letter_value(id_number[7]);
    checkSum += 3 * get_letter_value(id_number[8]);
    checkSum %= 10;
    if checkSum != get_letter_value(id_number[3]):
        return False
    return True