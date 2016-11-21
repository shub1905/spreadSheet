from utils import *

operations = ['+', '-', '*', '/']


def readFile(filename):
    '''
        Generate spreadSheet: 2D array from spreadsheet
    '''
    if not os.path.exists(filename):
        raise Exception("Input File Doesn't Exists")
    spreadsheet = []
    for line in open(filename):
        row = line.strip().split(',')
        spreadsheet.append(row)
    return spreadsheet


def outputSheet(Graph, spreadsheet, filename):
    '''
        Write computed spreadsheet to file
    '''
    fd = open(filename, 'w')
    bufferstring = []

    for i, row in enumerate(spreadsheet):
        for j, cell in enumerate(spreadsheet[i]):
            if spreadsheet[i][j] == '':
                bufferstring.append('')
            else:
                key = cellName(i, j)
                nodeval = Graph[key].val[0]

                if nodeval == int(nodeval):
                    bufferstring.append(str(int(nodeval)))
                else:
                    bufferstring.append(str(float(nodeval)))

        line = ','.join(bufferstring)
        fd.write(line + '\n')
        bufferstring = []
    fd.close()


def generateGraph(spreadsheet):
    '''
        Create Graph Nodes mapped by on Cellname
    '''
    Graph = {}

    for i, row in enumerate(spreadsheet):
        for j, cell in enumerate(spreadsheet[i]):
            if cell != '':
                temp = GraphNode()

                # reversed to treat it as a stack
                temp.val = cell.split(' ')[::-1]
                key = cellName(i, j)
                temp.key = key
                Graph[key] = temp

    return linkGraph(Graph)


def linkGraph(Graph):
    '''
        Add dependency graph Node in child list
    '''
    for key in Graph:
        cell = Graph[key]
        postfix = cell.val

        for i, var in enumerate(postfix):
            if var in Graph:
                cell.child.append(Graph[var])

            elif var[0] <= 'Z' and var[0] >= 'A':
                error = ("Improper Reference\n\t"
                         "Cell {}: {} doesn't exists or has empty Value").format(cell.key, var)
                raise Exception(error)

            elif var not in operations:
                try:
                    postfix[i] = float(postfix[i])
                except ValueError:
                    error = 'Bad argument\n\t{} in Cell {}'.format(var, cell.key)
                    raise Exception(error)

    return Graph


def evaluateSheet(node, Graph):
    if node.color == 2:
        return

    node.color = 1
    for child in node.child:
        if child.color == 1:
            error = 'Circular Reference between {} and {}'.format(node.key, child.key)
            raise Exception(error)

        evaluateSheet(child, Graph)

    node.color = 2
    evaluateCell(node, Graph)


def evaluateCell(node, Graph):
    postfix = node.val
    params = []
    while(len(postfix) > 0):
        var = postfix.pop()
        if var in operations:
            ans = mathOperation(var, params)
            postfix.append(ans)
            params = []
        elif var in Graph:
            params.extend(Graph[var].val)
        else:
            params.extend([var])

    if len(params) != 1:
        raise Exception('Wrong Expression in Cell {}'.format(node.key))

    node.val.extend(params)


def main(infile, outfile):
    try:
        spreadsheet = readFile(infile)
        Graph = generateGraph(spreadsheet)

        for key in Graph:
            evaluateSheet(Graph[key], Graph)

    except Exception as exp:
        print 'Errors Found\n\t{}'.format(exp.args[0])
        return

    outputSheet(Graph, spreadsheet, outfile)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print '''
        Usage: python main.py InputFile OutputFile
        '''
    else:
        main(sys.argv[1], sys.argv[2])
