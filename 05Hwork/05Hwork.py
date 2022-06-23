# 1. Напишите программу, удаляющую из текста все слова содержащие "абв", которое регистронезависимо.
# Используйте знания с последней лекции. Выполните ее в виде функции.
# Пример: «абвгдеж рабав копыто фабв Абкн абрыволк аБволк»
#

print('###### HW5 - Задание 1 ######')
text1 = 'абвгдеж рабав копыто фабв Абкн абрыволк аБволк'
text2 = 'абв'
print(text1)
print(text2)
def abw_removed(text1, text2):
    list1 = text1.split(' ')
    list2 = list(filter(lambda word: text2.lower() not in word.lower(), list1))
    return ' '.join(list2)
print(abw_removed(text1, text2))
print('******************************\n')

# 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.

print('###### HW5 - Задание 2 ######')
print("-" * 5, " Игра Крестики ", "-" * 5)
board = list(range(1, 10))

def draw_board(board):
    print("-" * 13)
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3], "|")
        print("-" * 13)

def take_input(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(board[player_answer - 1]) not in "XO"):
                board[player_answer - 1] = player_token
                valid = True
            else:
                print("Эта клетка уже занята!")
        else:
            print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)

main(board)
input("Нажмите Enter для выхода!")
print('******************************\n')

# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется.
# Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче,
# из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут,
# короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем,
# в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.
#
print('###### HW5 - Задание 3 ######')
initial_text = 'Ну, вышел я,  из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем.Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо.Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил'
filter_excluding = ['ну', 'В общем', 'короче говоря', 'кажется', 'иду я','ээ','_э' ,'короче,', ',кажется', 'в общем', 'ясен пень', 'как бы', 'кстати', 'короче', '... ,', '….','…', '...',', ,', ', _', '_,' ]
print("-" * 25, " Исходный текст", "-" * 25, '\n')
print(initial_text)
print("-" * 25, " Мусорные слова ", "-" * 25, '\n')
print(filter_excluding)
print("-" * 25, " Нормальный текст ", "-" * 25,'\n')

def filter_text(initial_text, filter_excluding):
    for trash in filter_excluding:
        initial_text = initial_text.casefold().replace(trash, '_')
    initial_text = initial_text.replace('я,', 'я')
    initial_text = initial_text.replace('_','')
    initial_text = initial_text.replace('  ',' ')
    initial_text = initial_text.split('.')
    sentences = []
    for sentence in initial_text:
      sentence = sentence.strip()
      if not sentence: continue
      sentences.append(sentence.capitalize())

    result_text = '. '.join(sentences) + '.'
    return result_text
print(filter_text(initial_text, filter_excluding))
print('******************************\n')


# 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один с названиями языков программирования,
# другой — с числами от 1 до длины первого плюс 1. Вам нужно сделать две функции: первая из которых создаст список кортежей,
# состоящих из номера и языка, написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице,
# в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.
#Приписка: По домашнему заданию номер 4:
# 1. Список из чисел от 1 до длины первого плюс один - это опечатка. Для списка из двух языков:
# ['python', 'go']
# [1, 2]
# 2. Список кортежей, состоящих из номера и языка:
# [(1, 'python'), (2, 'go')]
# 3. По поводу таблицы - да поможет вам функция ord.
#

print('###### HW5 - Задание 4 ######')
all_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abc_cost = {all_letters[i]: i + 65 for i in range(len(all_letters))}

p_lang = ['Python', 'C', 'Java', 'Go', 'PHP', 'JavaScript', 'ObjectiveC', 'Perl']
list1 = list(range(1, len(p_lang)+1))
print("-" * 25, " 2 списка ", "-" * 25, '\n')
print(p_lang)
print(list1)

def Function1(list1, list2):
    return [(list1[i], list2[i].upper()) for i in range(len(list1))]

def Function2(list3):
    return [list([sum_points(list3[i][1]), list3[i][1]]) for i in range(len(list3)) if sum_points(list3[i][1]) % list3[i][0] == 0]

def sum_points(string):
    return sum([abc_cost[string[i]] for i in range(len(string))])

print("-" * 25, " функция1 ", "-" * 25, '\n')
print(Function1(list1, p_lang))
print("-" * 25, " функция2 ", "-" * 25, '\n')
print(Function2(Function1(list1, p_lang)))
print('******************************\n')














#