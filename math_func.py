# from math import sqrt
#
#
# # для квадратного уранения  ==========================================================================
# def solver(a, b, c):
#     D = b * b - 4 * a * c
#     if D >= 0:
#         x1 = (-b + sqrt(D)) / (2 * a)
#         x2 = (-b - sqrt(D)) / (2 * a)
#         text = 'D = %s \n x1 = %s \n x2 =%s \n' % (D, x1, x2)
#     else:
#         text = 'D = %s \n Это уравнение не имеет корней' % D
#     return text
#
#
# # для герона   ==========================================================================
# def geron_func(a, b, c):
#     p = (a + b + c) / 2
#     s = p * (p - a) * (p - b) * (p - c)
#     s = sqrt(s)
#     text = f'ваш ответ: {s}'
#     return text
#
#
# def proverka_geron(a, b, c):
#     if a + b <= c or c + b <= a or a + c <= b:
#         return False
#     return True
#
#
# # для куба   ==========================================================================
# def kub_calculyator(a):
#     return a ** 3
#
#
from math import sqrt


# для квадратного уранения  ==========================================================================
def solver(a, b, c):
    D = b * b - 4 * a * c
    if D >= 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        text = 'D = %s \n x1 = %s \n x2 =%s \n' % (D, x1, x2)
    else:
        text = 'D = %s \n Это уравнение не имеет корней' % D
    return text


# для герона   ==========================================================================
def geron_func(a, b, c):
    p = (a + b + c) / 2
    s = p * (p - a) * (p - b) * (p - c)
    s = sqrt(s)
    text = f'ваш ответ: {s}'
    return text


def proverka_geron(a, b, c):
    if a + b <= c or c + b <= a or a + c <= b:
        return False
    return True


# для куба   ==========================================================================
def kub_calculyator(a):
    return a ** 3


# для параллелепипеда===================================================================
def para_calculyator(a, b, c):
    V = a * b * c
    return V
