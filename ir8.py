
import numpy as np

def page_rank(graph, damping_factor=0.85, max_iterations=100, tolerance=1e-6):
    # Get the number of nodes
    num_nodes = len(graph)

    # Initialize PageRank values
    page_ranks = np.ones(num_nodes) / num_nodes

    # Iterative PageRank calculation
    for _ in range(max_iterations):
        prev_page_ranks = np.copy(page_ranks)

        for node in range(num_nodes):
            # Calculate the contribution from incoming links
            incoming_links = [i for i, v in enumerate(graph) if node in v]
            if not incoming_links:
                continue

            page_ranks[node] = (1 - damping_factor) / num_nodes + \
                               damping_factor * sum(prev_page_ranks[link] / len(graph[link]) for link in incoming_links)

        # Check for convergence
        if np.linalg.norm(page_ranks - prev_page_ranks, 2) < tolerance:
            break

    return page_ranks

# Example usage
if __name__ == "__main__":
    # Define a simple directed graph as an adjacency list
    # Each index represents a node, and the list at that index contains nodes to which it has outgoing links
    web_graph = [
        [1, 2],     # Node 0 has links to Node 1 and Node 2
        [0, 2],     # Node 1 has links to Node 0 and Node 2
        [0, 1],     # Node 2 has links to Node 0 and Node 1
        [1, 2],     # Node 3 has links to Node 1 and Node 2
    ]

    # Calculate PageRank
    result = page_rank(web_graph)

    # Display PageRank values
    for i, pr in enumerate(result):
        print(f"Page {i}: {pr}")
