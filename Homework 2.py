# Задание 1

# Name = 'Sam'
# Age = 25
# Height = 177.5
# Femail = False
# my_list = [Name, Age, Height, Femail]
# print('Name:',type(my_list[0]), ', Age:',type(my_list[1]),', Height:',type(my_list[2]),', Femail:',type(my_list[3]))

# Задание 2

# Name = str(input('Введите имя: '))
# Age = int(input('Введите возраст: '))
# Height = float(input('Введите рост: '))
# Femail = bool(input('Мужчина? Да -1/Нет - 0: '))
# my_list = []
# my_list.append(Name)
# my_list.append(Age)
# my_list.append(Height)
# my_list.append(Femail)
# my_list[0], my_list[1] = my_list[1], my_list[0]
# my_list[2], my_list[3] = my_list[3], my_list[2]
# print(my_list)

# Задание 3

# number = int(input('Введите число от 1 до 12: '))
# numbers = range(1,13)
# my_list = ['Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето', 'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']
# while number not in numbers:
#     number = int(input('Введите число от 1 до 12: '))
# else:
#     print(my_list[number-1])

# Задание 4

# string = input("Введите строку с пробелами ")
# my_word = []
# number = 1
# for el in range(string.count(' ') + 1):
#     my_word = string.split()
#     if len(str(my_word)) <= 10:
#         print(f" {number} {my_word [el]}")
#         number += 1
#     else:
#         print(f" {number} {my_word [el] [0:10]}")
#         number += 1

# Задание 5

# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# digit = int(input("Введите число (111 - выход) "))
# while digit != 111:
#     for el in range(len(my_list)):
#         if my_list[el] == digit:
#             my_list.insert(el + 1, digit)
#             break
#         elif my_list[0] < digit:
#             my_list.insert(0, digit)
#         elif my_list[-1] > digit:
#             my_list.append(digit)
#         elif my_list[el] > digit and my_list[el + 1] < digit:
#             my_list.insert(el + 1, digit)
#     print(f"текущий список - {my_list}")
#     digit = int(input("Введите число "))


