escolhass = []
def escolher():
    import random
    escolhas = []

    nomes = ['julio', 'rogerio', 'sergio', 'mateuso',
            'joão', 'eudes', 'igor', 'lula', 'dilma', 'bolsonaro']

    pronomes = ['eu', 'tu', 'eles', 'nós', 'vós', 'eles', 'elas']

    acoes = ['pular', 'deitar', 'correr', 'chorar', 'sentar', 'dar']

    nome_escolhido = random.choices(nomes,k=2)

    pronome_escolhido = random.choices(pronomes, k=2)

    acao_escolhida = random.choices(acoes, k=2)
    for nome in nome_escolhido:
        escolhas.append(nome)
    for pronome in pronome_escolhido:
        escolhas. append(pronome)
    for acao in acao_escolhida:
        escolhas.append(acao)
    random.shuffle(escolhas)
    for p in escolhas:
        print(p,end=' ')
    escolhass = escolhas
    print()

escolher()
indexado = 0
frase = str(input('digite a frase com essas palavras: ')).strip()

for palavra in frase.split():
    if palavra.lower() in escolhass:
        indexado = escolhass.index(palavra)
        escolhass.pop(indexado)

if len(escolhass) <1:
    print('parabéns vc conseguiu fazer uma frase com todas as palavras')



