from email.errors import InvalidDateDefect
import math
#? Parâmetros são valores 'de fora da função'que são passados em sua chamada
#? é quando uma função NECESSITA de um valor para funcionar

def calcular_idade(ano_nascimento):
    print("Ano de nascimento é: ", ano_nascimento)
    idade = 2026 - ano_nascimento
    print("A idade é: ", idade)
    
print("Chamando função: ")    
calcular_idade(2009)

meu_ano_nascimento = 2009
calcular_idade(meu_ano_nascimento)

ano_perguntado = int(input("Digite um ano de nascimento: "))
calcular_idade(ano_perguntado)
