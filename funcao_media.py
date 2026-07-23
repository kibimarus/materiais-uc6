
#esta função tem 3 PARAMETROS
def calcular_media(n1,n2,n3):
    media = (n1+n2+n3) / 3
    #round(~var~, 1 = vai arredondar o número com 1 número após a  virgula)
    print("A média é: ", round(media,1))

    if media >= 6:
        print("Situação: Aprovado!")
    elif media >= 4:
        print("Situação: Recuperação!")
    else:
        print("Situação: Reprovado!")

    print("Aluno 1: ")
    calcular_media(8.5,10,2)

    print("Aluno 2: ")
    
n1_aluno2 = 5
n2_aluno2 = 2
n3_aluno2 = 10
calcular_media(n1_aluno2,  n2_aluno2,  n3_aluno2)