# Задание 1

# name = input('Введите Ваше имя: ')
# surname = input('Введите Вашу фамилию: ')
# age = int(input('Введите Ваш возраст: '))
# number = 10
# next_age = age + number
# print(f'Через {number} лет, Вам {name} {surname} будет {next_age} лет')

# Задание 2

# current_time = int(input('Введите время в секундах: '))
# hour = current_time // 3600
# minute = (current_time % 3600) // 60
# seconds = (current_time % 3600) % 60
# print("{:02}:{:02}:{:02}". format(hour, minute, seconds))

# Задание 3

# n = input('Введите число n: ')
# nn = int(n + n)
# nnn = int(n + n + n)
# print(int(n) + nn + nnn)

# Задание 4

# number = int(input('Введите число: '))
# number1 = 0
# while number < 10:
#     print('Введите число больше 10')
#     number = int(input('Введите число: '))
# else:
#     while number > 0:
#         if number % 10 > number1:
#             number1 = number % 10
#             number = number // 10
#         elif number % 10 <= number1:
#             number = number // 10
#     print(number1)
# print('Конец')

# Задание 5

# revenue = int(input('Введите сумму выручки фирмы: '))
# expence = int(input('Введите сумму издержек фирмы: '))
# if revenue >= expence:
#     print('Фирма работает с прибылью', revenue - expence, 'руб.')
# else:
#     print('Фирма работает в убыток', expence - revenue, 'руб.')
# if revenue > expence:
#     rent = float((revenue - expence) * 100 / revenue)
#     print("Рентабельность фирмы составляет {:.2f}%".format(rent))
# employees = int(input('Введите количество сотрудников фирмы: '))
# count = float((revenue - expence) / employees)
# print("Прибыль фирмы в расчете на одного сотрудника составляет {:.2f} руб.".format(count))

# Задание 6

# a = 2
# b = 3
# c = 1.1
# n = 1
# print('В первый день спортсмен пробежал', a, 'километра')
# while a < b:
#     n = n + 1
#     a = float(a * c)
# else:
#     print('На', n,'-й день спортсмен достиг результата - не менее', b, 'километров.')



