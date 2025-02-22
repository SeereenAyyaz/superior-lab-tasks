import math

def minmax(depth, node_index, is_maximizing, values, alpha, beta):
    if depth == 0 or node_index >= len(values):
        return values[node_index]
    
    if is_maximizing:
        best = -math.inf
        for i in range(2):
            val = minmax(depth - 1, node_index * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if beta <= alpha:
                break
        return best
    else:
        best = math.inf
        for i in range(2):
            val = minmax(depth - 1, node_index * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if beta <= alpha:
                break
        return best

values = [3, 5, 6, 9, 1, 2, 0, -1] 
depth = math.log2(len(values))
optimal_value = minmax(int(depth), 0, True, values, -math.inf, math.inf)
print(f"Optimal value using Min-Max Algorithm: {optimal_value}")
