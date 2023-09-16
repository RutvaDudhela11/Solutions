# Problem 4:  Swap two Strings Without Using any Third Variable


def swap_string(str1, str2):
    str1, str2 = str2, str1
    return str1, str2

a = "Hello"
b = "World"
print(f"Strings before swap: a = {a} and b = {b}")

x = swap_string(a, b)
print(f"Strings after  swap: a = {x[0]} and b = {x[1]}")