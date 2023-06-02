"""Задача 42: Узнать какая максимальная households в зоне минимального значения population"""

import pandas as pd

# загрузка данных из файла
df = pd.read_csv('california_housing_train.csv')

# нахождение максимального значения households в зоне минимального значения population
result = df[df['population'] == df['population'].min()]['households'].max()

# вывод результата
print("Максимальное количество households в зоне минимального значения population: ", result)
