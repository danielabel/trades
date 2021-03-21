import episodeLoader
from datetime import datetime


def test_sample_episode_file_loads_correct_shape():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert (len(df.index) == 5)
    assert (len(df.columns) == 7)


def test_types_for_key_columns():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert (df.dtypes['Trade Quantity'] == 'int64')
    assert (df.dtypes['Trade Date'] == 'datetime64[ns]')


def test_trade_price_is_processed_to_string_for_safe_decimal_processing():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert (df.dtypes['Trade Price'] == object)
    assert (isinstance(df.iloc[0]['Trade Price'], str))


def test_trade_date_is_processed_to_date_format():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert (df.iloc[0]['Trade Date'] == datetime(2012, 1, 18))


def test_data_is_placed_in_date_order():
    df = episodeLoader.load_from_csv('tests/testdata/out_of_order_trades.csv')
    assert (df.iloc[0]['Trade Identifier'] == 3649)
    assert (df.iloc[-1]['Trade Identifier'] == 3671)
