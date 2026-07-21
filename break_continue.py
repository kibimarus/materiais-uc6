 #& Break e  continue são comandos para controlar loops (Laços de repetição)

contador = 0
maximo = 50

while contador < maximo:
    #! O sinal"+=" quer dizer "Mais e igual"
    #? E quando queremos "Adicionar" um valor variável
    #? É a forma resumida de: contador = contador + 1
    #? É a forma de "não perder oque tem de varíavel" e adicionar aquele valor
    #? se o contador tem 5. contador +=1 || ele vai para sem
    contador += 1
    

    # & comando break e continue 
    #& se o resto da divisão de contador atual for 0
    #& OU :  se o contador for  da tabuada do 4 então...
    #& continue =  Interrompe o loop aqui e vai  para a próxima repetição

    if contador % 4 == 0:
        continue

    if contador == 38:
        break

    print(contador)

print("FIM DO CÓDIGO")
