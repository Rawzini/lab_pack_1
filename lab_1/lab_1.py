# В питоне можно импортировать всяческие модули, как встроенные, так и сторонние в свою программу
# К слову каждый отдельный файл - это модуль, example_1_1.py, example_1_2.py, example_1_3.py - это тоже модули
# Мы импортируем встроенный модуль random для получения случайного числа
import random

# В этом модуле есть функция randint, которая может генерировать случайное число в заданном диапазоне
variable = random.randint(0, 100)
print('variable: ', variable)
# Это все было подготовительной частью для написания лабораторной работы, перейдем к самому заданию

# Напишите мне одну строку, которая при условии, что variable > 50 выводит на экран 'Я больше 50'
# а в противном случае 'Я меньше 50'

