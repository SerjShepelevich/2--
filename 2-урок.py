#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''
print('Задача №1')
for i in range(1,6):
    print(i,'000000000')
    i+=1
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
'''
print('')
print('Задача №2')
print("Введите 10 цифр от 1 до 10 в разной последовательности, программа считает введенные цифры 5")
a = 0
for x in range(10):
    y = int(input())
    if y == 5:
        a += 1
print('Ввели цифру пять ',a,' раз(a)')

'''
'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

print('')
print('Задача №3')
# sum = 0
#
# for i in range(1,101):
#     sum+=i
# print(sum)
sum = 0
a = 0
while a < 101:
    sum+=a
    a+=1
print('Сумма = ',sum)
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''
print('')
print('Задача №4')
sum = 1
for i in range(1,11):
    sum = sum * i
print("произведение ряда чисел от 1 до 10 = ",sum)

'''
Задача 5
Вывести цифры числа на каждой строчке.
'''
print('')
print('Задача №5')

integer_number = 45345345
print('Исходное число ',integer_number)
#print(integer_number%10,integer_number//10)
while integer_number>0:
    print(integer_number%10)
    integer_number = integer_number//10

'''
Задача 6
Найти сумму цифр числа.
'''

print('')
print('Задача №6')

integer_number = 45345345
print('Исходное число ',integer_number)
#print(integer_number%10,integer_number//10)
sum = 0
while integer_number>0:
    sum += integer_number%10
    integer_number = integer_number//10
print('Сумма чисел числа = ',sum)

'''
Задача 7
Найти произведение цифр числа.
'''

print('')
print('Задача №7')

integer_number = 45345345
print('Исходное число ',integer_number)
#print(integer_number%10,integer_number//10)
sum = 1
while integer_number>0:
    sum *= integer_number%10
    integer_number = integer_number//10
print('Произведение чисел числа = ',sum)


'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print('')
print('Задача №8')

integer_number = 45345345
print('Исходное число ',integer_number)

while integer_number>0:
    if integer_number%10 == 5:
        print('Yes')
        break
    integer_number = integer_number//10
else: print('No')

'''
Задача 9
Найти максимальную цифру в числе
'''
print('')
print('Задача №9')

integer_number = 49585345
print('Исходное число ',integer_number)
x = 0
while integer_number>0:
    if integer_number%10 > x:
        x = integer_number%10
    integer_number = integer_number//10
print ('максимальное число = ', x)

'''
Задача 10
Найти количество цифр 5 в числе
'''
print('')
print('Задача №10')
integer_number = 49585345
print('Исходное число ',integer_number)

from collections import Counter
print('Цифра 5 есть = ',Counter(list(str(integer_number)))['5'], " раз")