class BTreeNode[T]:
    _value: T
    _left: Optional[object] = None
    _right: Optional[object] = None

    def __init__(self) -> None:
        pass

    def __repr__(self):
        return self._value
    
    def addChild(self, node: object):
        if value < self._value:
            if self._left is None:
                self._left = node

class BTree[T]:
    _root: Optional[BTreeNode[T]] = None

    def __init__(self):
        # self._root = root
        return
    
    def root(self):
        return self._root
    
    def add(self, value: T):
        node = BTreeNode[T](value)

        if self._root is None:
            self._root = node

    def toJson():
        return
    
    def fromJson():
        return

        

tree = BTree[str]()
tree.add('hello')

print(tree.root())