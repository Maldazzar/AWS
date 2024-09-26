def calcular_idade():
    import datetime
    ano_atual = 2022
    nome_completo = input("Digite seu nome completo: ")
    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                idade = ano_atual - ano_nascimento
                print(f"{nome_completo}, você completou ou completará {idade} anos em {ano_atual}.")
                break
            else:
                print("Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido para o ano.")
calcular_idade()