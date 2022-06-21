#
# def numerals(number):
#     if 0 < number < 13:
#         list_of_numeral = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
#         day = list_of_numeral[number-1]
#         return day
#
# def couplet (couplet_num):
#     print(f"On the {numerals(couplet_num)} day of Christmas \n"
#           f"my true love sent to me:")
#     if couplet_num == 1:
#         print("A partridge in a pear tree.")
#     else:
#         i = 0
#         for i in range(couplet_num-2, -1, -1):
#             couplet_strings = [
#                 "Two turtle doves,",
#                 "Three French hens,",
#                 "Four calling birds,",
#                 "Five golden rings,",
#                 "Six geese a-laying,",
#                 "Seven swans a-swimming,",
#                 "Eight maids a-milking,",
#                 "Nine ladies dancing,",
#                 "Ten lords a-leaping,",
#                 "Eleven pipers piping,",
#                 "Twelve drummers drumming,",
#                 ]
#             n = i
#             mean_of_string = couplet_strings[n]
#             print(mean_of_string)
#             i += 1
#         print("And a partridge in a pear tree.")
# number = int(input("Введите номер кумплета:"))
# couplet(number)

# def capital_letter(sentens):
#      print(sentens[0].upper(), end="")
#      i = 1
#      for i in range(1, len(sentens)):
#           if i + 2 < len(sentens):
#                if (sentens[i-2] =="." or sentens[i-2] == "!" or sentens[i-2] == "?") and sentens[i-1] == " ":
#                     print(sentens[i].upper(), end="")
#                     i += 1
#                elif sentens[i] == 'i' and (sentens[i-1] == " " or sentens[i+1] == " " or sentens[i+1] =="." or sentens[i+1] =="!" or sentens[i+1] =="?"):
#                     print("I", end="")
#                     i +=1
#                else:
#                     print(sentens[i], end="")
#                     i += 1
#           else:
#                print(sentens[i], end="")
#                i +=1
# capital_letter(input("Введите предложение:"))

# def capital_letter(sentens):
#      new_sentens = sentens[0].upper()
#      i = 1
#      for i in range(1, len(sentens)):
#           if i + 2 < len(sentens):
#                if (sentens[i-2] =="." or sentens[i-2] == "!" or sentens[i-2] == "?") and sentens[i-1] == " ":
#                     new_sentens = new_sentens + sentens[i].upper()
#                     i += 1
#                elif sentens[i] == 'i' and (sentens[i-1] == " " or sentens[i+1] == " " or sentens[i+1] =="." or sentens[i+1] =="!" or sentens[i+1] =="?"):
#                     new_sentens = new_sentens + "I"
#                     i +=1
#                else:
#                     new_sentens = new_sentens + sentens[i]
#                     i += 1
#           else:
#                new_sentens = new_sentens + sentens[i]
#                i +=1
#      return new_sentens
# old_sentens = input("Введите предложение:")
# new_sentens = capital_letter(old_sentens)
# print(old_sentens)
# print(new_sentens)

# def centering(sentens, width):
#      if len(sentens) > width:
#           return sentens
#      else:
#           space = (width-len(sentens))//2 * " "
#           center_sentens = space + sentens
#           return center_sentens
# for i in range(3):
#      s = input("Введите предложение")
#      w = int(input("Ввведите ширину окна"))
#      new_s = centering(s, w)
#      print(new_s)


# import prime
#
# def nextPrime(last_number):
#     while not prime.primenum(last_number):
#         last_number = last_number + 1
#     return last_number
#
# l_number = int(input("Введите число:"))
# prime_number = nextPrime(l_number)
# print(prime_number)

# def checking_pasword(password):
#     if len(password) < 8:
#         return None
#     number = 0
#     up_letter = 0
#     low_letter = 0
#     for ch in password:
#         if ch >= "A" and ch <= "Z":
#             up_letter += 1
#         elif ch >= "a" and ch <= "z":
#             low_letter += 1
#         elif ch >= "0" and ch <= "9":
#             number += 1
#     if number > 1 and up_letter > 2 and low_letter > 2:
#         return True
#     else:
#         return False
#
#
# user_password = input("Введите пароль:")
# chek_pass = checking_pasword(user_password)
# if chek_pass == True:
#     answer = "надежный"
# elif chek_pass == False:
#     answer = "не надежный"
# else:
#     answer = chek_pass
# print("Ваш пароль", answer)

