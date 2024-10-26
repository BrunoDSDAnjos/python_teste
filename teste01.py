print('Calculadora')
opcoes = [0,1,2,3,4]
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