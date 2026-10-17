# Дано следующее число А и целое число N(>0). Используя один цикл, найти сумму 1 + А + А^2 - А^3 + ...+(-1)^N A^N.
# Условный оператор не использовать.
a = input("Введите вещественное число")
n = input("Введите число")
while type(a) != float:
    try:
        a = float(a)
    except ValueError:
        print("Нерпавильно ввели число!")
        a = input("Введите вещественное число")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Нерпавильно ввели число!")
        n = input("Введите число")
k = 0
sum = 1.0
p = 1.0
while k < n:
    p = p * a
    sum += p
    k += 1
print(sum)