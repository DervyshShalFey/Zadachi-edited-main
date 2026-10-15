from transformation import *
try:
    x = float(input('Insert edge of cube: '))
    x = transform(x)
    print(f'LSA: {transform(4*(x**2))}')
    print(f'Volume: {transform(x**3)}')
except ValueError:
    print('Not a number!')