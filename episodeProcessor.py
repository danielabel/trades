from functools import reduce
from decimal import *


def balance_accumulator(total, row):
    return total - Decimal(row[0]) * Decimal(row[1])


def final_balance(df):
    total = reduce(balance_accumulator, zip(df['Trade Price'], df['Trade Quantity']), Decimal('0'))
    cents = Decimal('0.01')
    return total.quantize(cents, ROUND_HALF_UP)


def cost(quantity, price):
    # returns the difference between post and pre
    return -(quantity * price)


def old_profit(df):
    df['cost of trade'] = cost(df['Trade Price'], df['Trade Quantity'])
    return df['cost of trade'].sum()
