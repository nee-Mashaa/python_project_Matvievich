# Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2,
# AN-1, A3, AN-2, ….
import random
n = int(input("Введите размер массив"))
a = []
b = []
for i in range(n):
    a.append(random.randint(1, 10))
print(a)
j = n - 1
for i in range(j + 1):
    b.append(a[i])
    if i != j:

        j -= 1
print(b)
