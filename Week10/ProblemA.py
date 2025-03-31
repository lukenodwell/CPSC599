from heapq import heappop, heappush

class Graph:
        def __init__(self, num_nodes, adjacency_matrix):
                self.num_nodes = num_nodes
                self.adjacency_matrix = adjacency_matrix

        def mst(self, max_cost):
                return 'yes' if self._prims_algorithm(max_cost) else 'no'

        def _prims_algorithm(self, max_cost):

                min_edge_cost = [0] * self.num_nodes
                unvisited_nodes = set(range(1, self.num_nodes))
                visited = [True] + [False] * (self.num_nodes - 1)
                priority_queue = []
                edge_count, total_cost = 0, 0

                for i in range(1, self.num_nodes):
                        heappush(priority_queue, (self.adjacency_matrix[0][i], i))
                        min_edge_cost[i] = self.adjacency_matrix[0][i]

                while edge_count < self.num_nodes - 1:
                        while True:
                                weight, node = heappop(priority_queue)
                                if not visited[node]:
                                        break

                        edge_count += 1
                        total_cost += weight

                        if total_cost + self.num_nodes > max_cost:
                                return False

                        visited[node] = True
                        unvisited_nodes.remove(node)

                        for neighbor in unvisited_nodes:
                                if self.adjacency_matrix[node][neighbor] < min_edge_cost[neighbor]:
                                        min_edge_cost[neighbor] = self.adjacency_matrix[node][neighbor]
                                        heappush(priority_queue, (self.adjacency_matrix[node][neighbor], neighbor))

                return self.num_nodes + total_cost <= max_cost


def read_adjacency_matrix(num_nodes, adjacency_matrix):
    for _ in range((num_nodes * (num_nodes - 1)) // 2):
        u, v, weight = map(int, input().split())
        adjacency_matrix[u][v] = weight
        adjacency_matrix[v][u] = weight


def test_case(max_cost, num_nodes):
    adjacency_matrix = [[0] * num_nodes for _ in range(num_nodes)]
    read_adjacency_matrix(num_nodes, adjacency_matrix)

    if max_cost < num_nodes:
        print('no')
    else:
        graph = Graph(num_nodes, adjacency_matrix)
        print(graph.mst(max_cost))


num_test_cases = int(input())
for _ in range(num_test_cases):
        max_cost, num_nodes = map(int, input().split())
        test_case(max_cost, num_nodes)
