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

    
node = TreeNode[str](10, 'hello')
node.child(2, 'world')

print(node)