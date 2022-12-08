def roman(number):
    result = ''

    thousands = (number % 10000) // 1000

    if thousands == 3:
        result = result + "MMM"
    elif thousands == 2:
        result = result + "MM"
    elif thousands == 1:
        result = result + "M"

    hundreds = (number % 1000) // 100

    if hundreds == 9:
        result = result + "CM"
    elif hundreds == 8:
        result = result + "DCCC"
    elif hundreds == 7:
        result = result + "DCC"
    elif hundreds == 6:
        result = result + "DC"
    elif hundreds == 5:
        result = result + "D"
    elif hundreds == 4:
        result = result + "CD"
    elif hundreds == 3:
        result = result + "CCC"
    elif hundreds == 2:
        result = result + "CC"
    elif hundreds == 1:
        result = result + "C"

    decimal = (number % 100) // 10

    if decimal == 9:
        result = result + "XC"
    elif decimal == 8:
        result = result + "LXXX"
    elif decimal == 7:
        result = result + "LXX"
    elif decimal == 6:
        result = result + "LX"
    elif decimal == 5:
        result = result + "L"
    elif decimal == 4:
        result = result + "XL"
    elif decimal == 3:
        result = result + "XXX"
    elif decimal == 2:
        result = result + "XX"
    elif decimal == 1:
        result = result + "X"

    ones = (number % 10)

    if ones == 1:
        return result + "I"
    if ones == 2:
        return result + "II"
    if ones == 3:
        return result + "III"
    if ones == 4:
        return result + "IV"
    if ones == 4:
        return result + "IV"
    if ones == 5:
        return result + "V"
    if ones == 6:
        return result + "VI"
    if ones == 7:
        return result + "VII"
    if ones == 8:
        return result + "VIII"
    if ones == 9:
        return result + "IX"

    return result
