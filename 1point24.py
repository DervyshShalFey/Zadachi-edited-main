from math import *
from transformation import *
try:
    x = float(input('Insert a number: '))
    x = transform(x)
    try:
        print(f'A) x = √(2a + sinus of |3a|)/3.56 \n   If a is equal to {x}, then y will be equal to {sqrt((2*x + sin(module(3*x)))/3.56)}')
    except:
        print(f'A) Square root of (2a + sinus of |3a|)/3.56, where a = {x} is undefined')
except ValueError:
    print('Not a number!')