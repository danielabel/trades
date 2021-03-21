import pandas
import episodeProcessor
from decimal import Decimal


def test_calc_episode_balance():
    # given a data frame with a Trade price column
    df = pandas.DataFrame([['10', 5], ['12', 5], ['8', 1], ['2', 1], ['13', -12]],
                          columns=['Trade Price', 'Trade Quantity'])

    # when we calc profit
    profit = episodeProcessor.final_balance(df)

    # then we get the expected total
    assert (profit == 36)


def test_calc_episode_balance_with_cents():
    # given a data frame with a Trade price column (price is a string to avoid float nonsense)
    df = pandas.DataFrame([['10.52', 5], ['12.44', 5], ['8.33', 1], ['2', 1], ['13', -12]],
                          columns=['Trade Price', 'Trade Quantity'])

    # when we calc profit
    profit = episodeProcessor.final_balance(df)

    # then we get the expected total
    assert (profit == Decimal('30.87'))


def test_calc_episode_balance_with_rounding():
    # given a data frame with a Trade price column (price is a string to avoid float nonsense)
    df = pandas.DataFrame([['10.5233', 5], ['12.44', 5], ['8.33', 1], ['2', 1], ['13', -12]],
                          columns=['Trade Price', 'Trade Quantity'])

    # when we calc profit
    profit = episodeProcessor.final_balance(df)

    # then we get the expected total
    assert (profit == Decimal('30.85'))
