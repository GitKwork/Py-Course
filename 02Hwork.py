# Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
#
print('###### HW2 - Задание 1 ######')
print('Введите числа')
N_int = [int(x) for x in input().split()]
print(N_int)
sum_n = 0
for i in range(0, len(N_int)-1, 2):
    sum_n += N_int[i]
print(f'сумму чисел списка стоящих на нечетной позиции={sum_n}\n')
print('******************************\n')

# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
#
print('###### HW2 - Задание 2 ######')
print('Введите числа')
N_int2 = [int(y) for y in input().split()]
print(N_int2)
mult_n = list(range((len(N_int2)+1)//2))
for i in range(0, (len(N_int2)+1)//2):
    mult_n[i] = N_int2[i] * N_int2[len(N_int2)-1-i]
print(f'произведение пар чисел в списке={mult_n}\n')
print('******************************\n')


# В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
print('###### HW2 - Задание 3 ######')
print('Введите вещественные числа')
n_flt = [float(z) for z in input().split()]
n_flt = list[float]
n_new = list[float]
print(n_flt)
# n_df = list(range(len(n_flt)))
def ndif(mas):
    for i in range(0, len(mas)):
        n_new[i] = [mas[i] - math.trunc(mas[i])]
    return max(n_new) - min(n_new)
f = ndif(n_flt)
print(f'разницу между максимальным и минимальным значением дробной части={f}\n')
print('******************************\n')

# Написать программу преобразования десятичного числа в двоичное
#
print('###### HW2 - Задание 4 ######')
print('Введите числа в десятичной форме:')
num_dec = int(input())
num_bin = ''
while num_dec > 0:
    num_bin = str(num_dec % 2) + num_bin
    num_dec = num_dec // 2

print(f'двоичное число = {num_bin}\n')
print('******************************\n')


# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.
#
# 2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:
#
# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число. За каждую цифру, которую пользователь правильно угадал в нужном месте, у них есть “корова”. За каждую цифру, которую пользователь угадал правильно, в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает предположение, скажите им, сколько у них “коров” и “быков”. Как только пользователь угадает правильное число, игра окончена. Следите за количеством догадок, которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.
#
# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.
# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?
# 5.2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.Какое самое маленькое число делится нацело на все числа от 1 до 20?
