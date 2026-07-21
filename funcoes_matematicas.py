import  math
from traceback import print_tb
# ? Acima importamos as funções matemáticas do python 

#? sem essa importação as informações ficam 'travadas' ou impossibilitadas de serem usadas

#? Aqui poderemos ver o padrão  ao usar FUNÇÕES na programação

nota_bimestre = 8.7

print("Arredondando para baixo:", math.floor(nota_bimestre))
print("Arredondando para cima:", math.ceil(8.1))
print("Arredondando por proximidade:", round(5.6))
print("Arredondando por proximidade:", round(9.4))


#* No caso do math.pow() ele pede 2 parâmetros 
#*... Que é o valor e o expoente.
print ("calculando potência: ", math.pow(20,3))