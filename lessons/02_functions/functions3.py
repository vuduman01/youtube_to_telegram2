def multiply_of_two_numbers_with_users_input():
    print("Введите число 1")
    num_1 = int(input())
    print("Введите число 2")
    num_2 = int(input())
    z = num_1 * num_2
    print(z)

multiply_of_two_numbers_with_users_input()

def multiply_of_two_numbers_with_ours_variables(num_1, num_2):
    z = num_1 * num_2
    print(z)

multiply_of_two_numbers_with_ours_variables(1231, 1231231)

def multiply_of_two_numbers_with_return(num_1, num_2):
    return num_1 * num_2

result = multiply_of_two_numbers_with_return(2, 3)
print(result)
