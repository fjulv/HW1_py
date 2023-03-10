# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введи количество долек по длине плитки шоколада: '))
m = int(input('Введи количество долек по ширине плитки шоколада: '))
k = int(input('Введи количество долек, которые хочешь отломить: '))

if (k % n == 0 or k % m == 0) and k < n*m:
    print(f'От шоколадки размером {n}x{m} можно отломить {k} долек(-ки) с помощью одного разлома по прямой между дольками')
else:
    print(f'От шоколадки размером {n}x{m} нельзя отломить {k} долек(-ки) с помощью одного разлома по прямой между дольками')