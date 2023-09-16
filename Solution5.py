# Problem 5: Swap two numbers without using a temporary variable


def swap_number(num1, num2):
    num1, num2 = num2, num1
    return num1, num2

a = 10
b = 50
print(f"Numbers before swap: a = {a} and b = {b}")

y = swap_number(a, b)
print(f"Numbers after  swap: a = {y[0]} and b = {y[1]}")
