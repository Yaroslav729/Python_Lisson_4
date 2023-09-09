# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите колличество элементов первого множества '))
m = int(input('Введите колличество элементов второго множества '))

import random
list_One = set(random.randint(0, 20)
for i in range (n))
print(list_One)
list_Too = set(random.randint(0, 20)
for i in range (m))
print(list_Too)

list = sorted(list_One.intersection(list_Too))
print(list)

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, 
# находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# import random
# bush = int(input("введите количество кустов: "))
# berry = list(random.randint(1, 10) for i in range(bush))
# print(berry)

# arr_count = list()

# for i in range(len(berry)):
#        arr_count.append(berry[i-2] + berry[i-1] + berry[i])
# print(max(arr_count))
    