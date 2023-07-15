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
        print(f'{nome}\t{origem}\t{ida[0]}-{ida[1]}\tR${ida[2]}\t{volta[0]}-{volta[1]}\t{volta[2]}')

agenda = [1,4, 3,2, 7,3, 6,3, 2,4, 5,3]
imprimir_agenda(agenda)

# Função para converter um horário em minutos
def get_minutos(hora):
    x = time.strptime(hora,'%H:%M')
    minutos = x[3] * 60 + x[4]
    return minutos

# Função objetivo

def funcao_custo(solucao):
    preco_total = 0

    # menor valor possível
    ultima_chegada = 0

    # maior valor possível
    primeira_partida = 1439
    id_voo = -1
    
    for i in range(len(solucao)//2):
        origem = pessoas[i][1]
        id_voo += 1
        ida = voos[(origem, destino)][solucao[id_voo]]
        id_voo += 1
        volta = voos[(destino, origem)][solucao[id_voo]]    
        preco_total += ida[2]
        preco_total += volta[2]

        # Atualizando as variáveis extremas
        if ultima_chegada < get_minutos(ida[1]):
            ultima_chegada = get_minutos(ida[1])
        
        if primeira_partida > get_minutos(volta[0]):
            primeira_partida = get_minutos(volta[0])
        
    # Calcular o tempo de espera
    total_espera = 0

    for i in range(len(solucao)//2):
        origem = pessoas[i[1]]
        id_voo += 1
        ida = voos[(origem,destino)][solucao[id_voo]]
        id_voo += 1
        volta = voos[(destino,origem)][solucao[id_voo]]

        total_espera += ultima_chegada - get_minutos(ida[1])
        total_espera += get_minutos(volta[0]) - primeira_partida
        
        if ultima_chegada > primeira_partida:
            preco_total += 50
    return preco_total + total_espera

funcao_custo(agenda)