from agenda_de_compromissos.lib.interface import *


def leia_hora():
    while True:
        try:
            n = str(input('Hora(hh:mm):'))
            if n.find(':') == -1:
                print('formato invalido')
            else:
                m = n.split(':')
                if not m[0].isnumeric:
                    print('ERR01')
                elif not m[1].isnumeric:
                    print('ERR02')
                elif m[0] >= '24' or m[0] < '0' or m[1] >= '60' or m[1] < '0':
                    print('ERR03')
                else:
                    return f'{m[0]}:{m[1]}'
        except:
            print('ERR04')


def leia_data():
    global mes, dia, ano
    while True:
        try:
            dia = int(input('dia:'))
            mes = int(input('mes:'))
            ano = int(input('ano'))
        except:
            print('Erro')

        if dia <= 0 or dia >= 31 or mes >= 12 or mes <= 0:
            print('ERR0! não existe essa data')

        elif ano < 2020:
            print('Esse ano já se passou')

        else:
            print('data lida')
            n = {f'{dia}/{mes}/{ano}'}
            return n


def criar_compromisso(arq):
    try:
        a = open(arq, 'at')
    except:
        print('houve um erro no arquivo!!!')
    else:
        try:
            l = str(input('compromisso:'))
            n = leia_data()
            m = leia_hora()
            o = str(input('descrição:'))

            a.write(f'compromisso: {l};data: {n};Hora {m};Descrição: {o}\n')
        except:
            print('Err0 ao criar arquivo!!!')
        else:
            print(cabeçalho('Compromisso adicionado!'))


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('houve um ERR0')
    else:
        print(f'{nome} foi criado')


def adicionar_compromisso(arq):
    try:
        a = open(arq)
        compromisso = criar_compromisso()
    except:
        print('huve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{compromisso}')
        except:
            print('houve um erro!')
        else:
            print('o compromisso foi criado')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler o arquivo!')
    else:
        cabeçalho('Compromissos')
        for linha in a:
            p = linha.replace(';', '\n')
            print(p)

    finally:
        a.close()


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
