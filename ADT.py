class Node:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


def huffmanTree(a: list):
    # 认为每一个字符都是节点,如果不是,那就让它是
    if type(a[0]) != Node:
        a = [Node(data=i) for i in a]

    b = Node()
    a.sort(key=lambda x: x.data, reverse=True)
    while len(a) > 1:
        b.lchild = a.pop()
        b.rchild = a.pop()
        b.data = b.lchild.data + b.rchild.data
        a.append(b)
        a.sort(key=lambda x: x.data, reverse=True)

    return a[0]