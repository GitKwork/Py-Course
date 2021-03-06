# 1 - необязательно формировать список перед тем, как сделать список. Пользуйтесь методом append и наполняйте изначально пустой
# 2 - старайтесь не повторять свой собственный код. Чтобы избежать повторения, можно было сразу узнать, какая строка больше.
# main_string, text2 = max(str1, str2, key=len), min(str1,str2, key=len)
# 3- весьма хорошо, только забыли учесть отрицательные числа
# 4 - тоже верно



# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

print('###### HW1 - Задание 1 ######')
print('Введите N=')
N = int(input())
Nl = list(range(N))
Nl[0] = 1
for i in range(1, N):
    Nl[i] = (-3)**i
print(f'список из N={N} членов последовательности:\n{Nl}')
print('******************************\n')


# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

print('###### HW1 - Задание 2 ######')
print('Введите строку №1:')
str1 = str(input())
print('Введите строку №2:')
str2 = str(input())
index = -1
count = 0
if str1 == str2:
    print('Строки однаковы')
elif len(str1) > len(str2):
    while True:
        index = str1.find(str2, index+1)
        if index == -1:
            break
        count += 1
    print(f'вторая страка входит в первую {count} раз')
else:
    while True:
        index = str2.find(str1, index+1)
        if index == -1:
            break
        count += 1
    print(f'первая строка входит во вторую {count} раз')
print('******************************\n')



# # Подсчитать сумму цифр в вещественном числе.

print('###### HW1 - Задание 3 ######')
print('Введите вещественном число N=')
No = float(input())
Ns = str(No)
Ns = Ns.replace(".", "")
Sum = 0
for elm in Ns:
    Sum += int(elm)
print(f'сумма цифр в вещественном числе {No} = {Sum}')
print('******************************\n')



# # Написать программу получающую набор произведений чисел от 1 до N.
# # Пример: пусть N = 4, тогда  [ 1, 2, 6, 24 ]


print('###### HW1 - Задание 4 ######')
print('Введите N=')
Nr = int(input())
Nls = list(range(Nr))
Nls[0] = 1
for j in range(1, Nr):
    Nls[j] = Nls[j-1]*(j+1)
print(Nls)
print('******************************\n')

exit()



# Для тех, кому этих задач будет мало, еще несколько не слишком сложных для начала.
#* Экстра-задачи:
#
# 1. Написать функцию write_in_morse, которая принимает строку на английском языке и возвращает ее перевод на символьный язык Морзе. Ввод не должен зависеть от регистра.
# Да поможет вам этот словарь:
# char_to_dots = {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }
#





# 2. Есть такая вещь - палиндром. Это когда слово читается с обеих сторон одинаково. Например, слово "шалаш". Также есть числовой палиндром. Если при обратном чтении числа (124 - 421) не получается то же самое, то они складываются (124+421) и проверяются вновь. Попробуйте написать функцию (или просто программу, но лучше все же функцию), находящую числовой палиндром.
#





# 3. Напишите программу, смысл которой вот в чем. Программа загадывает вам число из ограниченного диапазона. Ваша цель — отгадать это за log(количество вариантов) попыток. Подсказками компьютера могут служить слова «больше» или «меньше»
#





# 4. Напишите программу, обратную предыдущей: теперь вы загадываете число, а компьютер отгадывает.
#






# 5. Эта задача больше на интерес и «для души». Попробуйте написать текстовый квест, где он выбранных ответов зависит исход игры. Подходит людям с писательскими способностями. Пример:
#
# >>> Ты просыпаешься. Оценив взглядом помещение, ты понимаешь, что это явно не твоя комната. Нужно выбраться отсюда. Перед тобой — невзрачный шкаф, стоящий посередине  стены, дверь, на которой почему-то весит замок, стол и окно. Куда подойдешь?
# >>> Дверь
# >>>Ты подошел к двери. На ней кодовый замок из 4 цифр. Ввести код или попробовать сбить его?
# >>>Попробовать сбить
# >>>Вы наделали много шума, но результата это не дало. Попробовать ввести код?
# >>> Да
# >>>Код:
# >>>5386
# >>>Неверно
# >>>5347
# >>>Неверно
# >>>Назад
# >>>Перед тобой — невзрачный шкаф, стоящий посередине стены, дверь, на которой почему-то весит замок, стол и окно. Куда подойдешь?
# >>> Стол
# >>> На столе есть фотография. На ней — какой-то улыбающийся мальчик. Есть также какая-то папка, органайзер с ручками и ваза. Что хочешь осмотреть?
# >>> Осмотреть фотографию.
# >>> На обороте написано: «Коленьке 6 лет. 06.11.2004»
# >>> Назад
# >>> Перед тобой — невзрачный шкаф, стоящий посередине стены, дверь, на которой почему-то весит замок, стол и окно. Куда подойдешь?
# >>> Дверь
# >>>Ты подошел к двери. На ней кодовый замок из 4 цифр. Ввести код или попробовать сбить его?
# >>>Ввести код
# >>> Код:
# >>> 0611
# >>>Замок открывается. Ты тянешь ручку двери на себя, дверь открывается. Ты оказываешься в коридоре. Слышишь рычание. Оборачиваешься и видишь жуткого зверя. Видимо, ты издал слишком много шума, чем привлек его внимание или пробудил ото сна. Кажется, это конец. Или нет?
# >>> Конец игры. Открыта одна из концовок.