CARACTERE = '#'
ESPACO = ' '

print('Informe n de 1 a 1000...')
n = int(input())
if n in range(1, 1000):

    def imprimirLinha(linha):
        def adicionarEspacos(quantidade):
            string = ''
            for _ in range(0, quantidade):
                string += ESPACO
            return string

        if linha == 0:
            string = ''
            string += adicionarEspacos(n)
            string += CARACTERE
            return string
        else:
            string = ''
            string += adicionarEspacos(n-linha)
            string += CARACTERE
            string += adicionarEspacos((linha*2)-1)
            string += CARACTERE
            return string

    for linha in range(0, n-1):
        print(imprimirLinha(linha))

    for linha in range(n-1, -1, -1):
        print(imprimirLinha(linha))
    