from collections import deque


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


a_node = Node(None, None, None)
b_node = Node(1, None, None)
c_node = Node(2, None, None)


def compare(a: Node, b: Node) -> bool:
    if a is None or b is None:
        return a is b
    return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)


print(compare(a_node, b_node))


class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check(p, q):
            # if both are None
            if not p and not q:
                return True
            # one of p and q is None
            if not q or not p:
                return False
            if p.val != q.val:
                return False
            return True

        deq = deque([(p, q),])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True

    def isSameTreeRecursion(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # p and q are both None
        if not p and not q:
            return True
        # one of p and q is None
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        return self.isSameTreeRecursion(p.right, q.right) and \
            self.isSameTreeRecursion(p.left, q.left)
