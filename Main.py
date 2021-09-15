import os
import re

# limpa o console
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def optionsMenu():
    print('Selecione uma das opções abaixo:')
    print('1 - Cadastrar Matriz')
    print('2 - Encontrar Caminho')
    print('3 - Mostrar Matriz Cadastrada')
    print('4 - Finalizar')

def InsertValuesMatriz(matriz):
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

def defineMatriz():
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

def searchBestWay(matriz):
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
    print(custo)



def branch_and_bound(matriz, node, goal, solucao_aux, solucao):
    print(matriz[node])
    for idx, adj in enumerate(matriz[node]):
        if idx == node or adj == 0 or solucao_aux.count(idx) > 0 or solucao_aux.count(goal) > 0:
            continue

        if idx == goal:
            if  calcula_custo(solucao_aux, matriz) < calcula_custo(solucao, matriz) or calcula_custo(solucao, matriz) == 0:
                solucao = solucao_aux
                solucao.append(idx)
        else:
            print(f"Adjacencias do vertice: {node}")
            solucao_aux.append(idx)
            print(solucao_aux)
           # print(f"Custo: {calcula_custo(solucao_aux, matriz)}")
           # print(f"Custo sol: {calcula_custo(solucao, matriz)}")
            if calcula_custo(solucao_aux, matriz) < calcula_custo(solucao, matriz) or calcula_custo(solucao, matriz) == 0:
                solucao = branch_and_bound(matriz, idx, goal, solucao_aux.copy(), solucao)
            else:
                solucao_aux.pop()
    print("foi")
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
            optionsMenu()

            result = int(input('Opção: ').strip())

            if result == 1:
                cls()
                matriz = InsertValuesMatriz(defineMatriz())
            elif result == 2:
                cls()
                searchBestWay(matriz)
            elif result == 3:
                cls()
                for x in matriz:
                    print(x)
            elif result == 4:
                close = True
                print('Encerrando...')
            else:
                print('Opção Inválida!\n')
    except Exception as e:
        print('Ocorreu um erro, tente novamente...\n')
        print(e)
    

if __name__ == '__main__':
    menu()