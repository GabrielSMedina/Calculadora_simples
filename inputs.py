def entrada():
    n1 = float(input('n1 = '))
    op = input('operação: ')
    n2 = float(input('n2 = '))

    return n1, op, n2


def entrada_continua(n1):
    print(f'n1 = {n1}')
    op = input('operação: ')
    n2 = float(input('n2 = '))

    return op, n2
