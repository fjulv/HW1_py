# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, 
# если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

total = int(input('Введи количество журавликов, которое сделали дети вместе '))
if total % 6 != 0:
    print("Введенное количество сделанных журавликов не соответствует условиям задачи")
else:
    x = total / 6
    print(f'Петя сделал {x} журавликов')
    print(f'Сережа сделал {x} журавликов')
    print(f'Катя сделала {4 * x} журавликов')