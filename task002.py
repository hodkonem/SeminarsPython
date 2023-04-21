# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

number = input("Введите трехзначное число: ")
   
digit_sum = sum(int(digit) for digit in number)
    
print("Сумма цифр числа", number, "равна:", digit_sum)