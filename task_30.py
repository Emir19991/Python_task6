# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# n = int(input('Input n ')) #общее кол-во эл-в
# x = int(input('Input a[0] '))
# d = int(input('Input d ')) #шаг
# print(*range(x, x + d * n, d))


a1 = 7
d = 2
n = 5
for i in range(n):
    print(a1 + i * d, end=' ')