# # Создаем список
# data = [2.71, 3.14, 1.41, 1.62]
# # Меняем местами элементы в списке с индексами 1 и 3
#
# data[1], data[3] = data[3], data[1]
# print(data)

# def del_extremum(values):
#     max_num = 0
#     min_num = 0
#     for i in range(len(values)):
#         if values[i] > values[max_num]:
#             max_num = i
#     values.pop(max_num)
#     for i in range(len(values)):
#         if values[i] < values[min_num]:
#             min_num = i
#     values.pop(min_num)
#     return values
# def input_of_values():
#     list_of_values = []
#     avarege_list = []
#     num = int(input("Введите значение (больше 4х, для остановки введите \"0\"): "))
#     while num != 0:
#         list_of_values.append(num)
#         num = int(input("Введите значение (больше 4х, для остановки введите \"0\"):"))
#     if len(list_of_values) < 4:
#         print("Введено меньше четырех значений")
#         return
#     else:
#         print(list_of_values)
#         avarege_list = del_extremum(list_of_values)
#         print(avarege_list)
#         repit = input("Убрать экстремумы еще раз \"Да\" или \"Нет\"")
#         while repit == "Да":
#             list_of_values = avarege_list
#             print(list_of_values)  # Не пойму, почему печатает одинаковые строки
#             avarege_list = del_extremum(list_of_values)
#             print(avarege_list) # Не пойму, почему печатает одинаковые строки
#             repit = input("Убрать экстремумы еще раз \"Да\" или \"Нет\:"")
#     return
# input_of_values()




# def double_del(double_list):
#     new_list = []
#     for compared in double_list:
#         if compared not in new_list:
#             new_list.append(compared)
#     return new_list
#
# list_of_words = []
# word = input("Введите слова (больше 4х, для остановки, нажмите Enter): ")
#


# print(list_of_words)
# sorted_list = double_del(list_of_words)
# print(sorted_list)



# positive = []
# negative = []
# zero = []
#
# values = input("Введите целые числа (для остановки нажмите Enter):")
# while values != "":
#     values = int(values)
#     if values > 0:
#         positive.append(values)
#     elif values == 0:
#         zero.append(values)
#     elif values < 0:
#         negative.append(values)
#     values = input("Введите целые числа (для остановки нажмите Enter):")
# input("Для вывода значений нажмите Enter")
# print(negative)
# print(zero)
# print(positive)


# def dividers(num):
#     i = 1
#     dividers_list = []
#     while i != num:
#         if num % i == 0:
#             dividers_list.append(i)
#         i += 1
#     return dividers_list
#
#
# def perfect_number(number):
#     list_of_dividers = dividers(number)
#     sum = 0
#     for div in list_of_dividers:
#         sum = sum + div
#     if sum == number:
#         return True
#     return False
#
#
# x = 1
# while x != 10000:
#     if perfect_number(x):
#         print(x)
#     x += 1


# def only_word(sentens):
#     invalid = [".", ",", ":", ";", " ", "?"]
#     word = str()
#     word_list = list()
#     for i in sentens:
#         if i not in invalid:
#             word = word+i
#         elif i == " " and word != "":
#             word_list.append(word)
#             word = str()
#     word_list.append(word)
#     return word_list
#
#
# def polidrom(sentens):
#     x = only_word(sentens)
#     y = x
#     y.reverse()
#     if x == y:
#         return True
#     return False
#
#
# x = polidrom("Is it crazy how saying sentences backwards creates b ckwards sentences saying how crazy it Is?".lower())
# print(x)


#   120

# def enumeration(list):
#     list.insert(-1, "и")
#     for i in range(-4, -len(list)-1, -1):
#         list[i] =list[i]+","
#     new_string = " ".join(list)
#     return new_string
# list_of_words = []
# word = input("Введите слово:")
# while word != "":
#     list_of_words.append(word)
#     word = input("Введите слово (для остановки, нажмите Enter):")
# enum_str = enumeration(list_of_words)
# print(enum_str)


