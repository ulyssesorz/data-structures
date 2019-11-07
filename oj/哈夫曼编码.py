class Node:
    def __init__(self, data):    #data是一个字典，键为字母，值为权值
        self.val = data[1]       #权值
        self.ch = data[0]        #字母
        self.code = ""           #编码
        self.left = None
        self.right = None

def getchar(str):               #获取字母的权值，并转化成需要的形式
    result = {}
    for i in str:               #使用字典去重统计权值
        if i in result:
            result[i] += 1
        else:
            result[i] = 1

    c=[]
    for i in result.items():
       c.append(i)                  #将字典转化为一个列表，键和值在一个集合中

    d=[[] for i in range(len(c))]
    j=0
    for i in c:                     #转变为大列表内含小列表的形式
        d[j].append(i[0])
        d[j].append(i[1])
        j+=1
    return d


def huffmantree(data):
    h=[Node(i) for i in data]
    while len(h)!=1:
        h.sort(key=lambda x:x.val)
        node=Node([None,h[0].val+h[1].val])     #合并的节点不带字母，只是权值相加
        node.left=h.pop(0)
        node.right=h.pop(0)
        h.append(node)
    return h[0]


codedic1 = {}
codedic2 = {}


def huffmancode(root, c):
    if root:
        huffmancode(root.left, c + '0')         #递归地给code赋值
        huffmancode(root.right, c + '1')
        root.code += c
        if root.ch:
            codedic1[root.ch] = root.code       #准备编码和解码的字典
            codedic2[root.code] = root.ch


def transencode(str):           #编码
    global codedic1
    result = ""
    for i in str:               #输出每个字母的编码
        result += codedic1[i]
    return result


def transdecode(strcode):
    global codedic2
    result = ""
    temp = ""
    for i in strcode:
        temp += i
        if temp in codedic2:            #找到对应的编码则输出字母（哈夫曼编码不必考虑重复）
            result += codedic2[temp]
            temp = ""
    return result


if __name__ == '__main__':
    str=input()
    tree=huffmantree(getchar(str))
    huffmancode(tree,"")
    print(transencode(str))
    print(transdecode(transencode(str)))

