def add_one(x):
    return x + 1

def print_hello():
    print("Hello")

x1 = add_one(1)
x2 = add_one(2)
x3 = add_one(3)
print(x1)
print(x2)
print(x3)

print_hello()

# без return и переменных
def sum_of_two_user_input():
    print("Введите число 1")
    num_1 = int(input())
    print("Введите число 2")
    num_2 = int(input())
    z = num_1 + num_2
    print(f'сумма чисел {z}')

sum_of_two_user_input()

# с нашими переменными но без return
def sum_of_two_our_variables(num_1, num_2):
    z = num_1 + num_2
    print(f'сумма чисел {z}')

sum_of_two_our_variables(20, 5)

# только return
def sum_of_two_with_return(num_1, num_2):
    return num_1 + num_2

result = sum_of_two_with_return(15, 60)
print(result)