#    121

# def winning_numbers(win_lenght = 6):
#     import random
#     win_list = []
#     while len(win_list) != win_lenght:
#         n = random.randint(1, 49)
#         if str(n) not in win_list:
#             win_list.append(str(n))
#         else:
#             continue
#     win_comb = " ".join(win_list)
#     return win_comb

# num_lenght = 6
# list_of_number = []
# i = 0
# for i in range(num_lenght):
#     num_ticket = input("Введите число:")
#     list_of_number.append(str(num_ticket))
#     i+=1
#
# you_ticket = " ".join(sorted(list_of_number))
# win_ticket = winning_numbers(num_lenght)
# print(win_ticket)
# print(you_ticket)


# 124


# def best_fit_line(x, y):
#     x_sum = 0
#     y_sum = 0
#     xy_sum = 0
#     x_sqr_sum = 0
#     x_average = 0
#     y_average = 0
#     for i in x: x_sum = x_sum + i
#     for i in y: y_sum = y_sum + i
#     for i, j in zip(x, y):
#         xy_sum = xy_sum + (i * j)
#     for i in x: x_sqr_sum = x_sqr_sum + i**2
#     m = (xy_sum - (x_sum * y_sum/len(x))) / (x_sqr_sum - (x_sum)**2 / len(x))
#     x_average = x_sum / len(x)
#     y_average = y_sum / len(y)
#     b = y_average - m*x_average
#     print("y = {} x + {}".format("%.2f" %m, "%.2f" %b))
#
# x_coord = []
# y_coord = []
# x = input("Введите X координату:")
# while x != "":
#     x_coord.append(float(x))
#     x = input("Введите X координату:")
# y = input("Введите Y координату:")
# while len(y) != len(x):
#     y_coord.append(float(y))
#     y = input("Введите Y координату:")
# best_fit_line(x_coord, y_coord)


#   125


# def createDeck():
#     card_deck = []
#     card_suit = ["s","h","d","c"]
#     card_value = ["T","J","Q","K","A"]
#     for i in range(2,10):
#         for j in card_suit:
#             card_deck.append(str(i)+j)
#     for i in card_value:
#         for j in card_suit:
#             card_deck.append(i+j)
#     return card_deck
#
# def shuffle(card_list):
#     cards = card_list
#     import random
#     for i in range(len(cards)):
#         j = random.randint(i, len(cards)-1)
#         cards[i], cards[j] = cards[j], cards[i]
#     return cards
# deck = createDeck()
# deck = shuffle(deck)
# print(deck)
#
# if __name__ == "__main__":
#     main()


#   126

#
# import shuffled_deck
#
# def card_distribution(players, cards):
#     cards_list = shuffled_deck.shuffle()
#     print(cards_list)
#     destribution = []
#     i=0
#     for i in range(players):
#         destribution.append([])
#     while len(destribution[-1]) != cards:
#         for j in range(players):
#             destribution[j].append(cards_list[0])
#             cards_list.pop(0)
#     for p in range(len(destribution)):
#         print("Player", p+1, destribution[p])
#     print(cards_list)
#
# players = int(input("Введите кол-во игроков:"))
# cards = int(input("Введите кол-во карт:"))
# card_distribution(players, cards)

#   133


# k = [1,2,3,4,5]
# l = []
# def sublist(larger, smaller):
#     if len(smaller) == 0:
#         return True
#     else:
#         i = 1
#         j = 0
#         n = 0
#         for i in range(len(larger)):
#             if larger[i] == smaller[j]:
#                 n += 1
#                 i += 1
#                 j += 1
#                 if len(smaller) == n:
#                     return True
#             else:
#                 i += 1
#                 n = 0
#         return False
#
# c = sublist(k,l)
# print(c)


#   134


