import heapq

# Grade com custos (cada número é o custo de entrar na célula)
grid_costs = [
    [1, 1, 2, 5, 5, 5],
    [1, 3, 2, 5, 9, 5],
    [1, 1, 1, 2, 5, 5],
    [6, 7, 1, 1, 1, 2],
    [5, 5, 4, 3, 2, 1],
    [9, 6, 5, 2, 1, 1]
]

n_rows = len(grid_costs)
n_cols = len(grid_costs[0])

start = (0, 0)   # canto superior esquerdo
goal = (5, 5)   # canto inferior direito

# Heurística admissível: distância Manhattan * menor custo de célula
min_cost = min(min(row) for row in grid_costs)

def in_bounds(pos):
    r, c = pos
    return 0 <= r < n_rows and 0 <= c < n_cols

def neighbors(pos):
    r, c = pos
    for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
        nr, nc = r+dr, c+dc
        if in_bounds((nr,nc)):
            yield (nr,nc)

def heuristic(a, b):
    return (abs(a[0]-b[0]) + abs(a[1]-b[1])) * min_cost

def a_star_grid(start, goal):
    frontier = []
    heapq.heappush(frontier, (heuristic(start, goal), start))
    came_from = {start: None}
    cost_so_far = {start: grid_costs[start[0]][start[1]]}

    while frontier:
        _, current = heapq.heappop(frontier)
        if current == goal:
            break
        for nb in neighbors(current):
            nb_cost = grid_costs[nb[0]][nb[1]]
            new_cost = cost_so_far[current] + nb_cost
            if nb not in cost_so_far or new_cost < cost_so_far[nb]:
                cost_so_far[nb] = new_cost
                priority = new_cost + heuristic(nb, goal)
                heapq.heappush(frontier, (priority, nb))
                came_from[nb] = current
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    if goal not in came_from:
        return None
    path = []
    current = goal
    while current:
        path.append(current)
        current = came_from[current]
    path.reverse()
    return path

if __name__ == "__main__":
    came_from, cost_so_far = a_star_grid(start, goal)
    path = reconstruct_path(came_from, start, goal)

    print("Grid (custos):")
    for row in grid_costs:
        print(row)

    print("\nCaminho encontrado:", path)
    print("Custo total:", cost_so_far[goal])

    # Visualização do caminho
    vis = [["." for _ in range(n_cols)] for _ in range(n_rows)]
    if path:
        for (r, c) in path:
            vis[r][c] = "X"
    vis[start[0]][start[1]] = "S"
    vis[goal[0]][goal[1]] = "G"

    print("\nGrid com caminho (S=Start, G=Goal, X=Caminho):")
    for r in range(n_rows):
        row_str = " ".join(f"{vis[r][c]}({grid_costs[r][c]})" for c in range(n_cols))
        print(row_str)
