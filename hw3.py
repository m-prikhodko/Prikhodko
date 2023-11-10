# 1.	Дана строка состоящая минимум из 6 символов.
print("Задание 1")
string_for_output = "Это строка для вывода разных символов."
print("Это моя строка:", string_for_output)
# - Сначала выведите третий символ этой строки.
print("1.", string_for_output[2])
# - Во второй строке выведите предпоследний символ этой строки.
print("2.", string_for_output[-2])
# - В третьей строке выведите первые пять символов этой строки.
print("3.", string_for_output[0:4])
# - В четвертой строке выведите всю строку, кроме последних двух символов.
print("4.", string_for_output[:-2])
# - В пятой строке выведите все символы с четными индексами
print("5.", string_for_output[::2])
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
print("6.", string_for_output[1::2])
# - В седьмой строке выведите все символы в обратном порядке.
print("7.", string_for_output[::-1])
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
print("8.", string_for_output[-1::-2])
# - В девятой строке выведите длину данной строки.
print("9.", len(string_for_output))
print("_____________")

# 2.	Дано слово. Верно ли, что оно начинается и оканчивается на одну и ту же букву?
print("Задание 2")
word_1 = "Benny"
start_end = word_1[0] == word_1[-1]
print(bool(start_end))
print("_____________")

# 3.	Дано слово. Получить его часть, образованную второй, третьей и четвертой буквами.
print("Задание 3")
word_2 = "Benito"
# part_of_word_2 = word_2[1] + word_2[2] + word_2[3]
part_of_word_2 = word_2[1:4]
print(part_of_word_2)
print("_____________")

# 4.	Из слова яблоко путем "вырезок" и "склеек" его букв получить слова блок и око.
print("Задание 4")
word_3 = "яблоко"
part1_of_word_3 = word_3[1:5]
print(part1_of_word_3)
part2_of_word_3 = word_3[3:6]
print(part2_of_word_3)
print("_____________")

# 5.	В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
print("Задание 5")
full_name = "Ivanou Ivan"
name = full_name[7:11]
surname = full_name[0:6]
reverse_of_full_name = name + " " + surname
print(reverse_of_full_name)
print("_____________")

# 6.	Проверить является ли строка палиндромом.(шалаш).
print("Задание 6")
word_4 = "шалаш"
is_palindrome = word_4 == word_4[::-1]
print(bool(is_palindrome))
print("_____________")

# 7.	Создайте список и извлеките из него списка второй элемент.
print("Задание 7")
cats = ["Benny", "Bairon", "Archi", "Stesha", "Missy", "Nyastya"]
print(cats[1])
print("_____________")

# 8.	Вывести входит ли строка1 в строку2 (пример: employ и employment )
print("Задание 8")
word_5 = "кот"
word_6 = "котеночек"
# print(word_6.startswith(word_5))
print(word_5 in word_6)
print("_____________")

# 9.	*Дана строка которая содержит более 2 символов ‘f’. Строка может быть произвольной. Найдите индекс второй буквы ‘f’ в данной строке.
print("Задание 9")
string_1 = "beautiful flower"
index_of_1 = string_1.find("f")
index_of_2 = string_1.find("f", index_of_1+1)
print(index_of_2)
print("_____________")

# 10.	*Создайте словарь, связав его с переменной school, и наполните его
# данными которые бы отражали количество учащихся в десяти разных
# классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
print("Задание 10")
school = {"1а": 15, "1б": 10, "2а": 20, "2б": 17, "3а": 19, "3б": 19, "4а": 14, "4б": 21, "5а": 20, "5б": 19}
# Внесите изменения в словарь согласно следующему:
# а) в одном из классов изменилось количество учащихся
school["1а"] = 16
# б) в школе появился новый класс.
school["5в"] = 23
# в) в школе был расформирован (удален) другой класс.
del school["3б"]
# г) Вычислите общее количество учащихся 9 классов в школе.
del school["1б"]
# Тут пришлось удалить один класс, чтобы посчитать количество учеников в 9 классах школы, как сказано в задании.
# Ниже есть решение для суммы учеников в 10 классах, так как по итогу всех действий в словаре осталось 10 классов
pupils_9_grades = sum(school.values())
print("Всего учеников в 9 классах в школе:", pupils_9_grades)
# Решение для количества учеников в 10 классах, тогда нужно закомментировать строки 100, 103, 104
# pupils_10_grades = sum(school.values())
# print("Всего учеников в 10 классах в школе:", pupils_10_grades)
print("_____________")