# <- этот символ (решётка) означает комментирование. Все символы после решётки и до конца строки не исполняются.

# __________________ типы данных и функция print() __________________

# Начнём с классики программирования и выведем на экран фразу Hello world.
# С этого по традиции начинается изучение любого языка программирования. (чтобы увидеть основные принципы языка)
print('Hello world')

# В print() можно передавать строки, числа, списки, словари, кортежи, множества, булевы значения,
# а также объекты в которых реализована функция __str__() и переменные, все это содержащие.

# Строки(текст) заключаются в кавычки, одинарные, либо двойные.
print('Я строка', "Я тоже строка")

# Числа не заключаются в кавычки.
print(322)

# Списки заключаются вот в такие скобочки - []
print(['AllYourBaseAreBelongToUs', 1337, 'Можно положить в массив... еще один массив ->', ['Я еще один массив, привет']])

# Словари заключаются в такие скобки - {}.
# В словаре есть как значение, так и ключ, по которому к значению можно обратиться
print({'Я ключ словаря': 'А я значение', 'ключи должны быть уникальны': 'А значения не обязательно'})

# Кортежи - это просто значения, перечисленные через запятую.
# Лучше всего заключить кортеж в скобки (), хотя это не всегда обязательно (при записи кортежа в переменную, например)
print(('Я кортеж с одним элементом, видишь запятую, без нее я строка ->',), ('А я кортеж', 'с двумя элементами'))

# Множества заключаются в кавычки {}, но в них есть только значения. Притом только уникальные.
print({'Только', 'уникальные', 'значения', 'попадут', 'на', 'экран', 'порядок не сохранится', 'уникальные', 'попадут'})

# Булевы значения - это только False или True
print(True, False, True, True)

# Мы только что познакомились с примитивами в языке Python.
# Примитивы - это основные типы данных, с помощью которых мы храним информацию по ходу выполнения алгоритмов.
# Также мы познакомились с функцией print, теперь мы умеем выводить данные в консоль.
# Чтобы узнать насколько python прост, можете загуглить примеры Hello world на других языках (C, Java, C++ и т.п.)
