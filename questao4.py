from questao1 import a_star_search, reconstruct_path
from questao2 import graph_romenia

"""
    Heurística baseada em coordenadas aproximadas:
    Craiova: (44.32, 23.82)
    Outras cidades calculadas com distância Euclidiana × fator de escala
"""
heuristica_craiova = {
 'Arad': 284, 'Zerind': 311, 'Oradea': 338, 'Sibiu': 166, 'Timisoara': 258,
 'Lugoj': 213, 'Mehadia': 131, 'Drobeta': 97, 'Craiova': 0, 'Rimnicu Vilcea': 98,
 'Fagaras': 193, 'Pitesti': 103, 'Bucareste': 183, 'Giurgiu': 180, 'Urziceni': 229,
 'Hirsova': 332, 'Eforie': 386, 'Vaslui': 400, 'Iasi': 432, 'Neamt': 350
}

if __name__ == "__main__":
    came_from, cost_so_far = a_star_search(graph_romenia, 'Arad', 'Craiova', heuristica_craiova)
    path = reconstruct_path(came_from, 'Arad', 'Craiova')
    print("Caminho encontrado:", path)
    print("Custo total:", cost_so_far['Craiova'])
