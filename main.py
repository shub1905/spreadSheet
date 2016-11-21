from utils import *

operations = ['+', '-', '*', '/']


def readfile(filename):
    '''
    return spreadSheet: 2D array from spreadsheet
    '''
    spreadsheet = []
    for line in open(filename):
        row = line.strip().split(',')
        spreadsheet.append(row)
    return spreadsheet


def outputfile(Graph, spreadsheet, filename):
    fd = open(filename, 'w')
    bufferstring = []

    for i, row in enumerate(spreadsheet):
        for j, cell in enumerate(spreadsheet[i]):
            if spreadsheet[i][j] == '':
                bufferstring.append('')
            else:
                key = cellname(i, j)
                nodeVal = Graph[key].val[0]

                if nodeVal == int(nodeVal):
                    bufferstring.append(str(int(nodeVal)))
                else:
                    bufferstring.append(str(float(nodeVal)))

        line = ','.join(bufferstring)
        fd.write(line + '\n')
        bufferstring = []
    fd.close()


def generateGraph(spreadsheet):
    Graph = {}

    for i, row in enumerate(spreadsheet):
        for j, cell in enumerate(spreadsheet[i]):
            if cell != '':
                temp = GraphNode()

                # reversed to treat it as a stack
                temp.val = cell.split(' ')[::-1]
                key = cellname(i, j)
                temp.key = key
                Graph[key] = temp

    return linkGraph(Graph)


def linkGraph(Graph):
    # link nodes
    for key in Graph:
        cell = Graph[key]
        postfix = cell.val
        for i, var in enumerate(postfix):
            if var in Graph:
                cell.child.append(Graph[var])
            elif var[0] <= 'Z' and var[0] >= 'A':
                raise Exception("Improper Reference: Node doesn't exists")
            elif var not in operations:
                try:
                    postfix[i] = float(postfix[i])
                except ValueError:
                    raise Exception('Bad argument')

    return Graph


def evaluateSheet(node, Graph):
    if node.color == 2:
        return
    if node.color == 1:
        raise Exception('Circular Reference')

    node.color = 1
    for child in node.child:
        evaluateSheet(child, Graph)

    node.color = 2
    evaluateCell(node, Graph)


def evaluateCell(node, Graph):
    postfix = node.val
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
        raise Exception('Wrong Expression')

    node.val.extend(params)


def main(infile='input.txt', outfile='output.txt'):
    spreadsheet = readfile(infile)

    try:
        Graph = generateGraph(spreadsheet)
    except Exception as exp:
        print 'Errors Found\n{}'.format(exp.args[0])
        return

    # tradeoff: better to hash instead of matrix if sheet is sparse
    for key in Graph:
        try:
            evaluateSheet(Graph[key], Graph)
        except Exception as exp:
            print 'Errors Found\n{}'.format(exp.args[0])
            return

    outputfile(Graph, spreadsheet, outfile)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '''
        Usage: python main.py InputFile OutputFile
        '''
    else:
        main(sys.argv[1], sys.argv[2])
