class Grafo:
    # Definindo o método construtor (instanciando o objeto)
    def __init__(self):
        self.lista_adjacencia = {
            'Arad':             [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
            'Bucharest':        [('Urziceni', 85), ('Pitesti', 101), ('Giurgiu', 90), ('Fagaras', 211)],
            'Craiova':          [('Drobeta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
            'Drobeta':          [('Mehadia', 75), ('Craiova', 120)],
            'Eforie':           [('Hirsova', 86)],
            'Fagaras':          [('Sibiu', 99), ('Bucharest', 211)],
            'Giurgiu':          [('Bucharest', 90)],
            'Hirsova':          [('Urziceni', 98), ('Eforie', 86)],
            'Iasi':             [('Neamt', 87), ('Vaslui', 92)],
            'Lugoj':            [('Timisoara', 111), ('Mehadia', 70)],
            'Mehadia':          [('Lugoj', 70), ('Drobeta', 75)],
            'Neamt':            [('Iasi', 87)],
            'Oradea':           [('Zerind', 71), ('Sibiu', 151)],
            'Pitesti':          [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
            'Rimnicu Vilcea':   [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
            'Sibiu':            [('Arad', 140), ('Oradea', 151), ('Rimnicu Vilcea', 80), ('Fagaras', 99)],
            'Timisoara':        [('Arad', 118), ('Lugoj', 111)],
            'Urziceni':         [('Vaslui', 142), ('Bucharest', 85), ('Hirsova', 98)],
            'Vaslui':           [('Iasi', 92), ('Urziceni', 142)],
            'Zerind':           [('Arad', 75), ('Oradea', 71)]
        }

    # Definindo o método para obter os vizinhos de um vértice (método get)
    def getVizinhos(self, v):
        return self.lista_adjacencia[v]

    def heuristica(self, cidade, objetivo):
        # Dicionário com as coordenadas das cidades
        coordenadas = {
            'Arad':     (91, 492),  'Bucharest':    (400, 327), 'Craiova':         (253, 288),
            'Drobeta':  (165, 299), 'Eforie':       (562, 293), 'Fagaras':         (305, 449),
            'Giurgiu':  (375, 270), 'Hirsova':      (534, 350), 'Iasi':            (473, 506),
            'Lugoj':    (165, 379), 'Mehadia':      (168, 339), 'Neamt':           (406, 537),
            'Oradea':   (131, 571), 'Pitesti':      (320, 368), 'Rimnicu Vilcea':  (233, 410),
            'Sibiu':    (207, 457), 'Timisoara':    (94, 410),  'Urziceni':        (456, 350),
            'Vaslui':   (509, 444), 'Zerind':       (108, 531)
        }

    # Coordenadas da cidade atual e do objetivo
        cidade_coords = coordenadas[cidade]
        objetivo_coords = coordenadas[objetivo]
        # Heurística de distância de Manhattan
        h = abs(cidade_coords[0] - objetivo_coords[0]) + abs(cidade_coords[1] - objetivo_coords[1])
        return h

    def a_star_algorithm(self, start_node, stop_node):
        # Armazena os nós descobertos, mas ainda não visitados
        open_list = set([start_node])
        # Armazena os nós já visitados
        closed_list = set([])

        g = {} # Armazena o custo do caminho do nó inicial para o nó atual
        g[start_node] = 0 # O custo do caminho do nó inicial para ele mesmo é zero

        # Inicializa o dicionário com os demais nós com custo infinito

        pais = {} # Armazena o nó pai de cada nó
        pais[start_node] = start_node # O nó inicial não tem pai

        while len(open_list) > 0: # Enquanto a lista de nós abertos não estiver vazia
            n = None # Inicializa o nó atual como nulo

            for v in open_list: # Para cada nó na lista de nós abertos
                if n == None or g[v] + self.heuristica(v, stop_node) < g[n] + self.heuristica(n, stop_node):
                    n = v; # O nó atual é o nó com o menor custo de caminho
            
            # Se o nó atual for o nó objetivo
            if n == None:
                print('Caminho não encontrado!')
                return None
            
            # Se o nó atual for o nó objetivo inicialize a lista de reconstrução do caminho
            if n == stop_node:
                reconstruir_caminho = [] 

                # Enquanto o nó atual não for o nó inicial adicione o nó atual ao caminho
                while pais[n] != n:
                    reconstruir_caminho.append(n) 
                    n = pais[n]
                
                reconstruir_caminho.append(start_node)

                reconstruir_caminho.reverse()

                print('Caminho encontrado: {}'.format(reconstruir_caminho))
                return reconstruir_caminho
            
            # Para cada vizinho do nó atual 
            for (m, peso) in self.getVizinhos(n):
                # Se o vizinho não estiver na lista de nós abertos e nem na lista de nós fechados
                if m not in open_list and m not in closed_list: 
                    open_list.add(m) # Adicione o vizinho à lista de nós abertos
                    pais[m] = n # O pai do vizinho é o nó atual
                    g[m] = g[n] + peso # O custo do caminho do nó inicial até o vizinho é o custo do caminho do nó inicial até o nó atual mais o peso da aresta entre o nó atual e o vizinho

                else:
                    if g[m] > g[n] + peso:
                        g[m] = g[n] + peso
                        pais[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)
            
            # Remova o nó atual da lista de nós abertos e adicione-o à lista de nós fechados
            open_list.remove(n)
            closed_list.add(n)

        print('Caminho não encontrado!')
        return 
    
# Para executar o algoritmo
grafo = Grafo()
grafo.a_star_algorithm('Arad', 'Bucharest')