# Задача 1
# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата

def hex_num(num):
    hex_digit = '0123456789abcdef'
    hex_str = ''
    HEX = 16
    while num > 0 :
        hex_str = hex_digit[num % HEX] + hex_str
        num //= HEX
    return hex_str
while True:
    num = input('Введите число : ')
    if num.isdigit():
        num=int(num)
        break
    else:
        print('Вы ввели не число. Повторите ввод ')
hex_str = hex_num(num)
print(f"Шестнадцатеричное представление числа {num} - {hex_str}")