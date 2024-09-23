def calculadora():
    num1 = float(input("Digite o primeiro número: "))
    if num1.is_integer():
        num1 = int(num1)
    num2 = float(input("Digite o segundo número: "))
    if num2.is_integer():
        num2 = int(num2)
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    operacao = int(input("Digite o número da operação desejada: "))    
    if operacao == 1:
        resultado = num1 + num2
        operacao_nome = "Soma"
    elif operacao == 2:
        resultado = num1 - num2
        operacao_nome = "Subtração"
    elif operacao == 3:
        resultado = num1 * num2
        operacao_nome = "Multiplicação"
    elif operacao == 4:
        if num2 != 0:
            resultado = num1 / num2
            operacao_nome = "Divisão"
        else:
            print("Erro: divisão por zero.")
            return
    else:
        print("Operação inválida. O resultado será 0.")
        exit()
    if isinstance(resultado, float) and resultado.is_integer():
        resultado = int(resultado)
    
    print(f"O resultado da {operacao_nome} entre {num1} e {num2} é {resultado}.")

calculadora()