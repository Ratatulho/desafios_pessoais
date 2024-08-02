import os
passo = []
def mover(direcao):
    if direcao == 'w':
        coordenadas[0] -=1
    elif direcao == 's':
        coordenadas[0] += 1
    elif direcao == 'd':
        coordenadas[1] += 1
    elif direcao == 'a':
        coordenadas[1] -= 1
    passo = coordenadas
    if passo[0] not in range(0,10) and passo[1] not in range(0,10):
        return False 


coordenadas = [0,0]
def mostrar():
    for linha in range(0,10):
        for coluna in range(0,10):
            if coordenadas == [linha,coluna]:
                print(' 😉',end='')
            else:
                print(' #',end='')
        print()
while True:
    mostrar()
    direcao = input('digite a direção')
    mover(direcao)
    os.system('cls')
