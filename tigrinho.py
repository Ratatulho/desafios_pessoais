import random as rd
escolha = []
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogados = []
ganhou = 0
def rolar():
    escolha.clear()
    for linha in range(1,4):
        escolha.append(rd.choice(numeros[:]))

    return escolha


for c in range(int(input('apenas 1000000 reais por jogada😃😃😃[quantas vezes vc quer jogar???] '))):
    rolar()
    jogados.append(escolha[:])
for lista in jogados:

    for numero in lista:

        if lista[0] == lista[1] == lista[2]:
            ganhou += 1

        elif lista[0] == lista[1] or lista[1] == lista[2] or lista [0] == lista[2]:
            ganhou += 1
            #print('aq',end='')

        print(f' {numero}',end='')
    print('\n',end='')
    print('-='*4)
if ganhou > 0:
    print(f'parabens você ganhou {ganhou} vezes e recuperou {1 * ganhou}R$')