# def sublist_gener(list):
#     if list == []:
#         return []
#     list_of_sublist = [[]]
#     temp_list = []
#     lenght = 1
#     while lenght != len(list):
#         i = 0
#         for i in range(len(list)):
#             cell = i
#             j = 0
#             temp_list = []
#             if i + lenght-1 < len(list):
#                 while j != lenght:
#                     temp_list.append(list[cell])
#                     cell += 1
#                     j += 1
#                 list_of_sublist.append(temp_list)
#             else:
#                 i += 1
#         lenght += 1
#     list_of_sublist.append(list)
#     return list_of_sublist
#
#
# a = [1, 2, 3, 4, 5, 6, 7, 9, 10]
# sublists = sublist_gener(a)
# for i in range(len(sublists)):
#     print(sublists[i])

#   138
#
# vocabulary = {
#     ".":"1",
#     ",":"11",
#     "?":"111",
#     "!":"1111",
#     ":":"11111",
#     "a":'2',
#     "b":'22',
#     "c":'222',
#     "d":'3',
#     "e":'33',
#     "f":'333',
#     "g":'4',
#     "h":'44',
#     "i":'444',
#     "j":'5',
#     "k":'55',
#     "l":'555',
#     "m":'6',
#     "n":'66',
#     "o":'666',
#     "p": '7',
#     "q": '77',
#     "r": '777',
#     "s": '7777',
#     "t": '8',
#     "u": '88',
#     "v": '888',
#     "w": '9',
#     "x": "99",
#     "y": '999',
#     "z": '9999',
#     " ": '0'}
# sentence = input("Введите предложение:")
# str_numbers = str()
# for x in sentence.lower():
#     if x in vocabulary:
#         str_numbers = str_numbers + vocabulary[x]
# print(str_numbers)

#    142

# def unique_symbols(text):
#     vocabularu_of_sym = {}
#     for x in text:
#         if x not in vocabularu_of_sym:
#             vocabularu_of_sym[x] = 1
#         else:
#             vocabularu_of_sym[x] += 1
#     return vocabularu_of_sym
# text = input("Предложение")
# t = unique_symbols(text)
# print(t)
#
# def card_gen():
#     import random
#     bingo_card = {"B":[], "I":[], "N":[], "G":[], "O":[]}
#     start = 1
#     stop = 16
#     for letter in bingo_card:
#         cell = 0
#         while 5 != len(bingo_card[letter]):
#             n = random.randint(start, stop)
#             if n not in bingo_card[letter]:
#                 bingo_card[letter].append(n)
#         start += 15
#         stop += 15
#     return bingo_card
#
# def card_print(b_card):
#     for x in b_card:
#         print(x.center(5), end="")
#     l = 0
#     while l != len(b_card["B"]):
#         print()
#         for x in b_card:
#             print(f"{b_card[x][l]}".center(5), end="")
#         l +=1
#     print()
#
# # card = card_gen()
# # card_print(card)
#
# def card_check(card):
#     for x in range(0, 5):
#         sum_horizont = 0
#         for letter in card:
#             sum_horizont = sum_horizont + card[letter][x]
#         if sum_horizont == 0:
#             return True
#     for letter in card:
#         sum_vertical = 0
#         for x in range(0, 5):
#             sum_vertical = sum_vertical + card[letter][x]
#         if sum_vertical == 0:
#             return True
#     n = 0
#     sum_diagonal_1 = 0
#     for letter in card:
#         sum_diagonal_1 = sum_diagonal_1 + card[letter][n]
#         n += 1
#     if sum_diagonal_1 == 0:
#         return True
#     n = -1
#     sum_diagonal_2 = 0
#     for letter in card:
#         sum_diagonal_2 = sum_diagonal_2 + card[letter][n]
#         n -= 1
#     if sum_diagonal_2 == 0:
#         return True
#     return False
#
# def game_gen():
#     from random import shuffle
#     start = 1
#     stop = 16
#     number_list = []
#     for letter in ["B","I","N","G","O"]:
#         for number in range(start, stop):
#             number_list.append(letter+str(number))
#             number += 1
#         start += 15
#         stop += 15
#     shuffle(number_list)
#     return number_list
#
# def num_del(card,win_number):
#     letter = win_number[0]
#     number = int(win_number[1:])
#     for i in range(0, 4):
#         if card[letter][i] == number:
#             card[letter][i] = 0
#     return card
#
# numbers_of_total_win = []
# games = 100
# x = 0
# while x!= games:
#     card = card_gen()
#     # card_print(card)
#     win_code = game_gen()
#     total_to_win = 0
#     for i in win_code:
#         # print(i, end=" ")
#         card = num_del(card, i)
#         if card_check(card):
#             # print()
#             # card_print(card)
#             break
#         total_to_win +=1
#     numbers_of_total_win.append(total_to_win)
#     x+=1
# print(numbers_of_total_win)
# print(min(numbers_of_total_win))
# print(max(numbers_of_total_win))
# avarage = sum(numbers_of_total_win)/len(numbers_of_total_win)
# print(avarage)

