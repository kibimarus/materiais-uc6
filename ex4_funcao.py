def verificacao_velocidade(v1,v2):
    #? v1= velocidade da via v2 = velocidade do veículo
    excesso = v2 - v1
    if v2 >= v1:
        print("Velocidade acima do permitido!") 
        print("Você ultrapassou o limite em ", excesso ,"Km/h")
    else:
        print("Velocidade permitida")


print("-----Verificação de velocidade-----")
v1 = (int(input("Digite o limite da via: ")))
v2 = (int(input("Agora digite a velocidade do veículo: ")))
verificacao_velocidade(v1,v2)
