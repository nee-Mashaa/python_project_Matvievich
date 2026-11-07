# Дан целочисленный список размера N, все элементы которого упорядочены (по возрастанию или по убыванию).
# Найти количество различных элементов в данном списке.
import random
n = int(input("Введите размер массив"))
a = []
count = 1
for i in range(n):
    a.append(random.randint(1, 10))
print(a)
for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
for i in range(1, n):
    if a[i] != a[i - 1]:
        count += 1
print(a," Количество различных элементов", count)