#  150

# import sys
#
# if len(sys.argv) < 2:
#     print("Имя файла необходимо передать в качестве", "аргумента.")
#     quit()
#
# try:
#     inf = open(sys.argv[1], "r")
#     line = inf.readline().rstrip()
#     tail = []
#     tail_len = int(sys.argv[2])
#     num = 1
#     while line != "":
#         if len(tail) < tail_len:
#             line = inf.readline().rstrip()
#             tail.append(line)
#             line = inf.readline().rstrip()
#             num +=1
#         elif len(tail) == tail_len:
#             tail.pop(0)
#             tail.append(line)
#             line = inf.readline().rstrip()
#             num += 1
#     inf.close()
#     k = num - tail_len
#     n = 0
#     while k != num:
#         print("%d : %s" % (k, tail[n]))
#         k += 1
#         n += 1
#     inf.close()
# except:
#     print("ОЙ, такого файла нет! Попробуйте еще раз.")


#  151 и 152

#
# import sys
#
# if len(sys.argv) < 2:
#     print("Имя файла необходимо передать в качестве аргумента.")
#     quit()
# n = 2
# inf = []
# while n != len(sys.argv):
#     try:
#         inf.append(open(sys.argv[n],"r"))
#         n+=1
#     except:
#         print("ОЙ, {} файла нет!".format(sys.argv[n]))
#         cont = input("Продолжить сцепку без этого файла \"Да/Нет\"")
#         if cont == "Да":
#             n+=10
#         else:
#             quit()
#
# def def_p():
#     for i in range(0, len(inf)):
#         line = inf[i].readline().rstrip()
#         while line != "":
#             print(line)
#             line = inf[i].readline().rstrip()
#
# def def_cat():
#     new_file_name = input("Введите новое имя файла: ")
#     new_file = open(new_file_name, "w")
#     coun = 1
#     for i in range(0, len(inf)):
#         line = inf[i].readline().rstrip()
#         while line != "":
#             new_file.write(str(coun) + " " + line + "\n")
#             coun += 1
#             line =inf[i].readline().rstrip()
#     new_file.close()
#     print("The files concatinate")
#
# def_name = locals()["def_" + sys.argv[1]]
# def_name()
#

#   153
#
# import sys
#
# try:
#     inf = open('test_open.txt', "r")
# except:
#     print("Такого файла нет")
#     quit()
# dict_of_word = {}
# line = inf.readline().rstrip()
# while line != "":
#     list_of_word = line.split(" ")
#     for i in list_of_word:
#         try:
#             dict_of_word[len(i)].append(i)
#         except:
#             dict_of_word[len(i)] = [i]
#     line = inf.readline().rstrip()
# lagest = 0
# for i in dict_of_word.keys():
#     if i > lagest:
#         lagest = i
# print("Самые длинные слова имеют длину {} - ".format(lagest), end="")
# for w in dict_of_word[lagest]:
#     print(w, end=" ")


#     154

# import sys
#
# try:
#     inf = open(sys.argv[1], "r")
# except:
#     print("Такого файла нет")
#     quit()
#
# line = inf.readline().rstrip()
# letters_list = {}
# while line != "":
#     for letter in line:
#         if letter in [".",",","!",":",";","_"," "]:
#             continue
#         letter = letter.lower()
#         try:
#             letters_list[letter] = letters_list[letter] + 1
#         except:
#             letters_list[letter] = 1
#     line = inf.readline().rstrip()
#
# for i in letters_list.keys():
#     print("%s : %s" % (i, letters_list[i]))


