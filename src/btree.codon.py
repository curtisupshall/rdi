class TreeNode[T]:
    key: int
    value: T
    left: Optional[TreeNode[T]] = None
    right: Optional[TreeNode[T]] = None

    def __init__(self, key: int, value: T):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'{self.key} => {self.value}'
    
    def child(self, key, value):
        if key < self.key:
            if self.left is None:
                self.left = TreeNode[T](key, value)
            else:
                self.left.child(key, value)
        else:
            if self.right is None:
                self.right = TreeNode[T](key, value)
            else:
                self.right.child(key, value)
    
    def find(self, key):
        if self.key == key:
            return self.value
        elif key < self.key and self.left is not None:
            return self.left.find(key)
        elif self.right is not None:
            return self.right.find(key)
        
        return None

    def serialize(self) -> str:
        left = self.left.serialize() if self.left else 'null'
        right = self.right.serialize() if self.right else 'null'

        return f'[{self.key}, {json.dumps(self.value)}, {left}, {right}]'

    @staticmethod
    def deserialize(body):
        return
    
class BTree[T]:
    root: Optional[TreeNode[T]] = None

    def __init__(self):
        self.root = None

    def __repr__(self):
        return None if self.root is None else self.root.serialize()
    
    def insert(self, key: int, value: T):
        if self.root is None:
            self.root = TreeNode(key, value)
        else:
            self.root.child(key, value)

    def search(self, key):
        return None if self.root is None else self.root.find(key)

    
# node = TreeNode[str](10, 'hello')
# node.child(2, 'world')

# print(node.serialize())

tree = BTree[List[int]]()

tree.insert(5, [5, 6])
tree.insert(3, [3, 4])
tree.insert(2, [2, 3])
tree.insert(9, [9, 10])
tree.insert(8, [8, 9])

print(tree)

print(tree.search(2))