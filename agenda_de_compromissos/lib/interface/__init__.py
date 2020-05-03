def lin(tam=42):
    # escreve 42 linhas
    return '-' * tam


def cabeçalho(txt):
    # criar algum titulo
    print(lin())
    print(txt.center(42))
    print(lin())


def leiaint(msg):
    # tenta ler numeros inteiros
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('digite um numero inteiro!')
            continue
        except KeyboardInterrupt:
            print('usuario preferiu não digitar nada')
            return 0
        else:
            return n


def menu(lista):
    # cria um menu que le numeros inteiros
    cabeçalho('Menu Pricipal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(lin())
    opc = leiaint('Sua opção:')
    return opc