#  156
#
# sum = 0
# number = input('Число (для остановки нажмите ENTER):')
# while number != "":
#     try:
#         number = float(number)
#     except:
#         print("Введена строка")
#     else:
#         sum = sum + number
#         print(sum)
#     number = input('Число (для остановки нажмите ENTER):')

#   158
#
# import sys
#
# try:
#     file_reading = open(sys.argv[1], "r")
# except:
#     print("Введено некоректное имя файла")
#     quit()
# try:
#     file_writing = open(sys.argv[2], "w")
# except:
#     print("Введен некорректный формат файла")
#     quit()
#
# line = file_reading.readline().rstrip()
# while line != "":
#     new_line = ""
#     while_breaker = False
#     for letter in line:
#         if letter == "#":
#             while_breaker = True
#             if new_line not in "    ":
#                 file_writing.write(new_line + "\n")
#             else:
#                 break
#         else:
#             new_line = new_line + letter
#     if while_breaker:
#         line = file_reading.readline().rstrip()
#         continue
#     file_writing.write(new_line + "\n")
#     line = file_reading.readline().rstrip()
# file_writing.close()
#
 # 159
# def wordseach():
#     import random
#     inf = open('words.txt', "r")
#     n = random.randrange(1, 235924)
#     k = 0
#     word = str()
#     while k != n:
#         word = inf.readline().rstrip()
#         k += 1
#     inf.close()
#     return word
# def pasgen():
#     password = str()
#     while 8 > len(password) or len(password) > 10:
#         word1 = wordseach().title()
#         word2 = wordseach().title()
#         password = word1 + word2
#     return password
#
# pas = pasgen()
# print(pas)

# inf = open("elements.txt", "r")
# elements = {}
# for line in inf:
#         line = line.rstrip()
#         num_elements = line.split(",")
#         elements[int(num_elements[0])] = num_elements[1] + ", " + num_elements[2]
#         elements[num_elements[1]] = num_elements[0] + ", " + num_elements[2]
#         elements[num_elements[2]] = num_elements[0] + ", " + num_elements[1]
#
# elem = input("Введите количество протонов или обозначение или название химического элемента:")
# while elem != "":
#     try:
#         print(elements[elem])
#     except KeyError:
#         try:
#             print(elements[int(elem)])
#         except:
#             print("Такого элемента в базе нет!")
#     elem = input("Введите количество протонов или обозначение или название химического элемента:")
#
# file_name = input("Введите наименование файла")
# inf = open(file_name, "r")
#

# popularity_letter = {}
# for l in range(65, 91):
#     letter = chr(l)
#     popularity_letter.setdefault(letter, 0)
# print(popularity_letter)
#
# line = inf.readline().rstrip()
# while line:
#     for letter in line:
#         try:
#             letter = letter.upper()
#             popularity_letter[letter] = popularity_letter[letter] + 1
#         except:
#             continue
#     line = inf.readline().rstrip()
#
# min = popularity_letter["A"]
# for key in popularity_letter:
#     if popularity_letter[key]<min:
#         min = popularity_letter[key]
# for l in range(65, 91):
#     letter = chr(l)
#     if popularity_letter[letter] == min:
#         num = popularity_letter.setdefault(letter, 0)
#         print("!%s:%d" % (letter, num))
#     else:
#         num = popularity_letter.setdefault(letter, 0)
#         print("%2.7s:%d" % (letter, num))




# import os
#
# boys_popular_names_by_year = {}
# girls_popular_names_by_year = {}
# path = r"C:\Users\Nik\Documents\venv\baby_names\BabyNames"
# file_names = os.listdir(path)
# for f in file_names:
#     year = f.split("_")[0]
#     gender = f.split("_")[1]
#     try:
#         inf = open("C:\\Users\\Nik\\Documents\\venv\\baby_names\\BabyNames\\{}".format(f), "r")
#     except:
#         print("Проблема с открытием файла \"{}\"".format(f))
#     else:
#         line = inf.readline().rstrip()
#         name = line.split(" ")[0]
#         if gender == "BoysNames.txt":
#             boys_popular_names_by_year[year] = name
#         elif gender == "GirlsNames.txt":
#             girls_popular_names_by_year[year] = name
# start = int(input("Введите начало периода:"))
# end = int(input("Введите конец периода:"))
# for i in range(start,end+1):нахождение наибольшего общего  делителя
#     print(i, end=" ")
#     print(boys_popular_names_by_year[str(i)], end=" ")Очередь
#     print(girls_popular_names_by_year[str(i)])

