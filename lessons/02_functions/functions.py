# Так писать долго!
# И этот кусок кода мы потом миллион раз копировать не будем
print("Введите число 1")
x = int(input())
print("Введите число 2")
y = int(input())
z = x + y
print(f'сумма чисел {z}')

# лучше использовать функции
# def - ключевое слово
# example - имя функции
# variable 1, 2 - переменные
# pass - ничего не делать
# return - то что функция вернет
# result - результат функции

def example(variable_1, variable_2):
    pass


def sum_of_two(num_1, num_2):
    print("Введите число 1")
    num_1 = int(input())
    print("Введите число 2")
    num_2 = int(input())
    z = num_1 + num_2
    print(f'сумма чисел {z}')

def print_name(name="User"):
    print(name)