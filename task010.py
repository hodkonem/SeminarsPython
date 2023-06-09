# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

n = int(input())  # считываем количество монет
coins = input()   # считываем порядок решек и гербов на монетах
heads = coins.count('1')  # считаем количество монет с решкой
tails = coins.count('0')  # считаем количество монет с гербом
print(min(heads, tails))