import pandas
import episodeProcessor


def test_calc_episode_balance():
    # given a data frame with a Trade price column
    df = pandas.DataFrame([[10, 5], [12, 5], [8, 1], [2, 1], [13, -12]], columns=['Trade Price', 'Trade Quantity'])

    # when we calc profit
    profit = episodeProcessor.final_balance(df)

    # then we get the expected total
    assert (profit == 36)
