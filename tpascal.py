def tpascal(n):
    linha = []
    anterior = 0
    for atual in range(n):
        soma = (atual + 1) + anterior
        anterior = (atual + 1)
        linha.append(soma)

    print(linha)
    return linha

assert tpascal(2) == [1,1]