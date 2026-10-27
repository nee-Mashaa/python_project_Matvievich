# Составить функцию, которая выведет на экран строку, содержащую задаваемое с клавиатуры число символов.
def print_line(n, symbol):
    print(symbol * n)

a = input("введите кол символов")
symb = input("введите символ")
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Число введено неправильно")
        a = input("введите кол символов")
print_line(a, symb)
