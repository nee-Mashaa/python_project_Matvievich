# Дан список A размера N. Вывести его элементы в следующем порядке: A1, AN, A2,
# AN-1, A3, AN-2, ….
n = int(input("Введите размер массив"))
a = []
for i in range(n):
    if i % 2 == 0:
        a.append(i + 1)
    else:
        a.append(n)
        n -= 1
print(a)
