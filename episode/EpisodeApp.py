from episode import episodeLoader, episodeProcessor
from episode.columns import *


class EpisodeApp:
    def __init__(self, file):
        self._data = episodeLoader.load_from_csv(file)
        self.balance = episodeProcessor.final_balance(self._data)

    def plot_episode(self, plot_path):
        episodeProcessor.add_quantity_held(self._data)
        self._data.plot.area(x=TRADE_DATE, y=QUANTITY_HELD).get_figure().savefig(plot_path, format='pdf')
