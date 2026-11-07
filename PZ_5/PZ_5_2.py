# Дан прямоугольник, длины стороны которого равны натуральным числам A и B. Составить функцию, которая будет находить
# на сколько квадратов можно разрезать данный прямоугольник, если от него каждый раз отрезать квадрат наибольшей площади
def count_square(A, B):
    count = 0
    while A > 0 and B > 0:
        if A >= B:
            count += A // B
            A %= B
        else :
            count += B // A
            B %= A
    return count
a, b = input("Введите число"), input("Введите число")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Число введено неправильно")
        a = input("Введите число")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Число введено неправильно")
        b = input("Введите число")
print(count_square(a, b))

