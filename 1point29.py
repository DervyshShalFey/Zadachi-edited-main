from transformation import *
try:
    x = float(input('Insert radius of circle: '))
    x = transform(x)
    print(f'Length: {transform(2*3.14*x)}')
    print(f'Area: {transform(3.14*(x**2))}')
except ValueError:
    print('Not a number!')