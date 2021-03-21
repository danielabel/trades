from functools import reduce


def balance_accumulator(total, row):
    return total - row[0] * row[1]


def final_balance(df):
    return reduce(balance_accumulator, zip(df['Trade Price'], df['Trade Quantity']), 0)


def cost(quantity, price):
    # returns the difference between post and pre
    return -(quantity * price)


def old_profit(df):
    df['cost of trade'] = cost(df['Trade Price'], df['Trade Quantity'])
    return df['cost of trade'].sum()
