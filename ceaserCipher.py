import string


def encode(str1, shift=13):
    lc = string.ascii_lowercase
    uc = string.ascii_uppercase
    new_lc = lc[shift:] + lc[:shift]
    new_uc = uc[shift:] + uc[:shift]
    map = str.maketrans(lc + uc, new_lc + new_uc)
    return str1.translate(map)
