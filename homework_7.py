def fact(n):
    global num1
    num1 = 1
    for el in range(1, n):
        num1 *= el
        yield num1
n = 5
print(f"Факториал числа {n}! = {list(el for el in fact(n))} = {n * num1}")
