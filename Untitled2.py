import heapq
from collections import deque

def bfs_and_a_star(start, goal, adj_list, heuristic):
    g = {start: 0}  
    f = {start: heuristic[start]}  
    open_set = []
    heapq.heappush(open_set, (f[start], start)) 

    visited = set()

    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            print("Da tim thay duong di!")
            return g[current]  

        visited.add(current)
        for neighbor in adj_list[current]:
            if neighbor not in visited:
                tentative_g = g[current] + 1  
                if neighbor not in g or tentative_g < g[neighbor]:
                    g[neighbor] = tentative_g
                    f[neighbor] = g[neighbor] + heuristic[neighbor] 
                    heapq.heappush(open_set, (f[neighbor], neighbor))

    print("Khong tim thay duong di .")
    return -1 

adj_list = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 4],
    3: [1, 5],
    4: [1, 2, 5],
    5: [3, 4]
}
heuristic = {
    0: 6,
    1: 5,
    2: 4,
    3: 3,
    4: 2,
    5: 1
}
start = 0
goal = 5
result = bfs_and_a_star(start, goal, adj_list, heuristic)
print(chi phi tu batdau den dich , result)
