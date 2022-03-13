# Funcoes
# Funcao de soma
def soma(n1, n2):
    return n1 + n2


# Funcao de subtracao
def subtrai(n1, n2):
    return n1 - n2


# Funcao de multiplicacao
def multiplica(n1, n2):
    return n1 * n2


# Funcao de divide
def divide(n1, n2):
    return n1 / n2


# Funcao de raiz
def raiz(n1, n2):
    return n1 ** 1 / n2


# Funcao de exponencial
def ex(n1, n2):
    return n1 ** n2


# Funcao de atribuicao de valores para resultado inexistente
def input_1():
    n1 = float(input('n1 = '))
    op = input('operacao = ')
    n2 = float(input('n2 = '))
    return n1, op, n2


# Funcao de atribuicao de valores para resultado existente
def input_2():
    op = input('operacao = ')
    n2 = float(input('n2 = '))
    return op, n2


# Dicionario
dicionario = {'+': soma,
              '-': subtrai,
              '*': multiplica,
              '/': divide,
              'r': raiz,
              '**': ex}

# Variaveis
# Variavel que dita se uma opecarao sera feita do zero
resultado = None

# Loop princial
while True:
    # Checa se existe um resultado previo
    if resultado is None:
        # Pega informacoes da operacao e os numeros
        n1, op, n2 = input_1()
        # Verifica se a operacao esta presente no dicionario
        if op in dicionario:
            funcao = dicionario[op]
            # Chama funcao
            resultado = funcao(n1, n2)
            print(f'{n1} {op} {n2} = {resultado}')
        else:
            print('Operacao invalida!')
    else:
        n1 = resultado
        print(f'n1 = {n1}')
        # Pega informacoes da operacao e os numeros
        op, n2 = input_2()
        # Verifica se a operacao esta presente no dicionario
        if op in dicionario:
            funcao = dicionario[op]
            # Chama funcao
            resultado = funcao(n1, n2)
            print(f'{n1} {op} {n2} = {resultado}')
        else:
            print('Operacao invalida!')

    pergunta = input('Deseja continuar esta operacao(y/n): ')
    if pergunta == 'n':
        resultado = None
        pergunta_2 = input('Deseja fazer uma nova operacao(y/n): ')

        if pergunta_2 == 'n':
            break
