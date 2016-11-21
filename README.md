# FB Interview spreadSheet
### Author: Shubham Bansal

The submitted solution uses a Hash Map to maintain the Adjacency List representation of spread sheet. The Mapping is from CellName to GraphNode. Each GraphNode contains the list of nodes that it's depends on. This method perform better in case the sheet is sparse. This is because we won't have to iterate over empty cells while evaluating.

We read the spread sheet as a csv from the specified input file if it exists. Then we create a dependency Graph as specified above by reading the contents of a Cell. During the Graph Creation we check for proper cell referencing and bad arguments if present in the Cell.

This is followed by a traversal of Graph in a Depth First fashion. We evaluate all the depending cells first and then try to evaluate current Cell. We check for Circular references or Wrong Expressions while evaluating the Cell.