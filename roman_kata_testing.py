# I = 1
# II = 2
# III = 3
# LXXXVII = 87
# CMXXXII = 932
# MMDCCCLXXV = 2875
# MMM = 3000

# It's possible to build a full dictionary, but what a waste of time.

class roman_numeral(object):

    def number_to_roman(self, arabic):
        roman = self.to_roman(arabic)
        return roman

    def to_roman(self, number):
        if (number == 1):
            return ("I")

    def to_roman2(self, number):
        roman_number = ""
        if (number == 5):
            roman_number = "V"
        elif (number == 4):
            roman_number = "IV"
        else:
            while (number > 0):
                roman_number += "I"
                number -= 1
        return roman_number

# Need to build dictionary to include the numerals that have reductions like IV, IX.
# Have to have converter interpret left to right highest common demoninator
    # Like 1324 is 1000 + 300 + 20 + 4 (M + CCC + XX + IV)
