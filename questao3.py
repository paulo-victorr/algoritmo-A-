from questao1 import a_star_search, reconstruct_path
from questao2 import graph_romenia, heuristica_bucareste

if __name__ == "__main__":
    # Timisoara -> Bucareste
    came_from, cost_so_far = a_star_search(graph_romenia, 'Timisoara', 'Bucareste', heuristica_bucareste)
    path = reconstruct_path(came_from, 'Timisoara', 'Bucareste')
    print("Timisoara -> Bucareste:", path, "Custo:", cost_so_far['Bucareste'])

    # Oradea -> Bucareste
    came_from, cost_so_far = a_star_search(graph_romenia, 'Oradea', 'Bucareste', heuristica_bucareste)
    path = reconstruct_path(came_from, 'Oradea', 'Bucareste')
    print("Oradea -> Bucareste:", path, "Custo:", cost_so_far['Bucareste'])
