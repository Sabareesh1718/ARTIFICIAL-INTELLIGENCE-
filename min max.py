def minimax(depth, node_index, is_maximizing, values, max_depth):
    # Base case: if we're at a leaf node
    if depth == max_depth:
        return values[node_index]

    if is_maximizing:
        return max(
            minimax(depth + 1, node_index * 2, False, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, values, max_depth)
        )

# Leaf node values (game end scores)
values = [3, 5, 2, 9, 12, 5, 23, 23]
max_depth = 3  # log2(8) = 3

# Start Minimax
best_score = minimax(0, 0, True, values, max_depth)
print("Best value for the maximizer:", best_score)
