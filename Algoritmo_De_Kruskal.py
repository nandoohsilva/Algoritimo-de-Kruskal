import heapq

# Matriz de entrada
matriz = [
    [9, 14],
    [0, 1, 4],
    [0, 7, 8],
    [1, 2, 8],
    [1, 7, 11],
    [2, 3, 7],
    [2, 5, 4],
    [2, 8, 2],
    [3, 4, 9],
    [3, 5, 14],
    [4, 5, 10],
    [5, 6, 2],
    [6, 7, 1],
    [6, 8, 6],
    [7, 8, 7]
]

# Extraindo o número de vértices e arestas da matriz
Nv_vertices, Na_arestas = matriz[0]



H = []

# Preenchendo o heap H com os dados das arestas da matriz
for i in range(1, Na_arestas+1):
    Primeiro_Extremo_Aresta, Segundo_Extremo_Aresta, Custo_Da_Aresta = matriz[i]
    heapq.heappush(H, (Custo_Da_Aresta, Primeiro_Extremo_Aresta, Segundo_Extremo_Aresta))

n = Nv_vertices
C = [[] * n for i in range(n)]  # Criar N conjuntos

for i in range(n):
    C[i].append(i)  # Cada C[i] é inicializado com [i]

S = []
for i in range(n):
    S.append(i) # S é o conjunto ao qual o vértice 'i' pertence

cont = 0 # vai ser um contador de arestas
custo = 0 # o custo da árvore geradora começa com 0 
arestas_selecionadas = [] # para guardar as arestas selecionadas

#print(S)
#print(C)  

while cont < n-1: # bastam n-1 arestas
    Custo_Da_Aresta, Primeiro_Extremo_Aresta, Segundo_Extremo_Aresta = heapq.heappop(H) # Remover a próxima aresta do heap
    if S[Primeiro_Extremo_Aresta] != S[Segundo_Extremo_Aresta ]: # se as arestas unem árvores diferentes
        custo = custo+Custo_Da_Aresta
        arestas_selecionadas.append((Primeiro_Extremo_Aresta, Segundo_Extremo_Aresta, Custo_Da_Aresta))
        p = S[Primeiro_Extremo_Aresta]
        q = S[Segundo_Extremo_Aresta]
        if q < p:
            p, q = q, p
        for j in C[q]: # para cada j no conjunto(q)
            S[j] = p
            C[p].extend(C[q]) # unir C[p] e C[q a união fica em C[p]]
            C[q] = [] # esvaziar C[q]
        cont = cont+1
#print(S)
#print(C)            
#print (f"O custo da última aresta adcionada é:", Custo_Da_Aresta)

# Imprimir as arestas selecionadas e seus custos
for aresta in arestas_selecionadas:
    print(f"Vertice {aresta[0]}, Vertice {aresta[1]}, Custo {aresta[2]}")


print (f"Custo total das arestas", custo)


# Entrada de dados, vertices e arestas
# V A C
# 9 14
# 0 1 4
# 0 7 8
# 1 2 8
# 1 7 11
# 2 3 7
# 2 5 4
# 2 8 2
# 3 4 9
# 3 5 14
# 4 5 10
# 5 6 2
# 6 7 1
# 6 8 6
# 7 8 7 
# Árvore geradora de custo 37