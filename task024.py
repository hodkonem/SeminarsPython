# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.



from random import randint

n = int(input('Введите кол-во кустов: '))
while n <= 0:
    print('Введено некорректное число, попробуйте ещё раз')
    n = int(input('Введите кол-во кустов: '))

list_1 = [randint(1, 5) for i in range(n)]
print('Количество ягод на каждом кусте:', list_1)

num = int(input('Введите номер куста: '))
while num <= 0 or num > n:
    print('Введено некорректное число, попробуйте ещё раз')
    num = int(input('Введите номер куста: '))

if num == 1 and n == 1:
    print('Это единственный куст, соседей нет')
elif num == 1:
    print('Количество ягод на заданном кусте:', list_1[num-1])
    print('Количество ягод на следующем кусте:', list_1[num])
elif num == n:
    print('Количество ягод на заданном кусте:', list_1[num-1])
    print('Количество ягод на предыдущем кусте:', list_1[num-2])
else:
    print('Количество ягод на заданном кусте:', list_1[num-1])
    print('Количество ягод на предыдущем кусте:', list_1[num-2])
    print('Количество ягод на следующем кусте:', list_1[num])