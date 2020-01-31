from math import factorial

def factotial_ver1(item):
    if item == 2:
        return 2
    else:
        return item*factotial_ver1(item - 1)

if __name__ == '__main__':
    for elem in (3, 6, 8):
        ans = factotial_ver1(elem)
        assert factorial(elem) == ans
        print('For elem', elem, 'factorial is', ans)
