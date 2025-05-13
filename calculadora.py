print('\t -- Calculadora --\n')

n1 = input('Número 1: ')
n2 = input('Número 2: ')

# Verifica se os valores são válidos (números reais)
if n1.replace('.', '', 1).replace('-', '', 1).isdigit() and n2.replace('.', '', 1).replace('-', '', 1).isdigit():
    n1 = float(n1)
    n2 = float(n2)

    op = -1
    while op != 0:
        op = input("Escolha a operação que deseja realizar: \n\t1 - Adição\n\t2 - Subtração\n\t3 - Multiplicação\n\t4 - Divisão\n\t5 - Potenciação\n\t0 - Sair\n")

        if op == "0":
            print("Saindo...")
        elif op == "1":
            print("Resultado: ", n1 + n2)
        elif op == "2":
            print("Resultado: ", n1 - n2)
        elif op == "3":
            print("Resultado: ", n1 * n2)
        elif op == "4":
            if n2 == 0:
                print("Erro: divisão por zero.")
            else:
                print("Resultado: ", n1 / n2)
        elif op == "5":
            print("Resultado: ", n1 ** n2)cd
        else:
            print("Operação inválida.")
else:
    print("Erro: pelo menos um dos valores informados não é um número.")
