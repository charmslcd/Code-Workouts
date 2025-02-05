def add(*args):
    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num

def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key,value)


sum_func = add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(sum_func)


calculate(add=3, multiple=5)