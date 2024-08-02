def sigla():
    frase = str(input('digite e saiba sua sigla: '))
    sigla = ''
    #sigla = frase.split()
    for letra in frase.split():
        sigla += letra[0].upper()
    print(sigla)

sigla()

print('-='*30)