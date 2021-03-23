import click
import episodeLoader
import episodeProcessor
from columns import *


@click.command()
@click.option('--file', default='./sample_data/python_exercise_trades.csv', help='CSV file to load')
@click.option('--plot', default='plot.pdf', help='file to save plot of episode to')
def click(file, plot):
    data = episodeLoader.load_from_csv(file)
    profit = episodeProcessor.final_balance(data)
    print(profit)

    episodeProcessor.add_quantity_held(data)
    data.plot.area(x=TRADE_DATE, y=QUANTITY_HELD).get_figure().savefig(plot)


if __name__ == '__main__':
    click()
