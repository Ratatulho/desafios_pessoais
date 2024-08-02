def escolher():
    import random


    senha = []

    simbolos = ['@', '!', '#', '$', '%', '&', '?']

    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

    primeiro_caracter = random.choice(minusculas).upper()

    cincocaracter = random.choices(minusculas, k=5)

    ano = []

    escolhidos = []

    for numero in range(4):
        ano.append(random.randint(0,9))

    for c in range(4):
        escolhidos.append(random.choice(simbolos))

    senha.append(primeiro_caracter)

    for caractere in cincocaracter:
        senha.append(caractere)

    for numero in ano:
        senha.append(numero)

    for simbol in escolhidos:
        senha.append(simbol)

    for t in senha:
        print(t,end='')
    senha.clear
    print()
for c in range(int(input('quantas senhas diferentes vc deseja gerar?'))):
    escolher()


