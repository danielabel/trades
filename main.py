import click
from EpisodeApp import EpisodeApp


@click.command()
@click.option('--file', default='./sample_data/python_exercise_trades.csv', help='CSV file to load')
@click.option('--plot', default='plot.pdf', help='file to save plot of episode to')
def click(file, plot):
    app = EpisodeApp(file)
    app.plot_episode(plot)
    print(app.balance)


if __name__ == '__main__':
    click()
