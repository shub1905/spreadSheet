import numpy
import sys
import os


class GraphNode(object):
    '''
        Class for cell in spreadsheet
    '''

    def __init__(self):
        self.key = ''
        self.val = []  # post fix Stack
        self.child = []  # depency nodes
        self.color = 0  # 0: unvisited, 1: gray, 2: black


def cellName(row, column):
    '''
        Convert row,column to Spread Sheet Key
        eg: (35, 27) : AB36
    '''

    columnName = ''
    while(column > 0):
        columnName = chr(column % 26 + ord('A')) + columnName
        column = column // 26 - 1

    if column == 0:
        columnName = 'A' + columnName

    key = columnName + str(row + 1)
    return key


def keyVal(var):
    '''
        Convert Spread Sheet Key to row,column
        eg: AB36: (35, 27)
    '''
    column, row = 0, 0
    for i, char in enumerate(var):
        if char <= 'Z' and char >= 'A':
            column = column * 26 + (ord(char) - ord('A') + 1)
        else:
            row = int(var[i:])
            break
    return [row - 1, column - 1]


def mathOperation(operation, params):
    '''
        perform operation on constants
    '''
    ans = 0
    b = params.pop()
    a = params.pop()

    if operation == '+':
        ans = a+b
    elif operation == '-':
        ans = a-b
    elif operation == '*':
        ans = a*b
    elif operation == '/':
        if b == 0:
            raise Exception('Division by Zero')
        ans = a*1./b
    else:
        raise Exception('Operation not defined')

    params.append(ans)
    return params


def test():
    # sample testing
    assert(cellName(35, 27) == 'AB36')
    assert(cellName(0, 0) == 'A1')
    assert(cellName(8, 3) == 'D9')

    assert(keyVal('AB36') == [35, 27])
    assert(keyVal('A1') == [0, 0])
    assert(keyVal('D9') == [8, 3])
