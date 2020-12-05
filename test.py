from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader

class Node:
    def __init__(self, data=None, lchild=None, rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild

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

def huffmanCode(a: Node, Code: dict, CodeIng: list):
    if a.lchild is None and a.rchild is None:
        Code[a.data] = str(CodeIng)
    if a.lchild:
        CodeIng.append('0')
        huffmanCode(a.lchild, Code, CodeIng)
    if a.rchild:
        CodeIng.append('1')
        huffmanCode(a.rchild, Code, CodeIng)
    if len(CodeIng):
        CodeIng.pop()

def printCode(code: dict):
    for i in range(1, len(code) + 1):
        print(f"{chr(i + 64)}  的赫夫曼编码是  {code[i][2:-2:5]}")

def WordToCode(word: str, code: dict):
    lista, str1 = [], ''
    for ch in word:
        lista.append(eval(code[ord(ch) - 64]))
    for i in range(len(lista)):
        for j in lista[i]:
            str1 += j
    return str1

def CodeToWord(word: str, code: dict):
    wcode, Num, str2 = list(word), [], ''
    while len(wcode):
        for ch in code:
            if str(wcode[:4]) == code[ch]:
                Num.append(chr(ch + 64))
                del wcode[:4]
            elif str(wcode[:5]) == code[ch]:
                Num.append(chr(ch + 64))
                del wcode[:5]
            elif str(wcode[:6]) == code[ch]:
                Num.append(chr(ch + 64))
                del wcode[:6]
            elif str(wcode[:7]) == code[ch]:
                Num.append(chr(ch + 64))
                del wcode[:7]
            elif str(wcode[:8]) == code[ch]:
                Num.append(chr(ch + 64))
                del wcode[:8]
    for i in range(len(Num)):
        str2 += Num[i]
    return str2

class Huffman:
    def __init__(self):
        self.window = QUiLoader().load('Huffman.ui')
        self.window.pushButton.clicked.connect(self.encode)
        self.window.pushButton_2.clicked.connect(self.decode)

    def encode(self):
        try:
            word1 = str(self.window.plainTextEdit.toPlainText())
            Begin = [i for i in range(1, 28)]
            Code, CodeIng, Word= {}, [], []
            Tree = huffmanTree(Begin)
            huffmanCode(Tree, Code, CodeIng)
            stra = WordToCode(word1, Code)
            self.window.textBrowser.setText(str(stra))
        except:
            QMessageBox.about(self.window, 'ERROR', f''' 错误的输入数据 ''')

    def decode(self):
        try:
            word2 = str(self.window.plainTextEdit_2.toPlainText())
            Begin = [i for i in range(1, 28)]
            Code, CodeIng, Word = {}, [], []
            Tree = huffmanTree(Begin)
            huffmanCode(Tree, Code, CodeIng)
            strb = CodeToWord(word2, Code)
            self.window.textBrowser.setText(str(strb))
        except:
            QMessageBox.about(self.window, 'ERROR', f''' 错误的输入数据 ''')

app = QApplication([])
huffman = Huffman()
huffman.window.show()
app.exec_()
