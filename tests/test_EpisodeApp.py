import os
from decimal import Decimal
from episode.EpisodeApp import EpisodeApp


def test_app_calculates_profit_from_sample_file():
    a = EpisodeApp('sample_data/python_exercise_trades.csv')
    assert a.balance == Decimal('40331.44')


def test_plot_generates_a_file(tmp_path):
    a = EpisodeApp('sample_data/python_exercise_trades.csv')
    pdf_path = tmp_path / 'plot.pdf'
    a.plot_episode(pdf_path)
    assert os.path.exists(pdf_path)
