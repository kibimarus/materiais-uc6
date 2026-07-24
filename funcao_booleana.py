
#? Variáveis booleanas são variáveis que aceitam apenas
#? dois tipos de valores: true e false

#? muito usada para situações de "Apenas dois casos" SIM ou NÃO

def eh_idoso(idade):
    if idade >=60:
        return True
    else: 
        return False

def pode_usar_excalibur(nivel,classe):
    if nivel >= 100 and classe =="Paladino":
        return True
    elif nivel >= 500:
        return True
    else:
        return False

idade = int(input("Digite sua idade: "))

if eh_idoso(idade):
    print("Seja Bem-vindo ao sistema: Melhor idade ++")
    input("Pressione ENTER para continuar...")

else:
    print("Esse sistema é exclusivo para Idosos")
    input("Pressione ENTER para continuar...")


nivel = 500 
classe = "mago" 

if pode_usar_excalibur(nivel,classe):
    print("Equipou")