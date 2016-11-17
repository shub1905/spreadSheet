import numpy

class GraphNode(object):
	def __init__(self):
		self.val =  [] #post fix Stack
		self.child = [] #depency nodes

def key2val(column, row, spreadSheet):
	column = ord(column) - ord('A')
	return spreadsheet[row, column]

def readfile(filename = 'input.txt'):
	'''
	return spreadSheet: numpy.array from spreadsheet
	'''
	spreadsheet = None
	# ToDO: check for validity of file
	for line in open(filename):
		row = line.strip().split(',')
		if spreadsheet == None:
			spreadsheet = numpy.zeros((0,len(row)))

		spreadsheet = numpy.vstack((spreadsheet, row))
	return spreadsheet


def outputfile(spreadsheet):
	pass

def generateGraph(spreadsheet):
	'''
	return set unvisited nodes of Graph
	'''
	unvisited = set()
	m,n = spreadsheet.shape
	for i,row in enumerate(spreadsheet):
		for j,cell in enumerate(spreadsheet[i]):
			temp = GraphNode()
			temp.val = cell.split(' ')
			spreadsheet[i][j] = temp
			unvisited.add(temp)

	return unvisited

def evaluateSheet(unvisited):
	if not unvisited:
		return

	root = unvisited.pop()

def main():
	spreadsheet = readfile()
	graph = generateGraph(spreadsheet)
	evaluateSheet(graph)

T = 1 # int(raw_input())
# for t in T:
main()