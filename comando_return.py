 #? c
def calcular_anos_caninos(idade):
    idade_humana = 0
    if idade >= 1:
        idade_humana = 15
    
    if idade >= 2:
        idade_humana += 9
    
    if idade >= 3:
        idade_humana += (idade - 2) * 5

    #? transformam=ndo função em resultado
    #? o comando  'return' faz com que um valor possa ser extraído daqui
    #? eu estou falando que o 'idade_humano' é o resultado desta função. ou o valor que é exportado 
    return idade_humana

    #? ESCOPO GLOBAL  (COLADO A ESQUERDA )
    #? chamando função 
idade_final = calcular_anos_caninos(5)
print("A idade humana é  ", idade_final)

print("O segundo dog tem: ",)
calcular_anos_caninos(12)," anos humanos"'