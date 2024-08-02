
cont = num = 0
ganhou = False
jogador = str(input('digite o nome do jogador: '))

adversario = str(input('digite o nome do adversário:'))

jogadas_j = [[], [], [], [], []]

jogadas_a = [[], [], [], []]

def limpar():
    import os
    os.system('cls')
def jogada(jogador):
    jogada = []
    linha = int(input('qual linha vc seleciona?'))
    coluna = int(input('qual coluna vc seleciona? '))
    
    jogada = [linha, coluna]
    return jogada
# erro pode estar acima
#jogadas_a.insert(0, jogada(jogador))
#print(jogadas_a)
    
def mostrar():
    cont = []
    for linha in range(1,4):
        for coluna in range(1,4):

            for jogada in jogadas_j:
                if [linha, coluna] == jogada:
                    print(' O',end='')
                    cont += [1]
            for jogada in jogadas_a:
                if [linha, coluna] == jogada:
                    print(' X',end='')
                    cont += [1]
            if len(cont) == 0:
                print(' #',end='')
            cont.clear()
            
        print()
limpar()
jogadas_a.insert(num,jogada(jogador))
mostrar()
for c in range(4):
    jogadas_j.insert(num, jogada(adversario))
    mostrar()
    jogadas_a.insert(num,jogada(jogador))
    limpar()
    mostrar()

 
    


# por enquanto tudo certo
