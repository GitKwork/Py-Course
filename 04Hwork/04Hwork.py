# 1.Создать и заполнить файл случайными целыми значениями. Выполнить сортировку содержимого файла по возрастанию.
#

import random
print('###### HW4 - Задание 1 ######')
with open('file_numbers4.txt', 'w') as data:
    for x in range(0, 20):
        data.write(str(random.randint(0, 100)) + " ")
path = 'file_numbers4.txt'
data = open(path, 'r')
all_numb = []
for line in data:
    print(line)
    all_numb.extend([int(item) for item in line.split()])
all_numb = sorted(all_numb)
data.close()
with open('file_numbers_sorted4.txt', 'w') as data:
    for y in all_numb:
        data.write(str(y) + ' ')
    print(f'отсортированный список = \n {all_numb}')
data.close()
print('******************************\n')


# 2.Дан список чисел. Создать список в который попадают числа, описывающие возрастающую последовательность и
# содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
# [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

print('###### HW2 - Задание 2 ######')
n_list = [1, 5, 2, 3, 4, 6, 1, 7]
# n_list = [5, 2, 3, 4, 6, 1, 7] # - alternative to test
print(n_list)
temp = list(range(len(n_list)+1))
temp2 = []
temp3 = []
for i in range(len(n_list)):
    temp.append(n_list[i])
    for k in range(i, len(n_list)-1):
        temp2.clear()
        temp2.append(n_list[i])
        temp.clear()
        temp.append(n_list[i])
        for j in range(k+1, len(n_list)):
            if n_list[j] >= n_list[i] and n_list[j] > temp[-1]:
                temp.append(n_list[j])
                temp2.append(n_list[j])
                temp3.append(temp2.copy())
max_list = max(temp3, key=len)
print(f'список возрастающей последовательностью и макс количеством элементов = \n {max_list}')
print('******************************\n')




# Экстра-задачи:
# 1.Давайте представим, что ваша компания только что наняла вашего друга из колледжа и заплатила вам реферальный бонус. Потрясающе! Чтобы отпраздновать, вы берете свою команду в очень странный бар по соседству и используете реферальный бонус, чтобы купить и построить самую большую трехмерную пирамиду из пивных банок, которую вы можете.
# Пирамида пивных банок будет квадратировать количество банок на каждом уровне - 1 банка на верхнем уровне, 4 на втором, 9 на следующем, 16, 25...
# Определите функцию beeramid, чтобы вернуть количество полных уровней пирамиды пивных банок, которую вы можете сделать, учитывая параметры: реферальный бонус и цена пивной банки.
# Например:
# beeramid(1500, 2)# 12
# beeramid(5000, 3)# 16
#
# 2.Создать функцию, которая из списка чисел возвращает число, являющее суммой двух или нескольких других элементов, либо возвращающее None, если такого числа нет.
# 3. Вот вам файл с английскими именами. https://cloud.mail.ru/public/J7aq/iHnLspVJR
# Начните с сортировки в алфавитном порядке. Затем подсчитайте алфавитные значения каждого имени и умножьте это значение на порядковый номер имени в отсортированном списке для получения количества очков имени.
#
# Например, если список отсортирован по алфавиту, имя COLIN (алфавитное значение которого 3 + 15 + 12 + 9 + 14 = 53) является 938-м в списке. Поэтому, имя COLIN получает 938 × 53 = 49714 очков.
#
# Какова сумма очков имен в файле?