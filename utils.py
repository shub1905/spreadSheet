import numpy


class GraphNode(object):

    def __init__(self):
        self.key = ''
        self.val = []  # post fix Stack
        self.child = []  # depency nodes
        self.color = 0  # 0: unvisited, 1: gray, 2: black


def cellname(row, column):
    # convert '35, 27'
    if not column:
        columnName = 'A'
    else:
        columnName = ''
        while(column > 0):
            columnName += chr(column % 26 + ord('A'))
            column = column // 26

    key = columnName + str(row + 1)
    return key


def key2val(var):
    # sample var = AZ123
    column, row = 0, 0
    for i, char in enumerate(var):
        if char <= 'Z' and char >= 'A':
            column = column * 26 + (ord(char) - ord('A'))
        else:
            row = int(var[i:]) - 1
            break
    return [row, column]


def maths(operation, params):
    params = map(int, params)
    if operation == '+':
        return sum(params)
    elif operation == '-':
        return (params[0] - params[1])
    elif operation == '*':
        return (params[0] * params[1])
    elif operation == '/':
        return (params[0] / params[1])
    else:
        raise 'Operation not defined'


def generatekeys(Graph):
    keys2 = Graph.keys()
    keys = map(lambda x: key2val(x), keys2)
    keys.sort()

    for k in keys:
        yield k
