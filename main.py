import inputs
import operacoes

dic = {'+': operacoes.soma,
       '-': operacoes.subtracao,
       '*': operacoes.multiplicacao,
       '/': operacoes.divisao,
       '**': operacoes.exponencial,
       'r': operacoes.raiz
       }

letra = None
resultado = None

print(f'Operações:\n+ = soma\n- = subtração\n* = multiplicação'
      f'\n/ = divisão\n** = potencia na forma (n1**n2)\nr = n1 ** 1/n2\n\n')

while True:
    if letra is None:
        n1, op, n2 = inputs.entrada()
        func = dic[op]
        resultado = func(n1, n2)
        print(f"{n1} {op}  {n2} : {resultado}")
        letra = 'a'
    letra = input('Deseja continuar esta operação(y/n)? ')
    if letra == 'y':
        n1 = resultado
        op, n2 = inputs.entrada_continua(n1)
        func = dic[op]
        resultado = func(n1, n2)
        print(f"{n1} {op}  {n2} : {resultado}")
    else:
        letra = input('Deseja fazer uma nova operação(y/n)? ')
        if letra == 'n':
            print('--Encerrando Calculadora--')
            break
        else:
            letra = None
