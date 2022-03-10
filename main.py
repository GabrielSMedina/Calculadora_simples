import inputs
import operacoes

# Criando o dicionario que armazena nossas chamadas de funções
dic = {'+': operacoes.soma,
       '-': operacoes.subtracao,
       '*': operacoes.multiplicacao,
       '/': operacoes.divisao,
       '**': operacoes.exponencial,
       'r': operacoes.raiz
       }

# Definindo algumas variaveis
letra = None
resultado = None

# Mostrando as operações possiveis ao usuario
print(f'Operações:\n+ = soma\n- = subtração\n* = multiplicação'
      f'\n/ = divisão\n** = potencia na forma (n1**n2)\nr = n1 ** 1/n2\n\n')

# Iniciando o loop
while True:
    # Iniciando uma nova operação sem dependencia da operação anterior
    if letra is None:
        #inputs
        n1, op, n2 = inputs.entrada()
        func = dic[op]
        resultado = func(n1, n2)
        print(f"{n1} {op}  {n2} : {resultado}")
        letra = ''
    letra = input('Deseja continuar esta operação(y/n)? ')
    # Continuara a operação com o resultado anterior
    if letra == 'y':
        n1 = resultado
        op, n2 = inputs.entrada_continua(n1)
        func = dic[op]
        resultado = func(n1, n2)
        print(f"{n1} {op}  {n2} : {resultado}")
    else:
        letra = input('Deseja fazer uma nova operação(y/n)? ')
        # Finaliza o programa
        if letra == 'n':
            print('--Encerrando Calculadora--')
            break
        # Reinicia a calcularora
        else:
            letra = None
