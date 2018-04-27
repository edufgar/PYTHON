from math import sqrt

print('\33[32m-=-\33[m' * 20)
print('\33[30m                Cálculo da Fórmula de Bhaskara\33[m')
print('\33[32m-=-\33[m' * 20)

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

delta = sqrt((b**2) - (4*a*c))

if delta < 0:
    print('Raiz negativa nao pode ser extraida.')
    exit()
else:
    x1 = (-b + delta) / (2 * a)
    x2 = (-b - delta) / (2 * a)

print('\nO valor de X1 será de {}'.format(x1))
print('O valor de X2 será de {}'.format(x2))