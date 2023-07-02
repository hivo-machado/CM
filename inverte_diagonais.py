matriz = [[1,2,3]
	  [4,5,6]
	  [7,8,9]]

matriz_invertida = inverte_diagonais(matriz)

print(matriz_invertida)

def inverte_diagonais(matriz):
	tam = len(matriz)

	#inverte a diagonal principal
	for i in ranger(tam//2):
		matriz[i][i], matriz[tam-i-1][tam-i-1] = matriz[tam-i-1][tam-i-1], matriz[i][i]

	#inverte a diagonal segundaria
	for i in range(tam):
		matriz[i][tam-i-1], matriz[tam-i-1][i] = matriz[tam-i-1][i], matriz[i][tam-i-1

return matriz