matriz_A = [[1,2,3,4]
	    [5,6,7,8]
	    [9,10,11,12]
	    [13,14,15,16]]

matriz_B = [[2,3]
	    [6,7]]

ocorrencias = contar_submatriz(matriz_A, matriz_B)

print("Numero de ocorrencias: ", ocorrencias)

def contar_submatriz(matriz_A, submatriz_B):
    count = 0
    rows_A = len(matriz_A)
    cols_A = len(matriz_A[0])
    rows_B = len(submatriz_B)
    cols_B = len(submatriz_B[0])
    
    for i in range(rows_A - rows_B + 1):
        for j in range(cols_A - cols_B + 1):
            if matriz_A[i:i+rows_B] == submatriz_B:
                count += 1
    
return count