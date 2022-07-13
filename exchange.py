def exchange_money(budget, exchange_rate):
    """
    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return float(budget / exchange_rate)

def get_change(budget, exchanging_value):
    """
    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return float(budget - exchanging_value)

def get_value_of_bills(denomination, number_of_bills):
    """
    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return int(denomination * number_of_bills)

def get_number_of_bills(budget, denomination):
    """
    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget // denomination)

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    sprd = spread / 100
    xrt = exchange_rate * sprd
    fr = xrt + exchange_rate
    conv = (budget / fr)
    final = (int(conv/denomination)) * denomination
    """
    /denomination takes how many times you can put the money into bills, int turns to int, * denomination gives how much money you have after conversion and w/out float
    """
    #don't write in one line: return int(((budget / exchange_rate) + (exchange_rate * (spread / 100))) // denomination)
    return final

def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """
    sprd = spread / 100
    xrt = exchange_rate * sprd
    fr = xrt + exchange_rate
    conv = (budget / fr)
    final = int(conv%denomination)
    return final

non_exchangeable_value(100000, 10.61, 10, 1)
non_exchangeable_value(1500, 0.84, 25, 40)
non_exchangeable_value(425.33, 0.0009, 30, 700)
non_exchangeable_value(12000, 0.0096, 10, 50)
# output_data = [0, 28, 229, 13]