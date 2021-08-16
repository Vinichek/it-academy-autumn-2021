'''Определите, является ли число палиндромом (читается слева направо и справа налево одинаково).
Число положительное целое, произвольной длины.
Задача требует работать только с числами (без конвертации числа в строку или что-нибудь еще)
'''

print('Введите целое положительное число')
number = int(input())
n = number
turn_over = 0
while n > 0:
    turn_over = turn_over * 10 + n % 10
    n //= 10
if number == turn_over:
    print('Число', number, '- палиндром')
else:
    print('Число', number, 'не является числом палиндромом')
