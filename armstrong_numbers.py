"""
take each digit of a number and raise it to the power of the number of digits in the number
"""
def is_armstrong_number(number):
    """
    Check if a number is an Armstrong number.
    """
    number = str(number)
    sum = 0
    for digit in number:
        sum += int(digit) ** len(number)
    if sum == int(number):
        return True
    else:
        return False

is_armstrong_number(153)
