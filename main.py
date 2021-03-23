import click
from EpisodeApp import EpisodeApp


@click.command()
@click.option('--file', default='./sample_data/python_exercise_trades.csv', help='CSV file to load')
@click.option('--plot', default='plot.pdf', help='file to save plot of episode to')
def click(file, plot):
    try:
        app = EpisodeApp(file)
        app.plot_episode(plot)
        print(app.balance)
    except KeyError as e:
        print("Data file format not compatible - is there a column missing: ", str(e))
    except Exception as e:
        print("failed to process data. Error:", str(e))


if __name__ == '__main__':
    click()
