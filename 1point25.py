from transformation import *
try:
    x = float(input('Insert side of square: '))
    x = transform(x)
    print(f'Perimeter: {transform(x*4)}')
except ValueError:
    print('Not a number!')