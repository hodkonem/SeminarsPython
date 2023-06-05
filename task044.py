"""
| Задание 44 |
| --- |
| В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI'lst})
data.head() |
"""

import random
import pandas as pd

# Создаем DataFrame с признаками категорий
lst = ['robot'] * 10
lst += ['human'] * 10
lst += ['belka'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Создаем словарь для one-hot кодирования
categories = sorted(data['whoAmI'].unique())
one_hot_dict = {cat: (data['whoAmI'] == cat).astype(int) for cat in categories}

# Создаем DataFrame из словаря
one_hot_df = pd.DataFrame(one_hot_dict)

# Выводим результат
print(one_hot_df)