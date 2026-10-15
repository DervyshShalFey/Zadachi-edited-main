from transformation import *
try:
    x = float(input('Insert radius of circle: '))
    x = transform(x)
    print(f'Diameter: {transform(x*2)}')
except ValueError:
    print('Not a number!')