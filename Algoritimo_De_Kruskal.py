import heapq

Nv_vertices, Na_arestas = input("Digite o número do vértice as arestas e peso de cada aresta: ").split() # Ler o numero de vertices, arestas e transformar em lista

Nv_vertices =int(Nv_vertices) # Convertendo para o tipo 'inteiro'
Na_arestas = int(Na_arestas) # Convertendo para o tipo 'inteiro'

H = []

for i in range(Na_arestas): # Ler o número de arestas do grafo
    Primeiro_Extremo_Aresta, Segundo_Extremo_Aresta, Custo_Da_Aresta = input().split() #ler arestra de A para B com custo C
    Primeiro_Extremo_Aresta = int(Primeiro_Extremo_Aresta)
    Segundo_Extremo_Aresta = int(Segundo_Extremo_Aresta)
    Custo_Da_Aresta = int(Custo_Da_Aresta)
    heapq.heappush(H, (Custo_Da_Aresta, Primeiro_Extremo_Aresta, Segundo_Extremo_Aresta)) #Coloca aresta no heap

n = Nv_vertices
C = [[] * n for i in range(n)] # Criar N conjuntos

for i in range(n):
    C[i].append(i)  # Cada C[i] é inicializado com [i]

S = []
for i in range(n):
    S.append(i) # S é o conjunto ao qual o vértice 'i' pertence

cont = 0 # vai ser um contador de arestas
custo = 0 # o custo da árvore geradora começa com 0 
#print(S)
#print(C)  

while cont < n-1: # bastam n-1 arestas
    Custo_Da_Aresta, Primeiro_Extremo_Aresta, Segundo_Extremo_Aresta = heapq.heappop(H) # Remover a próxima aresta do heap
    if S[Primeiro_Extremo_Aresta] != S[Segundo_Extremo_Aresta ]: # se as arestas unem árvores diferentes
        custo = custo+Custo_Da_Aresta
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