#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <graphviz/gvc.h>

void visualize_graph(int** adj_matrix, int num_nodes) {
    GVC_t* gvc;
    Agraph_t* G;
    FILE* fp;

    // Create a new graph
    gvc = gvContext();
    G = agopen("G", Agdirected, 0);

    // Add nodes to the graph
    for (int i = 0; i < num_nodes; i++) {
        std::ostringstream node_name;
        node_name << i + 1;
        agnode(G, const_cast<char*>(node_name.str().c_str()));
    }

    // Add edges to the graph
    for (int i = 0; i < num_nodes; i++) {
        for (int j = 0; j < num_nodes; j++) {
            int weight = adj_matrix[i][j];
            if (weight != 0 && weight != INT_MAX) {
                std::ostringstream edge_label;
                edge_label << weight;

                std::ostringstream src_node_name, dst_node_name;
                src_node_name << i + 1;
                dst_node_name << j + 1;

                agedge(G, agnode(G, const_cast<char*>(src_node_name.str().c_str())),
                       agnode(G, const_cast<char*>(dst_node_name.str().c_str())),
                       const_cast<char*>(edge_label.str().c_str()), 1);
            }
        }
    }

    // Render the graph to a file in DOT format
    fp = fopen("graph.dot", "w");
    agwrite(G, fp);
    fclose(fp);

    // Render the graph using Graphviz's dot layout engine and display it
    std::string dot_command = "dot -Tpng graph.dot -o graph.png";
    system(dot_command.c_str());

    gvFreeLayout(gvc, G);
    agclose(G);
    gvFreeContext(gvc);
}

int main() {
    int num_nodes = 5; // Replace this with the number of nodes in your graph

    // Replace this with your adjacency matrix
    int** adj_matrix = new int*[num_nodes];
    for (int i = 0; i < num_nodes; i++) {
        adj_matrix[i] = new int[num_nodes];
        for (int j = 0; j < num_nodes; j++) {
            adj_matrix[i][j] = INT_MAX; // Initialize with infinity
        }
    }

    // Call the function to visualize the graph
    visualize_graph(adj_matrix, num_nodes);

    // Free the memory
    for (int i = 0; i < num_nodes; i++) {
        delete[] adj_matrix[i];
    }
    delete[] adj_matrix;

    return 0;
}
