# __________________ условия __________________
print('__ условия __')
# Любое программирование начинается с условий: если то - сделай сё, а иначе - сделай это и т.п.

# Приведем пример:
test_variable = 'то'

if test_variable == 'то':
    print('сделай сё')
else:
    print('сделай это')

# Обратите внимание на ключевые слова if и else, сравнение, а также на двоеточия, запомните этот синтаксис
# К слову, выражение == это сравнение на равенство. Любое сравнение возвращает булево значение: True или False

# Еще в сравнения бывают такими: != (не равно), > (больше), < (меньше), <= (меньше либо равно), >= (ну вы поняли)
# Подытожим - в условии должно оказаться либо True либо False, либо операция(объединение операций) их возвращающая.
# Можете так и написать True либо False, все сработает:

if True:
    print('Я попаду на экран')
if False:
    print('А я не попаду, блин(')
if 1 > 8:
    print('Я тоже не попаду на экран')
if 1 < 8:
    print('А я попаду на экран, да еще как!')

# Условие можно не дописывать, если в случае невыполнения условия ничего делать не надо (нет else части)

# Кстати, чтобы проверить, что объект определен (переменная не равна None) мы используем особый синтаксис:
if test_variable is not None:
    print('test_variable не равен None')
# Или
if test_variable is None:
    print('test_variable равен None')
# То есть если дословно, то мы проверяем является ли объект внутри переменной test_variable объектом типа None

# Чем == отличается от is спросите вы.
# Тут все просто: == проверяет на равенство значений в двух объектах, а is проверяет идентичность объектов
# Другими словами с помощью is мы проверяем что "по двум адресам живет один и тот же объект"


# А теперь настало время питоновского рок-н-ролла, который выгодно отличает его от множества других языков
# Такой способ написания называется Pythonic way
# Условие сделай сё/это можно записать в одну строку и все будет выглядеть логично для человека

print('сделай сё') if test_variable == 'то' else print('сделай это')

# Так и читаем это в строку: Выведи на экран 'сделай сё', если test_variable равна 'то', а иначе выведи 'сделай это'
# Благодаря Pythonic way написанию алгоритмов вы существенно сокращаете количество кода в своих программах
# Загуглите это словосочетание, если интересно и посмотрите, что еще вы можете сделать подобным способом

# Остановимся на этом и перейдем к выполнению первой лабораторной работы в файле lab_1.py