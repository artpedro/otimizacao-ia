# IA: Algoritmos de Otimização em Python

# EMENTA

## Introdução a IA e a importância dos processos de otimização

## Algoritmos de Otimização:

### Soluções eficientes (ótimas) para problemas complexos;
### Ferramentas matemáticas exectuadas de forma iterativa,
### até que uma solução ótima, ou pelo menos satifatória, seja encontrada;
### Encontrar a combinação ideal das variáveis de decisão que
### otimizem a função objetivo, levando em consideração as restrições impostas;

### Variaveis - Restrições - Função objetivo (max ou min):

#### - Variáveis de decisão: escolhas feitas para resolver o problema;

#### - Função objetivo: medida quantitativa que deve ser maximizada ou minimizada;

#### - Restrições: condições limitantes das soluções, devem ser respeitadas.

### Exemplos:

#### Algoritmos de busca local: Solução inicial -> Busca local -> Novos valores ótimos;
##### Máximo local: melhor valor num conjunto discreto de dados;
##### Máximo global: melhor valor no conjunto total.


#### Algoritmos genético: Algoritmo de otimização baseado em conceitos de seleção natural.

#### Algoritmo enxame de partículas: Inspirado no comportamento coletivo de um grupo de
### indivíduos em direção a um objetivo comum. Ajusta-se as velocidades e direções das partículas no espaço.


#### Algoritmo de recozimento simulado: Busca estocástica.

## Viagem em grupo e algoritmos aplicáveis

### Desafio clássico de otimização. Organização eficiente de grupos de pessoas,
### considerando diversas restrições e variáveis.

# Variáveis do problema:
import time
import random
import math

pessoas = [('Amanda','CWB'),
           ('Pedro','GIG'),
           ('Marcos','POA'),
           ('Priscila','FLN'),
           ('Jessica','CNF'),
           ('Paulo','GYN')]

destino = 'GRU'

voos = {}

for linha in open('data/voos.txt'):

    _origem, _destino, _saida, _chegada, _preco = linha.split(',')

    voos.setdefault((_origem,_destino),[])
    
    voos[(_origem, _destino)].append((_saida,_chegada,int(_preco)))

#Impressão da agenda de Voos
# [1,4, 3,2, 7,3, 6,3, 2,4, 5,3] exemplo de lista de pessoas com voos que irão ser pegos

def imprimir_agenda(agenda):
    id_voo = -1
    for i in range(len(agenda) // 2): #(//2 para pegar os dados em dupla)
        nome = pessoas[i][0] 
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][agenda[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][agenda[id_voo]]
        print('%10s%10s %5s-%5s R$%3s %5s-%5s R$%3s' % (nome, origem, ida[0], ida[1], ida[2],
                                                       volta[0], volta[1], volta[2]))
        
agenda = [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
imprimir_agenda(agenda)

## Pesquisa randômica

## Método Hill climb

## Simulated annealing

## Algoritmos Genéticos

## Estudo de caso: Representação do problema dos dormitórios