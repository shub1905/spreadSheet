import numpy


class GraphNode(object):

    def __init__(self):
        self.val = []  # post fix Stack
        self.child = []  # depency nodes
        self.color = 0  # 0: unvisited, 1: gray, 2: black


def cellname(row, column):
    # convert '35, 27'
    key = chr(ord('A') + column) + str(row + 1)
    return key


def key2val(var, spreadSheet):
    # sample var = AZ123
    column = ''
    for i, char in enumerate(var):
        if char <= 'Z' and char >= 'A':
            column += char
        else:
            row = int(var[i:])
            break
    column = ord(column) - ord('A')
    return spreadsheet[row, column]


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
