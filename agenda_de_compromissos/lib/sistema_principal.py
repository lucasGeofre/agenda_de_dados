from agenda_de_compromissos.lib.arquivo import *
from agenda_de_compromissos.lib.interface import *

arq = 'agenda.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resposta = menu(['adicionar compromisso', 'alterar compromisso','excluir compromisso','ver listas de compromissos','sair'])
    if resposta == 1:
        cabeçalho('Adicionar compromisso')
        criar_compromisso(arq)
    if resposta == 2:
        cabeçalho('Alterar compromisso')
