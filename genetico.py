import copy
import random

sudoku = [[5,0,8,6,0,9,4,0,0],[0,0,0,5,0,8,9,3,1],[9,0,0,0,0,4,6,8,0],[2,0,0,0,7,0,8,5,0],[3,0,7,6,0,2,0,0,0],[1,0,9,0,3,8,2,0,0],[0,9,0,3,6,0,0,8,0],[0,0,6,7,9,0,4,2,0],[0,0,6,7,9,0,4,2,0],[5,0,3,8,0,0,7,0,0]]

sudoku = [5,0,8,6,0,9,4,0,0,0,0,0,5,0,8,9,3,1,9,0,0,0,0,4,6,8,0,2,0,0,0,7,0,8,5,0,3,0,7,6,0,2,0,0,0,1,0,9,0,3,8,2,0,0,0,9,0,3,6,0,0,8,0,0,0,6,7,9,0,4,2,0,0,0,6,7,9,0,4,2,0,5,0,3,8,0,0,7,0,0]

sudoku = [5,0,8,0,0,0,9,0,0,6,0,9,5,0,8,0,0,4,4,0,0,9,3,1,6,8,0,2,0,0,3,0,7,1,0,9,0,7,0,6,0,2,0,3,8,8,5,0,0,0,0,2,0,0,0,9,0,0,0,6,5,0,3,3,6,0,7,9,0,8,0,0,0,8,0,4,2,0,7,0,0]

sudoku2 = [
    0,6,0,1,0,4,0,5,0,
    0,0,8,3,0,5,6,0,0,
    2,0,0,0,0,0,0,0,1,
    8,0,0,4,0,7,0,0,6,
    0,0,6,0,0,0,3,0,0,
    7,0,0,9,0,1,0,0,4,
    5,0,0,0,0,0,0,0,2,
    0,0,7,2,0,6,9,0,0,
    0,4,0,5,0,8,0,7,0
]

sudoku2Resuelto = [
    9,6,3,1,7,4,2,5,8,
    1,7,8,3,2,5,6,4,9,
    2,5,4,6,8,9,7,3,1,
    8,2,1,4,3,7,5,9,6,
    4,9,6,8,5,2,3,1,7,
    7,3,5,9,6,1,8,2,4,
    5,8,9,7,1,3,4,6,2,
    3,1,7,2,4,6,9,8,5,
    6,4,2,5,9,8,1,7,3
]



def printSudoku(sudoku):
    for s in sudoku:
        end = 0
        for l in s:
            print(l,end=" ")
            end += 1
            if end == 3:
                print(" ")
                end =0


def checkColumns(sudoku):
    num = 0
    nums = []
    e= 0
    for i in range(9):
        init = num + i
        for j in range(9):
            nums.append(sudoku[init])
            init += 9
        e += errors(nums)
        #print(nums)
        nums = []
    return e

def checkRows(sudoku):
    nums =[]
    e = 0
    num = 9
    for i in range(9):
        for j in range(9):
            nums.append(sudoku[j+(num*i)]) 
        e += errors(nums)
        #print(nums)
        nums = []
    return e

def checkSubSudoku(sudoku):
    numeroQueSeSumaParaCambiarColumna= 3
    numeroQueSumaCambiarFila = 9
    index = 0
    nums = []
    e = 0 
    for h in range (3):
        index = numeroQueSeSumaParaCambiarColumna * h
        for k in range(3):
            for j in range (3):
                for i in range(3):
                    nums.append(sudoku[index+i])
                index += numeroQueSumaCambiarFila
            e += errors(nums)
            #print(nums)
            nums = []
    return e

        

def errors(lista):
     errors = 0
     unicos = list(set(lista))
     if len(unicos) != 9:
            errors += 1
     return errors
    

def checkSudoku(sudoku):
    return (checkColumns(sudoku) + checkRows(sudoku) + checkSubSudoku(sudoku))

def quitarNumeros(sudoku):
    base = []
    for i in sudoku:
        if i == 0:
            base.append(i)
    return base

def nuevoIndividuo(base):
    nuevo = copy.copy(base)
    for i in range(len(nuevo)):
        nuevo[i] = random.randint(1,9)
    return nuevo

def ponerNumeros(individuo, sudoku):
    ind = copy.copy(individuo)
    s = copy.copy(sudoku)

    for i in range(len(s)):
        if s[i] == 0:
            s[i] = ind[0]
            ind.pop(0)
    return s


def elitismo(poblacion, aptitudes):
    p = copy.copy(poblacion)
    a = copy.copy(aptitudes)
    m = []
    for i in range(10):



def cruza(poblacion, aptitudes):
    nuevaGen = []



generaciones = 0
indexMA = -1
base = quitarNumeros(copy.copy(sudoku))
#print(base)
#print(sudoku)

poblacion = []
aptitudes =[]

for i in range(100):
    poblacion.append(nuevoIndividuo(base))

while generaciones < 100:

    #generando sudokus con la nueva generacion
    sudokus = []
    for individuo in poblacion:
        sudokus.append(ponerNumeros(individuo,sudoku))

    #calculando la aptitud de la nueva generacion
    aptitudes= []
    for su in sudokus:
        aptitudes.append(checkSudoku(su))
    
    #verificando si hay aptitud = 0
    indexMA = 0
    for i in range(len(aptitudes)):

        if aptitudes[i] < aptitudes[indexMA]:
            indexMA  = i
    
    if aptitudes[indexMA] == 0:
        break

    if generaciones%10 == 0:
        print("Generacion: " + str(generaciones)+":")
        print("Mejor aptitud: " + str(aptitudes[indexMA]))

    
    

    generaciones +=1
