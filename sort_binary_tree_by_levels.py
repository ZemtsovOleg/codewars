class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


def tree_by_levels(tree):
    queue = [tree]
    values = []

    while queue:
        node = queue.pop(0)
        if node:
            queue += [node.left, node.right]
            values.append(node.value)

    return values


print(tree_by_levels(Node(Node(None, Node(None, None, 4), 2), Node(
    Node(None, None, 5), Node(None, None, 6), 3), 1)), [1, 2, 3, 4, 5, 6])



# def serpentine_traversal(node: Node, result=None) -> list:
#     if result is None:
#         result = []
#     if node is None:
#         return
#     serpentine_traversal(node.left, result)
#     result.append(node.value)
#     serpentine_traversal(node.right, result)
#     return result
