import os
import re
import random
from igraph import *

# limpa o console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def options_menu(matriz):
    print('Selecione uma das opções abaixo:')
    print('1 - Cadastrar Matriz')
    print('2 - Gerar Matriz Aleatória')
    print('3 - Usar matriz de exemplo')
    if len(matriz) > 0:
        print('4 - Mostrar Matriz Cadastrada')
        print('5 - Encontrar Caminho')
    print('0 - Finalizar')

def generate_matriz_random():
    numbers = [-1, 0, 1, 2, 3, 4, 0, 6, 7, 0]
    
    size_matriz = random.randint(2, 6)
    matriz = [[ 0 if random.randint(0, 1) == 0 else random.choice(numbers) for x in range(size_matriz)] for y in range(size_matriz)]
    return matriz

def Insert_values_matriz(matriz):
    data = matriz
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            valid = False
            while not valid:
                result = input(f'Insira o valor entre o vértice {i} e o vértice {j}: ').strip()
                if re.match('^[-+]?[0-9]*\.?[0-9]+$', result):
                    data[i][j] = int(result)
                    valid = True
                else:
                    print('\nValor inválido!\n')

    return matriz

def define_matriz():
    print('------------------- Definindo Matriz -------------------')

    matriz = []
    valid = False
    while not valid:
        cls()
        try:
            size = int(input('Insira a quantidade de vértices da matriz: ').strip())

            if size:
                matriz = [[0 for x in range(size)] for y in range(size)]
                valid = True
        except:
            print('\nInsira valores válidos!\n')

    return matriz

def define_matriz_exemplo():
    matriz = []
    matriz.append([0,6,0,0,0,0])
    matriz.append([0,0,-1,0,5,0])
    matriz.append([0,3,0,2,0,0])
    matriz.append([0,0,0,0,0,0])
    matriz.append([0,0,0,5,0,5])
    matriz.append([0,6,0,0,0,1])

    return matriz

def search_best_way(matriz):
    start = int(input('Start: ').strip())
    goal = int(input('Goal: ').strip())
    solucao = list()

    solucao = branch_and_bound(matriz, start, goal, [start], solucao)

    if len(solucao) > 0:
        print("\nExiste uma solução viável: \n")
        print(solucao)
        print("\n")
    else:
        print("\n\nNão existe uma solução viável\n\n")



def branch_and_bound(matriz, node, goal, solucao_aux, solucao):
    for idx, adj in enumerate(matriz[node]):
        if idx == node or adj == 0 or solucao_aux.count(idx) > 0 or solucao_aux.count(goal) > 0:
            continue

        if idx == goal:
            solucao_aux.append(idx)

            if  valida_solucoes(solucao, solucao_aux, matriz):
                solucao = solucao_aux
        else:
            solucao_aux_2 = solucao_aux.copy()
            solucao_aux_2.append(idx)

            if valida_solucoes(solucao, solucao_aux_2, matriz):
                solucao = branch_and_bound(matriz, idx, goal, solucao_aux_2, solucao)

    return solucao

def calcula_custo(solucao, matriz):
    soma = 0
    for i in range(0, len(solucao)-1):
        if matriz[solucao[i]][solucao[i+1]] == -1:
            return -1

        soma += matriz[solucao[i]][solucao[i+1]]
    return soma

def valida_solucoes(solucao, solucao_aux, matriz):
    custo_solucao =  calcula_custo(solucao, matriz)
    custo_solucao_aux = calcula_custo(solucao_aux, matriz)

    return (custo_solucao_aux < custo_solucao or custo_solucao == 0) and custo_solucao_aux != -1

def menu():
    cls()
    try:
        close = False
        matriz = []
        while close != True:
            options_menu(matriz)

            result = int(input('Opção: ').strip())

            if result == 1:
                cls()
                matriz = Insert_values_matriz(define_matriz())
            elif result == 2:
                cls()
                matriz = generate_matriz_random()
                print('\nMatriz gerada com sucesso!\n')
            elif result == 3:
                cls()
                matriz = define_matriz_exemplo()
                print("\nMatriz criada com sucesso!\n")
            elif result == 4 and len(matriz) > 0:
                cls()
                print("\n\n=================== Matriz utilizada ===================")
                for i in matriz:
                   print(i)

                print("=========================================================\n\n")

                edges = []
                weight_edges = []
                try:
                    for x in range(0, len(matriz)):
                        for y in range(0, len(matriz)):
                            if(matriz[x][y] != 0):
                                edges.append([x, y])
                                weight_edges.append(matriz[x][y])
                    g = Graph(n=len(matriz), edges=edges, directed=True)  
                    g.es['weight'] = weight_edges
                    g.es['label'] = weight_edges

                    plot(g, vertex_label=range(0,len(matriz)), vertex_color="white")
                except:
                    cls()
            elif result == 5 and len(matriz) > 0:
                cls()
                search_best_way(matriz)
            elif result == 0:
                close = True
                print('Encerrando...')
            else:
                print('Opção Inválida!\n')
    except Exception as e:
        print('Ocorreu um erro, tente novamente...\n\n')
        print(e)
    

if __name__ == '__main__':
    menu()