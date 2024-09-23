def calculadoraManual():
    op = 1
    while op != 0:
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        numero1 = float(input("Digite o primeiro número: "))
        if numero1.is_integer():
            numero1 = int(numero1)
        numero2 = float(input("Digite o segundo número: "))
        if numero2.is_integer():
            numero2 = int(numero2)
        op = int(input("Digite qual a operação deseja usar: "))
        if op == 1:
            resultado = numero1 + numero2
            op_nome = "soma"
        elif op == 2:
            resultado = numero1 - numero2
            op_nome = "subtração"
        elif op == 3:
            resultado = numero1 * numero2
            op_nome = "multiplicação"
        elif op == 4:
            if numero2 == 0:
                while numero2 == 0:
                    print("Erro! Divisor não pode ser 0")
                    numero2 = float(input("Digite outro número para ser o divisor: "))
                    if numero2.is_integer():
                        numero2 = int(numero2)
            resultado = numero1 / numero2
            op_nome = "divisão"
        elif op == 0:
            exit()
        else:
            print("Essa opção não existe")
        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)
        print(f"O resultado da {op_nome} entre {numero1} e {numero2} é {resultado}.")
        op = int(input("Para realizar outra operação digite qualquer número para continuar ou 0 para sair: "))

calculadoraManual()