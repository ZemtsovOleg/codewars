class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, *args) -> None:
        self.root = None
        for val in args:
            self.insert(val)

    def insert(self, val) -> None:
        if self.root is None:
            self.root = Node(val)
        else:
            self.__insert_recursive(self.root, val)

    def __insert_recursive(self, node: Node, val) -> None:
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                self.__insert_recursive(node.left, val)
        if val > node.val:
            if node.right is None:
                node.right = Node(val)
            else:
                self.__insert_recursive(node.right, val)


one = BinaryTree(10, 5, 6, 13, 16, 11, 2, 3, 12)
two = BinaryTree(1, 5, 6, 13, 16, 9, 2, 3, 12)


def search(n: int, node: BinaryTree) -> bool:
    if not node:
        return False
    if n == node.val:
        return True
    if n < node.val:
        return search(n, node.left)
    if n > node.val:
        return search(n, node.right)


print(search(3, one.root))


def search(n: int, root: BinaryTree) -> bool:
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            if node.val == n:
                return True
            if n < node.val:
                queue.append(node.left)
            if n > node.val:
                queue.append(node.right)

    return False


print(search(16, one.root))


# def search(n: int, node: BinaryTree) -> bool:
#     try:
#         print(node.val)
#     except:
#         print('here None')
#     if not node:
#         return False
#     if node.val == n:
#         return True
#     return search(n, node.left) or search(n, node.right)


# print(search(17, one.root))
