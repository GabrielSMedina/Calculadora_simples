import inputs
import operacoes

dic = {'+': operacoes.soma,
       '-': operacoes.subtracao,
       '*': operacoes.multiplicacao,
       '/': operacoes.divisao
       }

continuar = 'y'
encerrar = False
txt_sair = 'n'

n1, op, n2 = inputs.entrada()
func = dic[op]
resultado = func(n1, n2)

print(f"{n1} {op}  {n2} : {resultado}")
'''while not encerrar:
    

    if txt_sair == 'y':
        encerrar = True'''