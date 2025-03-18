N=int(input('ingresa un valor entero: '))
M=int(input('ingresa otro valor entero: '))
if N<M:
    for i in range(N,M,1):
        if i%2 == 0:
            print(i, ' es par')
        else:
            print(i, ' es impar')
else:
    for i in range(N, M, -1):
        if i%2 == 0:
            print(i, ' es par')
        else:
            print(i, ' es impar')