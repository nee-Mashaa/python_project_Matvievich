# Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2,
# AN-1, A3, AN-2, ….
import random
n = int(input("Введите размер массив"))
a = []
b = []
c = []
for i in range(n):
    a.append(random.randint(1, 10))
print(a)
j = n - 1
for i in range(j):
    b.append(a[i])
    if i != j:
        b.append(a[j])
        j -= 1
h = n - 1
for i in range(h+1):
    c.append(b[i])
print(c)
