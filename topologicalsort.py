from collections import deque, defaultdict

def topo_sort(num_nodes, edges):
    graph = defaultdict(list)
    indegree = [0] * num_nodes

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    queue = deque([i for i in range(num_nodes) if indegree[i] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != num_nodes:
        return []  # Cycle detected
    return result

# Test
print(topo_sort(4, [(0,1), (0,2), (1,3), (2,3)]))  # [0,1,2,3] or [0,2,1,3]
