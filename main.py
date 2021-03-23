import click
import episodeLoader
import episodeProcessor
from columns import *


@click.command()
@click.option('--file', default='./sample_data/python_exercise_trades.csv', help='CSV file to load')
def click(file):
    data = episodeLoader.load_from_csv(file)
    profit = episodeProcessor.final_balance(data)
    print(profit)


if __name__ == '__main__':
    click()
