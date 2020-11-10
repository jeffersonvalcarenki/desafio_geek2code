CARACTERE = '#'
ESPACO = ' '

print('Informe n de 1 a 1000...')
n = int(input())
if n in range(1, 1000):

    def imprimir_linha(linha):
        def adicionar_espacos(quantidade):
            string = ''
            for _ in range(0, quantidade):
                string += ESPACO
            return string

        if linha == 0:
            string = ''
            string += adicionar_espacos(n)
            string += CARACTERE
            return string
        else:
            string = ''
            string += adicionar_espacos(n-linha)
            string += CARACTERE
            string += adicionar_espacos((linha*2)-1)
            string += CARACTERE
            return string

    for linha in range(0, n-1):
        print(imprimir_linha(linha))

    for linha in range(n-1, -1, -1):
        print(imprimir_linha(linha))
    
