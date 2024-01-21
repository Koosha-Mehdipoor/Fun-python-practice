from itertools import count

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def divisors(x):
    divisor_list = []  
    max_divisor = 0
    number = 0

    for i in range(1, x + 1):
        if x % i == 0:
            if is_prime(i):
                divisor_list.append(i)
                if len(divisor_list) > max_divisor:
                    max_divisor = len(divisor_list)
                    number = x

    return divisor_list, max_divisor, number

max_divisor_result = 0
number_result = 0

for i in range(2):  # Loop twice, as in your example
    inputtt = int(input("Please enter a number: "))
    result = divisors(inputtt)

    if result[1] > max_divisor_result:
        max_divisor_result = result[1]
        number_result = result[2]

print("Number with maximum divisor count:", number_result)
print("Maximum divisor count:", max_divisor_result)
