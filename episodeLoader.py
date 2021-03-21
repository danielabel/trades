import pandas as pd

def load_from_csv(path_to_file):#
    frame = pd.read_csv(path_to_file, dtype={'Trade Price': str})
    frame['Trade Date'] = pd.to_datetime(frame['Trade Date'], format='%d/%m/%Y')
    frame.sort_values(by=['Trade Date', 'Trade Identifier'], inplace=True)

    return frame
