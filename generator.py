from math import sqrt

def is_prime(x):

    if x in [0, 1]:
        return False
    if x == 2:
        return True
    for n in range(3, int(x ** 0.5 + 1)):
        if x % n == 0:
            return False
    return True


for n in [i for i in range(100)if is_prime(i)]:
    print (n)

for n in filter(is_prime, range(100)):
    print (n)


