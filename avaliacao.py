import sys
import os
import numpy as np
import matplotlib.pyplot as plt

## Declarando lambda functions

# recebe um arreio de strings e retorna um arreio de inteiros
int_array = lambda i : [int(d) for d in i]
# lendo conteúdo dos arquivos
ler_entrada = lambda inf, sup=None : [int_array(i.split(' ')) for i in conteudo[inf:sup]]

## Validando a entra de dados

if len(sys.argv) <= 1:
    print('Faltam argumentos!')
    exit()

if not os.path.isfile(sys.argv[1]):
    print('Esse arquivo não é válido!')
    exit()

## Lendo arquivo de entrada

arquivo = open(sys.argv[1], 'r')
conteudo = arquivo.read().split('\n')
arquivo.close()

## Lendo conteúdo do arquivo

numeroDeConsultas = int(conteudo[0])
saidasIdeias = ler_entrada(1, numeroDeConsultas+1)
respostasObtidas = ler_entrada(numeroDeConsultas+1)

## Processando os dados

niveis = np.array([*range(0, 11)])
resultados = []
for index, conjunto in enumerate(respostasObtidas):
    revocacao = []
    precisao = []
    numDoc = 0
    nSaidasIdeias = len(saidasIdeias[index])
    for idx, doc in enumerate(conjunto):
        if doc in saidasIdeias[index]:
            numDoc += 1
            revocacao.append(numDoc/nSaidasIdeias)
            precisao.append(numDoc/(idx+1))
    resultado = []
    for n in niveis:
        p = []
        for i, r in enumerate(revocacao):
            if r >= n/10:
                p.append(precisao[i])
            else:
                p.append(0)
        resultado.append(max(p))
    resultados.append(resultado)
    plt.plot(niveis*10, np.array(resultado) * 100)
    plt.show()

resultadoFinal = {v:0 for v in range(0, 11)}
for i in resultados:
    for k, v in i.items():
        resultadoFinal[k] += v/numeroDeConsultas

plt.plot(resultadoFinal.keys(), resultadoFinal.values())
plt.show()

# Escrevendo arquivo

arquivo = open('media.txt', 'w')
for k in resultadoFinal.values():
    arquivo.write(f'{k:.2f} ')
arquivo.close()
    
#maior precisao nas revocacoes maiores ou iguais a rj
