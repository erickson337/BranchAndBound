import os
import re
import random

# limpa o console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def options_menu():
    print('Selecione uma das opções abaixo:')
    print('1 - Cadastrar Matriz')
    print('2 - Gerar Matriz Aleatória')
    print('3 - Encontrar Caminho')
    print('4 - Mostrar Matriz Cadastrada')
    print('5 - Finalizar')

def generate_matriz_random():
    numbers = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
    size_matriz = random.randint(2, 8)
    matriz = [[random.choice(numbers) for x in range(size_matriz)] for y in range(size_matriz)]
    return matriz

def Insert_values_matriz(matriz):
    data = matriz
    count = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            count += 1
            valid = False
            while not valid:
                result = input(f'Insira o {count}° valor: ').strip()
                if re.match('^[0-9]*$', result):
                    data[i][j] = int(result)
                    valid = True
                else:
                    print('Valor inválido!')

    return matriz

def define_matriz():
    print('------------------- Definindo Matriz -------------------')

    matriz = []
    valid = False
    while not valid:
        cls()
        try:
            line = int(input('Insira a quantidade de linhas: ').strip())
            column = int(input('Insira a quantidade de colunas: ').strip())

            if line and column:
                matriz = [[0 for x in range(line)] for y in range(column)]
                valid = True
        except:
            print('Insira valores válidos!\n')

    return matriz

def search_best_way(matriz):
    matriz = []
    matriz.append([0,6,0,0,0,0])
    matriz.append([0,0,53,0,5,0])
    matriz.append([0,3,0,2,0,0])
    matriz.append([0,0,0,0,0,0])
    matriz.append([0,0,0,5,0,5])
    matriz.append([0,6,0,0,0,1])

    start = int(input('Start: ').strip())
    goal = int(input('Goal: ').strip())
    solucao = list()
    custo = 0

    solucao = branch_and_bound(matriz, start, goal, [start], solucao)

    print(solucao)



def branch_and_bound(matriz, node, goal, solucao_aux, solucao):
    for idx, adj in enumerate(matriz[node]):
        if idx == node or adj == 0 or solucao_aux.count(idx) > 0 or solucao_aux.count(goal) > 0:
            continue

        if idx == goal:
            solucao_aux.append(idx)
            if  calcula_custo(solucao_aux, matriz) < calcula_custo(solucao, matriz) or calcula_custo(solucao, matriz) == 0:
                solucao = solucao_aux
        else:
            solucao_aux_aux = solucao_aux.copy()
            solucao_aux_aux.append(idx)
            if calcula_custo(solucao_aux, matriz) < calcula_custo(solucao, matriz) or calcula_custo(solucao, matriz) == 0:
                solucao = branch_and_bound(matriz, idx, goal, solucao_aux_aux, solucao)

    return solucao

def calcula_custo(solucao, matriz):
    soma = 0
    for i in range(0, len(solucao)-2):
        soma += matriz[solucao[i]][solucao[i+1]]
    return soma

def menu():
    try:
        close = False
        matriz = []
        while close != True:
            options_menu()

            result = int(input('Opção: ').strip())

            if result == 1:
                cls()
                matriz = Insert_values_matriz(define_matriz())
            elif result == 2:
                cls()
                matriz = generate_matriz_random()
                print('Matriz gerada com sucesso!')
            elif result == 3:
                cls()
                search_best_way(matriz)
            elif result == 4:
                cls()
                for x in matriz:
                    print(x)
            elif result == 5:
                close = True
                print('Encerrando...')
            else:
                print('Opção Inválida!\n')
    except Exception as e:
        print('Ocorreu um erro, tente novamente...\n')
        print(e)
    

if __name__ == '__main__':
    menu()