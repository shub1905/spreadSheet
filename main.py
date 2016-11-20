'''
Test Cases

1. Mis-constructed expression
2. circular recursion
3. improper Expression
'''

from utils import *


def readfile(filename='input.txt'):
    '''
    return spreadSheet: 2D array from spreadsheet
    '''
    spreadsheet = []
    # ToDO: check for validity of file
    for line in open(filename):
        row = line.strip().split(',')
        spreadsheet.append(row)
    return spreadsheet


def outputfile(Graph):
    # for key in generateKeys():
    for column in ['A', 'B', 'C']:
        for row in [1, 2, 3]:
            key = column + str(row)
            val = Graph.get(key, None)
            if val:
                print key, val.val


def generateGraph(spreadsheet):
    Graph = {}
    for i, row in enumerate(spreadsheet):
        for j, cell in enumerate(spreadsheet[i]):
            if cell != '':
                temp = GraphNode()

                # reversed to treat it as a stack
                temp.val = cell.split(' ')[::-1]
                key = cellname(i, j)
                Graph[key] = temp

    # link nodes
    for key in Graph:
        cell = Graph[key]
        postfix = cell.val
        for var in postfix:
            if var in Graph:
                cell.child.append(Graph[var])
            else:
                # Mis-constructed expression
                # expressions or actual number
                pass

    return Graph


def evaluateSheet(node, Graph):
    if not node:
        raise 'improper reference'

    if node.color == 2:
        # print node.val
        # return node.val[0]
        return
    if node.color == 1:
        raise 'Circular Recursion'

    node.color = 1
    for child in node.child:
        evaluateSheet(child, Graph)

    node.color = 2
    evaluateCell(node, Graph)


def evaluateCell(node, Graph):
    postfix = node.val
    operations = ['+', '-', '*', '/']

    params = []
    while(len(postfix) > 0):
        var = postfix.pop()
        if var in operations:
            ans = maths(var, params)
            postfix.append(ans)
            params = []
        elif var in Graph:
            params.extend(Graph[var].val)
        else:
            params.extend([var])

    if len(params) != 1:
        raise 'wrong evaluation'

    node.val = params


def main():
    spreadsheet = readfile()
    Graph = generateGraph(spreadsheet)

    # tradeoff: better to hash instead of matrix if sheet is sparse
    for key in Graph:
        evaluateSheet(Graph[key], Graph)
        print '.',

    outputfile(Graph)


main()
