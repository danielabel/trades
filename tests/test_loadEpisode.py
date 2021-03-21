import episodeLoader


def test_sample_episode_file_loads_correct_shape():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert (len(df.index) == 5)
    assert (len(df.columns) == 7)


def test_types_for_key_columns():
    df = episodeLoader.load_from_csv('tests/testdata/trades.csv')
    assert (df.dtypes['Trade Quantity'] == 'int64')
    assert (df.dtypes['Trade Price'] == 'float64')
