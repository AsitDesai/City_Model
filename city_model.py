import random

def generate_random_adj_matrix(n, edge_probability=0.3):
    adj_matrix = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                adj_matrix[i][j] = 0
            elif random.random() < edge_probability:
                weight = random.randint(5, 10)
                adj_matrix[i][j] = weight

    return adj_matrix

def print_adj_matrix(adj_matrix):
    for row in adj_matrix:
        print(' '.join(str(val) if val != float('inf') else 'INF' for val in row))

if __name__ == "__main__":
    n = 5
    edge_probability = 0.4  

    random.seed(42) 

    adj_matrix = generate_random_adj_matrix(n, edge_probability)

    print("Random Adjacency Matrix:")
    print_adj_matrix(adj_matrix)
