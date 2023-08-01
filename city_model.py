import random
import networkx as nx
import matplotlib.pyplot as plt
# visualizer
def visualize_graph(adj_matrix):
    G = nx.DiGraph()

    num_nodes = len(adj_matrix)

    G.add_nodes_from(range(1, num_nodes+1))

    for i in range(num_nodes):
        for j in range(num_nodes):
            weight = adj_matrix[i][j]
            if weight != 0 and weight != float('inf'):
                G.add_edge(i+1, j+1, weight=weight)

    pos = nx.spring_layout(G, seed=42)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=10, font_color='red')

    plt.show()


def generate_random_adj_matrix(n, edge_probability=0.3):
    adj_matrix = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                adj_matrix[i][j] = 0
            elif random.random() < edge_probability:
                weight = random.randint(2, 10)
                adj_matrix[i][j] = weight

    return adj_matrix


def traffic(adj_matrix, traffic_intensity):
    n = len(adj_matrix)
    for i in range(n):
        for j in range(n):
            if not i == j and not adj_matrix[i][j] == float('inf'):
                adj_matrix[i][j] *= (100+traffic_intensity)/100
                adj_matrix[i][j] = int(adj_matrix[i][j])
    return adj_matrix


def dijkstra(adj_matrix, source):
    n = len(adj_matrix)
    distances = [float('inf')] * n
    distances[source] = 0

    previous_node = [-1] * n
    previous_node[source] = source

    visited = [False] * n

    for _ in range(n):
        min_distance = float('inf')
        min_node = -1
        for node in range(n):
            if not visited[node] and distances[node] < min_distance:
                min_distance = distances[node]
                min_node = node

        if min_node == -1:
            break

        visited[min_node] = True

        for neighbor in range(n):
            if adj_matrix[min_node][neighbor] != float('inf') and not visited[neighbor]:
                distance_to_neighbor = min_distance + \
                    adj_matrix[min_node][neighbor]
                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor
                    previous_node[neighbor] = min_node
    return distances, previous_node


def find_shortest_path(previous_node, target, start):
    stack = []
    current_node = target
    while not previous_node[current_node] == -1 and not current_node == start:
        stack.append(current_node)
        current_node = previous_node[current_node]
    stack.append(current_node)
    return stack[::-1]


def print_adj_matrix(adj_matrix):
    for row in adj_matrix:
        print(' '.join(str(val) if val != float('inf') else 'INF' for val in row))


if __name__ == "__main__":
    n = int(input("Enter the number of nodes in the city "))
    edge_probability = 0.5
    traffic_intensity = float(
        input("Enter the intensity of traffic in percentage"))
    # random.seed(42)
    q = int(input("Number of queries "))
    adj_matrix = generate_random_adj_matrix(n, edge_probability)
    # print_adj_matrix(adj_matrix)
    adj_matrix = traffic(adj_matrix, traffic_intensity)
    
    # print_adj_matrix(adj_matrix)
    while (q):
        start = int(input("Enter the starting node "))
        end = int(input("Enter the ending node "))
        ans, previous_nodes = dijkstra(adj_matrix, start-1)
        print(
            f"The shortest distance between {start} and {end} is: {ans[end-1]}")
        path = find_shortest_path(previous_nodes, end-1, start-1)
        for i, x in enumerate(path):
            if not i == len(path) - 1:
                print(f"{x+1} -> ", end="")
            else:
                print(x+1)
        q -= 1
    visualize_graph(adj_matrix)