#  173
#
# def sum_elements():
#     n = input("Введите число:")
#     if n != "":
#         n = float(n)
#         return n + sum_elements()
#     else:
#         return 0.0
# sum = sum_elements()
# print(sum)


#  174
#
# def calculating_grearest_common_divisor(first,second):
#     if first > second:
#         a = first
#         b = second
#     else:
#         a = second
#         b = first
#     if b == 0:
#         return a
#     else:
#         c = a % b
#         return calculating_grearest_common_divisor(b,c)
#
# a = float(input("Введите число:"))
# b = float(input("Введите число:"))
# n = calculating_grearest_common_divisor(a,b)
# print(n)

# def NATO(word):
#     vocabulary = {"A": "ALFA", "B": "BRAVO", "C": "CHARLIE"}
#     new_word = str()
#     letter = word[0]
#     if len(word) != 1:
#         word = word[1:]
#         if letter.upper() in vocabulary:
#             letter = letter.upper()
#             new_word = new_word + vocabulary[letter] + str(NATO(word))
#         else:
#             new_word = new_word + str(NATO(word))
#     else:
#         if letter.upper() in vocabulary:
#             letter = letter.upper()
#             return vocabulary[letter]
#         else:
#             return ""
#     return new_word
# a = NATO("ABB,c,C")
# print(a)

#  180
# import inspect
#
#
# def itorial_distance(s,t):
#     if len(s) == 0:
#         return len(t)
#     elif len(t) == 0:
#         return len(s)
#     else:
#         cost = 0
#         if s[-1] != t[-1]:
#             cost = 1
#         d1 = itorial_distance(s[0:len(s)-1], t)+ 1
#         d2 = itorial_distance(s, t[0:len(t)-1])+ 1
#         d3 = itorial_distance(s[0: len(s) - 1], t[0:len(t)-1]) + cost
#
#
#         return min(d1, d2, d3)
#
# def main():
#
#     s = input("Введите строку: ")
#     t = input("Введите другую строку: ")
#
#     print("Редакционное расстояние между %s и %s равно %d." % \
#     (s, t, itorial_distance(s, t)))



# main()
# def min_way(x1,x2):
#     step = []
#     x = x2-x1
#     print(x,"X")
#     if x !=0:
#         a = x - 1
#         print(a,"a")
#         b = x + 1
#         print(b,"b")
#         if a < b:
#             step.append(1)
#             c = x1+1
#         else:
#             step.append(-1)
#             c = x1-1
#         step.append(min_way(c, x2))
#     return step
#
# s = min_way(1,5)
# print(s)

# 181

# def coin_exchange(sum,number_of_coin):
#     def coin(coins, values):
#         print(coins,values)
#         if coins < number_of_coin and values < sum:
#             d1 = coin(coins + 1, values + 0.25)
#             d2 = coin(coins + 1, values + 0.1)
#             d3 = coin(coins + 1, values + 0.05)
#             d4 = coin(coins + 1, values + 0.01)
#             if d1 or d2 or d3 or d4:
#                 return True
#             else:
#                 return False
#         elif coins > number_of_coin or values > sum:
#             return False
#         elif coins == number_of_coin and values == sum:
#             return True
#     return coin(0,0)
# sum = float(input("Введите сумму:"))
# enter_coin = int(input("Введите количество монет:"))
#
# answer = coin_exchange(sum, enter_coin)
# print(answer)

