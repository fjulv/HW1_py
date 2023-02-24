# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no


number = int(input("Введи шестизначный номер билета: "))
second = number%10 + int((number/10)%10)+ int(((number/100)%10))
first = int((number/1000)%10) + int((number/10000)%10) + int((number/100000)%10)
if first == second:
    print("Поздравляю, у Вас счастливый билет!")
else:
    print("К сожалению, билет не является счастливым. Повезет в другой раз!")