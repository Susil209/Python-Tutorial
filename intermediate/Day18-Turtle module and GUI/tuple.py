import random

print("Tuple")

# create tuple
my_tuple = ('apple', 'orange', 100, True, 'banana',
            {1: 'start', '2': 'énd'}, ['l1', 'l2'], 'pizza')

# print(my_tuple)
# print(my_tuple[-1])
#
# print(my_tuple[2:4])

# update and add tuple
my_list = list(my_tuple)
print(my_list)  #['apple', 'orange', 100, True, 'banana', {1: 'start', '2': 'énd'},
# ['l1', 'l2'], 'pizza']

my_list[0] = 'banana'
my_tuple = tuple(my_list)
print(my_tuple)  #('banana', 'orange', 100, True, 'banana', {1: 'start', '2': 'énd'},
# ['l1', 'l2'], 'pizza')


# unpacking
(x, y, z, *a, c) = my_tuple
print(x)  # banana
print(a)  # [True, 'banana', {1: 'start', '2': 'énd'}, ['l1', 'l2']]
print(c)  #pizza

# create tuple using constructor
new_tuple = tuple((1, 2, 3))
print(new_tuple)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return tuple((r, g, b))


print(random_color())
