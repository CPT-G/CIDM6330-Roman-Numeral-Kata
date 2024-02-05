# Arrange
def number_roman(num):
    symbols = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
# Act
    roman = ''
    for value, symbol in symbols:
        while num >= value:
            roman += symbol
            num -= value
# Assert
    return roman


# UI
integer = int(input("Input number (betweeen 1-3000):"))

roman_numeral = number_roman(integer)
print(f">> Roman numeral equivalent: {roman_numeral}")


# References
# https://stackoverflow.com/questions/53908319/arabic-number-to-roman-numeral-converter-number-containing-4-will-not-convert
# https://www.tutorialspoint.com/python-program-to-convert-integer-to-roman
