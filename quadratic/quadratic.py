a = float(input('enter value of a '))
b = float(input('enter value of b '))
c = float(input('enter value of c '))

# isq = ((b**2) - (4*a*c))
# sq = (isq ** 0.5)
# nB = (-b)
# on = (nB + isq)
# dv = (on / (2*a))

# print(dv)

topEquationPlus = ((-1 * b) + (((b**2) - (4*a*c)) ** 0.5))
divideBy2Plus = (topEquationPlus / (2*a))

topEquationMinus = ((-1 * b) - (((b**2) - (4*a*c)) ** 0.5))
divideBy2Minus = (topEquationMinus / (2*a))

RootMinus = (((b**2) - (4*a*c)))

if RootMinus < 0:
    print('You cant square root a negative number. input another value.')
else: print(f'x = {divideBy2Plus} and x = {divideBy2Minus}')

