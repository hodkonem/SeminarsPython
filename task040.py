"""
Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
"""
import pandas as pd

# загружаем датасет
dataset = pd.read_csv('sample_data/california_housing_train.csv')

# фильтруем датасет, чтобы оставить только те строки, где population <= 500
filtered_dataset = dataset[dataset['population'] <= 500]

# вычисляем среднюю стоимость дома в отфильтрованном датасете
mean_house_value = filtered_dataset['median_house_value'].mean()

# выводим результат
print("Средняя стоимость дома, где количество людей от 0 до 500: $", round(mean_house_value, 2))