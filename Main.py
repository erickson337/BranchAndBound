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
    data:list = matriz
    count:int = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            count += 1
            valid = False
            while not valid:
                result:str = input(f'Insira o {count}° valor: ').strip()
                if re.match('^[0-9]*$', result):
                    data[i][j] = int(result)
                    valid = True
                else:
                    print('Valor inválido!')

    return matriz

def defineMatriz():
    print('------------------- Definindo Matriz -------------------')

    matriz:list = []
    valid:bool = False
    while not valid:
        cls()
        try:
            line:int = int(input('Insira a quantidade de linhas: ').strip())
            column:int = int(input('Insira a quantidade de colunas: ').strip())

            if line and column:
                matriz = [[0 for x in range(line)] for y in range(column)]
                valid = True
        except:
            print('Insira valores válidos!\n')

    return matriz

def searchBestWay(matriz):
    pass

def menu():
    try:
        close:bool = False
        matriz:list = []
        while close != True:
            optionsMenu()

            result:int = int(input('Opção: ').strip())

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