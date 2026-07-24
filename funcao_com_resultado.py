import math
def unir_nomes(nome,sobrenome):
    #? soma de nomes = conicatenação
    nome_completo = nome + "" + sobrenome 
    print("O nome completo é: ", nome_completo)

unir_nomes("Cuca", "Beludo")
#? a diferença entre função ' com resultado' e 'sem resultado' 

potencia = math.pow(25,5) 
print("A potência é ", potencia)

nome = unir_nomes("Mudrungo","Souza")
print("O nome é ", nome)

#?STRING REPLACE;
#? pega uma string e trocauma palavra ou por um caractere por outro 
pais = "Brasil"
trocado = pais.replace("B","p")
print("O nome trocado é: ", trocado)

