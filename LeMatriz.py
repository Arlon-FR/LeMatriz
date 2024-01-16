def criar_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        matriz.append(linha)
        
    return matriz

def imprimir_matriz(m):
    for linha in m:
        for elemento in linha:
            print(elemento, end=' ')
        print()


def Le_matriz():
    lin = int(input("Digite o número de linhas: "))
    col = int(input("Digite o número de colunas: "))
    return criar_matriz(lin, col)


m = Le_matriz()
print(imprimir_matriz(m))