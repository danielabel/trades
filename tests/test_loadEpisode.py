from episode import episodeLoader
from datetime import datetime
from episode.columns import *


def test_sample_episode_file_loads_correct_shape():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert len(df.index) == 5
    assert len(df.columns) == 7


def trade_quantity_should_be_inputted_as_an_int():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert df.dtypes[TRADE_QUANTITY] == 'int64'


def test_trade_price_is_processed_to_string_for_safe_decimal_processing():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert df.dtypes[TRADE_PRICE] == object
    assert isinstance(df.iloc[0][TRADE_PRICE], str)


def test_trade_date_is_processed_to_date_format():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert df.dtypes[TRADE_DATE] == 'datetime64[ns]'
    assert df.iloc[0][TRADE_DATE] == datetime(2012, 1, 18), 'dates should be read in uk format'


def test_data_is_placed_in_date_order():
    df = episodeLoader.load_from_csv('tests/testdata/out_of_order_trades.csv')
    assert df.iloc[0][TRADE_IDENTIFIER] == 3649, 'row should be ordered first'
    assert df.iloc[-1][TRADE_IDENTIFIER] == 3671,  'row should be ordered last'
