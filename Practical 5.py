# #Цикл for
# # 1. Выведите все числа от 1 до 10.
# for i in range(1, 11):
#     print(i)

# # 2. Выведите все чётные числа от 2 до 50.
# for i in range(2, 51, 2):
#     print(i)

# # 3. Выведите числа от 10 до 1 в порядке убывания.
# for i in range(10, 0, -1):
#     print(i)

# # 4. Дано число n. Найдите сумму всех чисел от 1 до n.
# n = int(input("Введите число: "))
# s = 0
# for i in range(1, n + 1):
#     s += i
# print(s)

# # 5. Дано число n. Найдите его факториал.
# n = int(input("Введите число: "))
# fact = 1
# for i in range(1, n + 1):
#     fact *= i
# print(fact)

# # 6. Дано число n. Выведите таблицу умножения на n от 1 до 10.
# n = int(input("Введите число: "))
# for i in range(1, 11):
#     print(n, "*", i, "=", n * i)

# # 7. Дан список чисел. Посчитайте, сколько в нём положительных чисел.
# nums = [-3, 5, 0, 8, -1, 4, -7, 2]
# count = 0
# for x in nums:
#     if x > 0:
#         count += 1
# print(count)

# # 8. Дана строка. Посчитайте, сколько в ней гласных букв.
# text = "привет мир"
# vowels = "аеёиоуыэюя"
# count = 0
# for ch in text:
#     if ch in vowels:
#         count += 1
# print(count)

# # 9. Дан список чисел. Найдите наибольший элемент, не используя max().
# nums = [3, 8, 1, 15, 7, 12]
# largest = nums[0]
# for x in nums:
#     if x > largest:
#         largest = x
# print(largest)

# # 10. Выведите таблицу умножения от 1 до 9 в виде квадрата.
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i * j, end=" ")
#     print()



# #Цикл While
# # 1. Выведите все числа от 1 до 10 с помощью while.
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# # 2. Вводите числа, пока не будет введён 0. Выведите сумму введённых чисел.
# s = 0
# num = int(input("Введите число (0 — выход): "))
# while num != 0:
#     s += num
#     num = int(input("Введите число (0 — выход): "))
# print("Сумма:", s)

# # 3. Дано натуральное число. Посчитайте количество его цифр.
# n = int(input("Введите число: "))
# count = 0
# while n > 0:
#     count += 1
#     n //= 10
# print("Количество цифр:", count)

# # 4. Дано натуральное число. Найдите сумму его цифр.
# n = int(input("Введите число: "))
# s = 0
# while n > 0:
#     s += n % 10
#     n //= 10
# print("Сумма цифр:", s)

# # 5. Дано натуральное число. Выведите его цифры в обратном порядке одним числом.
# n = int(input("Введите число: "))
# rev = 0
# while n > 0:
#     rev = rev * 10 + n % 10
#     n //= 10
# print("Обратное число:", rev)

# # 6. Дано число n. Выведите все степени двойки, не превышающие n.
# n = int(input("Введите число: "))
# p = 1
# while p <= n:
#     print(p)
#     p *= 2

# # 7. Запрашивайте пароль, пока пользователь не введёт правильный.
# password = "1234"
# p = input("Введите пароль: ")
# while p != password:
#     p = input("Неверно, попробуйте снова: ")
# print("Доступ разрешён")

# # 8. Даны два натуральных числа. Найдите их наибольший общий делитель.
# a = int(input("Введите a: "))
# b = int(input("Введите b: "))
# while b != 0:
#     a, b = b, a % b
# print("НОД:", a)

# # 9. Дано число n. Выведите все числа Фибоначчи, не превышающие n.
# n = int(input("Введите число: "))
# a, b = 0, 1
# while a <= n:
#     print(a)
#     a, b = b, a + b

# # 10. Программа загадывает число от 1 до 100. Пользователь угадывает его,
# # а программа отвечает «больше» или «меньше». В конце выведите количество попыток.
# secret = 67          # загаданное число
# tries = 0
# guess = int(input("Угадайте число от 1 до 100: "))
# tries += 1
# while guess != secret:
#     if guess < secret:
#         print("Загаданное число больше")
#     else:
#         print("Загаданное число меньше")
#     guess = int(input("Попробуйте снова: "))
#     tries += 1
# print("Вы угадали! Попыток:", tries)



#Словари
# 1. Создайте словарь из трёх учеников и их оценок. Выведите оценку одного ученика по его имени.
students = {"Иван": 5, "Мария": 4, "Пётр": 3}
print(students["Мария"])

# 2. Дан словарь. Добавьте в него новую пару, измените значение одного из ключей,
# удалите другой ключ и выведите результат.
d = {"a": 1, "b": 2, "c": 3}
d["d"] = 4          # добавили новую пару
d["a"] = 10         # изменили значение
del d["b"]          # удалили ключ
print(d)

# 3. Дан словарь и ключ. Выведите значение по этому ключу, а если такого ключа нет,
# выведите «Нет такого ключа».
d = {"a": 1, "b": 2}
key = "c"
if key in d:
    print(d[key])
else:
    print("Нет такого ключа")

# 4. Дан словарь. Выведите отдельно все его ключи, все значения и количество пар.
d = {"a": 1, "b": 2, "c": 3}
print("Ключи:", list(d.keys()))
print("Значения:", list(d.values()))
print("Количество пар:", len(d))

# 5. Дан словарь товаров и их цен. Выведите каждый товар и его цену с новой строки.
products = {"хлеб": 40, "молоко": 80, "сыр": 300}
for name, price in products.items():
    print(name, "-", price)

# 6. Дан словарь товаров и их цен. Найдите сумму всех цен и название самого дорогого товара.
products = {"хлеб": 40, "молоко": 80, "сыр": 300}
total = 0
expensive = None
for name, price in products.items():
    total += price
    if expensive is None or price > products[expensive]:
        expensive = name
print("Сумма цен:", total)
print("Самый дорогой товар:", expensive)

# 7. Дана строка. Посчитайте, сколько раз в ней встречается каждый символ,
# и сохраните результат в словарь.
text = "привет мир"
counts = {}
for ch in text:
    if ch in counts:
        counts[ch] += 1
    else:
        counts[ch] = 1
print(counts)

# 8. Дана строка из слов через пробел. Посчитайте, сколько раз встречается каждое слово,
# и выведите самое частое.
text = "я люблю python и я люблю программировать"
counts = {}
for word in text.split():
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
print(counts)
most_common = None
for word, cnt in counts.items():
    if most_common is None or cnt > counts[most_common]:
        most_common = word
print("Самое частое слово:", most_common)

# 9. Дан словарь. Создайте новый словарь, в котором ключи и значения поменяны местами.
d = {"a": 1, "b": 2, "c": 3}
inverted = {}
for key, value in d.items():
    inverted[value] = key
print(inverted)

# 10. Даны два списка одинаковой длины: страны и их столицы. Составьте из них словарь
# и выведите столицу страны, которую введёт пользователь.
countries = ["Россия", "Франция", "Германия"]
capitals = ["Москва", "Париж", "Берлин"]
country_capitals = {}
for i in range(len(countries)):
    country_capitals[countries[i]] = capitals[i]
user_country = input("Введите страну: ")
if user_country in country_capitals:
    print(country_capitals[user_country])
else:
    print("Нет такой страны в словаре")