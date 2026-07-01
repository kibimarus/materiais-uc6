#? Criando uma lista vazia
from operator import truediv
from pickle import TRUE
from traceback import print_tb


produtos = []

#? Variavel auxiliar para controlar loop principal
sair = False

print("Bem-vindo ao Sistema de Estoque")
#? Repita enquanto sair é igual a False 
while sair == False:
    #? Menu dentro do loop para repetir
    print("_"*29)
    print("1-Listar produtos")
    print("2-Cadastrar um Novo produto")
    print("3-Deletar um produto")
    print("0-Sair do Sistema")
    #? pedir para a pessoa digitar a opção:
    opcao = input("sua opção: ")
    print("_"*29)
    #? Escolha caso/ match case
    match opcao:
        case '0':
            sair = True
            #colocamos sair como verdadeiro que quando rodar o loop  ele sair.
            sair = True
        case '1':
             print("Lista de produtos:")
             for p in produtos:
                 print("-", p)
             print("#"*30)
             input("Pressione ENTER para continuar...")
        case '2':
            print("Cadastrar novo produto: ")
            nome_produto = input ("Nome do produto: ")
            #? A função append adiciona um novo item em uma lista
            produtos.append(nome_produto)
        case '3':
            print("Remover produto: ")
            nome_produto = input("Qual deletar: ")
            # checar se o deletado existe na lista
            if nome_produto in produtos:
                produtos.remove(nome_produto)
                print("Removido com sucesso!")
            else:
                print(nome_produto, "Não existe na lista!")

            input("Pressione ENTER para continuar...")
            