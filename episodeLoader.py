import pandas as pd


def load_from_csv(pathToFile):
    frame = pd.read_csv(pathToFile)
    return frame
