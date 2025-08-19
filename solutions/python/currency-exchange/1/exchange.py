"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    exchange = budget / exchange_rate
    return exchange


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    get = budget - exchanging_value
    return get


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - total number of bills.
    :return: int - calculated value of the bills.
    """
    den = denomination * number_of_bills
    return den

    


def get_number_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained from the amount.
    """

    num = amount // denomination
    return num


def get_leftover_of_bills(amount, denomination):
    """

    :param amount: float - the total starting value.
    :param denomination: int - the value of a single bill.
    :return: float - the amount that is "leftover", given the current denomination.
    """

    left = amount % denomination
    return left



def exchangeable_value(budget, exchange_rate, spread, denomination):
    # Calcola lo spread come decimale
    fee_rate = exchange_rate * (spread / 100)
    
    # Calcola il tasso effettivo con lo spread
    actual_rate = exchange_rate + fee_rate

    # Calcola l'importo totale ottenibile nella nuova valuta
    exchanged = budget / actual_rate

    # Calcola quante banconote intere del taglio specificato si possono ottenere
    total_value = int(exchanged // denomination) * denomination

    return total_value