from tkinter import * 

soma = 0


def somar():
    global soma
    soma += 1
    atualizar_resultado()

def subtrair():
    global soma
    soma -= 1
    atualizar_resultado()

def atualizar_resultado():
    resultado.config(text=str(soma))

principal = Tk()
principal.title('soma')
principal.geometry('200x200')

texto_orientacao = Label(principal, text='faça a soma aq ó -->')
texto_orientacao.grid(column=0,row=0, padx= 10, pady= 10)

botao_subtracao = Button(principal,text='     -      ',command=subtrair)
botao_subtracao.grid(column=1,row=2, padx= 10, pady= 10)

botao_adicao = Button(principal,text='     +     ',command=somar)
botao_adicao.grid(column=1,row=0, padx= 10, pady= 10)

resultado = Label(principal,text='0')
resultado.grid(column=1,row=1)

principal.mainloop()