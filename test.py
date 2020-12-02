class Node:
    def __init__(self,data = None, lchild = None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

Begin = [i for i in range(1,28)]


def huffmanTree(a: list):
    # 认为每一个字符都是节点,如果不是,那就让它是
    if type(a[0]) != Node:
        a = [Node(data=i) for i in a]
    while len(a) > 1:
        b = Node(None, None, None)
        a.sort(key=lambda x: x.data, reverse=True)
        b.lchild = a.pop()
        b.rchild = a.pop()
        b.data = b.lchild.data + b.rchild.data
        a.append(b)
    return a[0]
Code = {}
CodeIng = []
def print_Tree(a:Node):
    print(a.data)
    if a.lchild is None and a.rchild is None:
        Code[a.data] = str(CodeIng)
    if a.lchild:
        CodeIng.append(0)
        print("L",end='  ')
        print_Tree(a.lchild)
    else :
        print("L  None")
    if a.rchild:
        CodeIng.append(1)
        print("R",end='  ')
        print_Tree(a.rchild)
    else :
        print("R  None")
    if len(CodeIng):
        CodeIng.pop()


Tree = huffmanTree(Begin)
print_Tree(Tree)
for i in range(1, len(Code)+1):
    print(f"{chr(i+64)}的赫夫曼编码是{Code[i]}")