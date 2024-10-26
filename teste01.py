print('Calculadora')
opcoes = [0,1,2,3,4]
while True == True:
    escolha = int(input('''Escolha sua opcão
[0]adicão
[1]subtração
[2]multiplicação
[3]divisao
        :   '''))
    if escolha == 0:
        print("voce escolheu adição")
        n1 = int(input("digite um numero: "))
        n2 = int(input("Digite putro numero: "))
        n3 = n1+n2
        print(f"A soma entre {n1}+{n2} é igual a {n3}")
    elif escolha == 1:
        print("voce escolheu subtração")
        n1 = int(input("digite um numero: "))
        n2 = int(input("Digite putro numero: "))
        n3 = n1-n2
        print(f"A subttração entre {n1}-{n2} é igual a {n3}")
    elif escolha == 2:
        print("voce escolheu multiplicação")
        n1 = int(input("digite um numero: "))
        n2 = int(input("Digite putro numero: "))
        n3 = n1*n2
        print(f"A mult entre {n1}*{n2} é igual a {n3}")
    elif escolha == 3:
        print("voce escolheu divisão")
        n1 = int(input("digite um numero: "))
        n2 = int(input("Digite putro numero: "))
        n3 = n1/n2
        print(f"A divisao entre {n1}/{n2} é igual a {n3}")
    else:
        print("opção invalida")
