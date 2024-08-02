from time import sleep

def esperar(tempo):
    for c in range(tempo,0,-1):
        print(c)
        sleep(1)

esperar(int(input('quantos segundos vc deseja esperar?')))
