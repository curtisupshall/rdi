from bio import *
from sys import *

class Node[T]:
    key: int
    value: T
    left: Node[T]
    right: Node[T]

    def __init__(self, key: int, value: T):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree[T]:
    root: Node[T]

    def __init__(self):
        self.root = None

    def add(self, key: int, value: T):
        if self.root is None:
            self.root = Node[T](key, value)
        else:
            self._add_recursive(self.root, key, value)

    def _add_recursive(self, node: Node[T], key: int, value: T):
        if key < node.key:
            if node.left is None:
                node.left = Node[T](key, value)
            else:
                self._add_recursive(node.left, key, value)
        else:
            if node.right is None:
                node.right = Node[T](key, value)
            else:
                self._add_recursive(node.right, key, value)

    def search(self, key: int) -> T:
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node: Node[T], key: int) -> T:
        if node is None:
            return None
        if key == node.key:
            return node.value
        if key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def height(self) -> int:
        return self._height_recursive(self.root)

    def _height_recursive(self, node: Node[T]) -> int:
        if node is None:
            return 0
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

# Example usage
def main():
    bst = BinarySearchTree[int]()
    bst.add(5, "A")
    bst.add(3, "B")
    bst.add(7, "C")
    print("Height:", bst.height())
    print("Search 5:", bst.search(5))
    print("Search 3:", bst.search(3))

if __name__ == "__main__":
    main()
