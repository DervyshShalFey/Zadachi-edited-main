from math import *
from transformation import *
try:
    x = float(input('Insert a number: '))
    x = transform(x)
    try:
        print(f'A) x = √((2a)+sinus of |3a|) \n   If a is equal to {x}, then y will be equal to {transform((x**2+10)/(sqrt((x**2)-1)))}')
    except:
        print(f'Square root of a^2 - 1, if a = {x} is undefined')
except ValueError:
    print('Not a number!')