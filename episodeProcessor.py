from functools import reduce
from decimal import Decimal, ROUND_HALF_UP
from columns import *


def calc_total_of_all_buys_and_sells(df):
    return reduce(balance_accumulator, zip(df[TRADE_PRICE], df[TRADE_QUANTITY]), Decimal('0'))


def final_balance(df):
    total = calc_total_of_all_buys_and_sells(df)
    return round_to_currency(total)


def round_to_currency(total):
    cents = Decimal('0.01')
    return total.quantize(cents, ROUND_HALF_UP)


def balance_accumulator(total, row):
    return total - Decimal(row[0]) * Decimal(row[1])
