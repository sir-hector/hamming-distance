def roman(number):
    result = ''

    decimal = (number % 100) // 10

    if decimal == 9:
        result = "XC"
    elif decimal == 8:
        result = "LXXX"
    elif decimal == 7:
        result = "LXX"
    elif decimal == 6:
        result = "LX"
    elif decimal == 5:
        result = "L"
    elif decimal == 4:
        result = "XL"
    elif decimal == 3:
        result = "XXX"
    elif decimal == 2:
        result = "XX"
    elif decimal == 1:
        result = "X"

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
