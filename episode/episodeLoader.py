import pandas as pd
from episode.columns import *


def load_from_csv(path_to_file):
    frame = pd.read_csv(path_to_file, dtype={TRADE_PRICE: str})
    frame[TRADE_DATE] = pd.to_datetime(frame[TRADE_DATE], format='%d/%m/%Y')
    frame.sort_values(by=[TRADE_DATE, TRADE_IDENTIFIER], inplace=True)
    return frame
