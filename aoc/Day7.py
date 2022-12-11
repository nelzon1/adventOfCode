from pathlib import Path
import re

fileSizeRE = re.compile('^\\d+')
dskTotal = 70000000
freeTotal = 30000000
target = 10822529
'''
Classes: Tree, Node
read in instructions
    each line parse to cmd or node
    reader should know current node
    if its a ls cmd, we do nothing
    if its a cd we go to that node in the current node's children or up if a ..
    if its a dir list, we add that node
    if its a file, we add that
    
'''

class Tree:
    # head
    # nodes
    def __init__(self, head=None, nodes=[]):
        self.head = head
        self.nodes = nodes,
        self.current = head

    def setHead(self, node):
        self.head = node
        self.current = node

    def setCurrent(self,node):
        self.current = node

class Node:
    # parent
    # type
    # size
    # children

    def __init__(self, name='', parent=None, type='file', size=0):
        self.parent = parent
        self.type = type
        self.size = size
        self.children = {}
        self.name = name

    def getSize(self):
        fullSize = self.size
        for childKey in self.children:
            fullSize += self.children[childKey].getSize()
        self.size = fullSize
        return self.size

    def addChild(self, node):
        self.children[node.name] = node

    def countSub100kDirectories(self):
        totalSize = self.size
        for childKey in self.children:
            totalSize += self.children[childKey].countSub100kDirectories() \
                        if self.children[childKey].size <= 100000 and self.children[childKey].type == 'dir' else 0
        return totalSize

def cnt100K(node, curSum):

    for childKey in node.children:
        curSum += cnt100K(node.children[childKey], 0)

    return node.size + curSum if node.size <= 100000 and node.type == 'dir' else 0

def count100000Directores(tree):
    queue = [tree.head]
    totalSize = 0
    while len(queue) > 0:
        currentNode = queue.pop(0)
        #add children to queue
        [queue.append(x) for x in currentNode.children.values()]
        #chck dir and size
        totalSize += currentNode.size if currentNode.size <= 100000 and currentNode.type == 'dir' else 0
    return totalSize

def findDirToDelete(tree):
    queue = [tree.head]
    currentSize = 0
    diff = 10**10
    while len(queue) > 0:
        currentNode = queue.pop(0)
        #add children to queue
        [queue.append(x) for x in currentNode.children.values()]
        #chck dir and size
        if currentNode.size - target < diff and currentNode.size - target >= 0 and currentNode.type == 'dir':
            diff = currentNode.size - target
            currentSize = currentNode.size
    return currentSize

def parseCmd(strIn, tree):
    if len(strIn) < 2:
        raise Exception('bad input')
    if strIn[0] == '$':
        #cmd
        if strIn[2] == 'l':
            #ls - do nothing
            return
        else:
            #cd
            if strIn[5:7] == '..':
                #go to parent
                tree.setCurrent(tree.current.parent)
            else:
                newDirName = strIn[5:].strip()
                tree.setCurrent(tree.current.children[newDirName])

    elif strIn[0] == 'd':
        #dir
        newDirName = strIn[4:].strip()
        tree.current.addChild(Node(name=newDirName,type='dir', parent=tree.current))

    else:
        #file
        fileSize = int(re.findall(fileSizeRE, strIn)[0])
        newFileName = strIn[strIn.index(' ')+1:].strip()
        tree.current.addChild(Node(name=newFileName, type='file', size=fileSize, parent=tree.current))

if __name__ == '__main__':
    print('Running AOC Day 7')
    filename = Path.joinpath(Path.cwd(), 'input/Day7.txt')

    tree = Tree()
    tree.setHead(Node(name='/', type='dir'))
    cmdList = ''
    with open(filename, 'r') as file:
        cmdList = file.readlines()
    lineCnt = 1
    for cmd in cmdList:
        parseCmd(cmd,tree)
        lineCnt+=1
    #Part 1
    tree.head.getSize()
    print('Done parsing cmds')
    print('Directories with less than 100k stored: ',count100000Directores(tree) )

    #Part 2
    print('Total tree size: ', tree.head.size)
    print('Amt to free up: ', dskTotal - tree.head.size - freeTotal)
    print('Smallest directory to satisfy target: ', findDirToDelete(tree))