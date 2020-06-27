from itertools import count, cycle
from sys import argv

l1, l2 = map(int, argv[1:])


def my_func(l1, l2):
    for el in count(l1):
        if el > l2:
            return "End."
        print(el)


print(my_func(l1, l2))
def mu_func2():
    my_list = ["Элементы", "этого", "списка", "повторяются", "раз."]
    my_list.insert(4, l1)
    n_cycle = 0
    n_len = len(my_list) * int(my_list[4])
    for el in cycle(my_list):
        if n_cycle >= n_len:
            return
        print(el)
        n_cycle +=1
mu_func2()