"""
run Collatz conjecture to make any positive integer to eventually equal 1 and show how many steps
"""
def steps(number):
    """
    runs algorithm to eventually equal 1
    Parameters:
        number
    """
    if number <= 0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
    step_n = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1
        step_n += 1
    return step_n
