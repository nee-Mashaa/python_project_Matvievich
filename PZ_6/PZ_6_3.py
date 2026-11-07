# Дан список размера N. Осуществить циклический сдвиг элементов списка влево на одну позицию
# (при этом AN перейдет в AN-1, AN-1 — в AN-2, . . ., A1 — в AN).
import random
n = int(input("Введите размер массив"))
a = []
for i in range(n):
    a.append(random.randint(1, 10))
print(a)
for i in range(1, n):
    a[i], a[i-1]=a[i-1], a[i]
print(a)