# 182
#
# def el (word, list_of_elements, slice):
#     if word[0:slice] in list_of_elements:
#         element = word[0:slice]
#         next_word = word.replace(word[0:slice], '')
#         new_word = list_of_elements[element] + substitution_letter(next_word, list_of_elements)
#         return new_word
#     else:
#         return ""
#
# def substitution_letter(word, list_of_elements, max_len=max_lenght):
#     if len(word) == 0:
#         return ""
#     else:
#         words = []
#         for i in range(max_len):
#             words.append(el(word, list_of_elements, i))
#     for i in words:
#         if i.lower() == word.lower():
#             return i
#     return "Собрать нельзя"
#
# elements_table = {}
# inf = open("elements.txt", "r")
# line = inf.readline().rstrip()
# while line != "":
#     line = line.split(",")
#     elements_table[line[1].lower()] = line[1]
#     line = inf.readline().rstrip()
#
# max_lenght = 1
# for i in elements_table.keys():
#     if len(i) > max_lenght:
#         max_lenght = len(i)
#
#
# enter_word = "silicon"
# new_word = substitution_letter(enter_word, elements_table)
# print(new_word)
# import random
# def longest_game(win_list_1,win_list_2):
#     if len(win_list_1) >= len(win_list_2):
#         win = win_list_1
#     else:
#         win = win_list_2
#     win = " ".join(win)
#     return win
#
#
# def longestSequence(start, words):
#     if start == "":
#         return []
#     best = []
#     last_letter = start[len(start) - 1].lower()
#     for i in range(0, len(words)):
#         first_letter = words[i][0].lower()
#         if first_letter == last_letter:
#             candidate = longestSequence(words[i], words[0: i] + words[i + 1: len(words)])
#             if len(candidate) > len(best):
#                 best = candidate
#     return [start] + best
#
# def removing_elements_table(start_word_of_element, elements_table, removing=True):
#     if len(elements_table) >= 2:
#         if removing:
#             elements_table.remove(start_word_of_element.lower())
#         for i in range(0, len(elements_table)):
#             next_word = elements_table[i].lower()
#             if start_word_of_element[-1] == next_word[0]:
#                 win_list_1 = next_word + ' ' + removing_elements_table(next_word, elements_table)
#                 win_list_1 = win_list_1.split(" ")
#                 win_list_2 = next_word + ' ' + removing_elements_table(next_word, elements_table, False)
#                 win_list_2 = win_list_2.split(" ")
#                 win = longest_game(win_list_1, win_list_2)
#                 return win
#         return "Игра закончена!"
#     else:
#         if start_word_of_element == elements_table[0]:
#             return "Вы выиграли!"
#         else:
#             return "Игра закончена!"
# #
# standart_elements_table = []
# inf = open("elements.txt", "r")
# line = inf.readline().rstrip()
# while line != "":
#     line = line.split(",")
#     standart_elements_table.append(line[2].lower())
#     line = inf.readline().rstrip()
# random.shuffle(standart_elements_table)
# #
# start_element = input("Введите стартовый элемент:")
# table_selection = input("Использовать стандартную таблицу? Yes/No :")
# if table_selection.lower() == "yes":
#     table = standart_elements_table
# elif table_selection.lower() == "no":
#     table_of_player = []
#     enter_element = input("Введите элемент латиницей. Для остановки оставьте пустую строку:")
#     while enter_element != "":
#         table_of_player.append(enter_element.lower())
#         enter_element = input("Введите элемент латиницей. Для остановки оставьте пустую строку:")
#         table = table_of_player
# else:
#     table = standart_elements_table
#     print("Что то пошло не так!")
#     quit()
#
# new_word = longestSequence(start_element, table)
# print(new_word)
# def nato(sentens):
#     vocabulary = {"A": "ALFA", "B": "BRAVO", "C": "CHARLIE"}
#     if sentens =="":
#         return ""
#     tail = sentens[1:len(sentens)]
#     if sentens[0].upper() in vocabulary.keys():
#         print("y")
#         total = vocabulary[sentens[0].upper()] + nato(tail)
#         return total
#     else:
#         return nato(tail)
# c = nato("aacb,,,aaaa")
# print(c)


n = "count_bcy(1,10)"

print(n.replace("c","",1))
dfgbdfgdfgdfgd
