import episodeLoader
import episodeProcessor

data = episodeLoader.load_from_csv('./sample_data/python_exercise_trades.csv')
print(data)
profit = episodeProcessor.final_balance(data)
print(profit)
