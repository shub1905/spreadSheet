import numpy
import sys
import os


class GraphNode(object):

    def __init__(self):
        self.key = ''
        self.val = []  # post fix Stack
        self.child = []  # depency nodes
        self.color = 0  # 0: unvisited, 1: gray, 2: black


def cellname(row, column):
    # convert '35, 27'

    columnName = ''
    while(column > 0):
        columnName = chr(column % 26 + ord('A')) + columnName
        column = column // 26 - 1

    if column == 0:
        columnName = 'A' + columnName

    key = columnName + str(row + 1)
    return key


def key2val(var):
    # sample var = AB36

    column, row = 0, 0
    for i, char in enumerate(var):
        if char <= 'Z' and char >= 'A':
            column = column * 26 + (ord(char) - ord('A') + 1)
        else:
            row = int(var[i:])
            break
    return [row - 1, column - 1]


def maths(operation, params):
    if operation == '+':
        return sum(params)
    elif operation == '-':
        return (params[0] - params[1])
    elif operation == '*':
        return (params[0] * params[1])
    elif operation == '/':
        return (params[0] / params[1])
    else:
        raise Exception('Operation not defined')


def generatekeys(Graph):
    keys = Graph.keys()
    keys = map(lambda x: key2val(x), keys)
    keys.sort()

    for k in keys:
        yield k


def test():
    assert(cellname(35, 27) == 'AB36')
    assert(cellname(0, 0) == 'A1')
    assert(cellname(8, 3) == 'D9')

    assert(key2val('AB36') == [35, 27])
    assert(key2val('A1') == [0, 0])
    assert(key2val('D9') == [8, 3])
