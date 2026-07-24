 #? aqui (colado a esquerda) estamos no ESCOPO GLOBAL
def divisao(numb2):
    resultado = numb1 / numb2
    print("O resultado é: ", resultado)

numb1 = 500
divisao(6)
print("O resultado aqui fora é: ",resultado)