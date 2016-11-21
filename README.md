# FB Interview spreadSheet
### Author: Shubham Bansal

The submitted solution uses a Hash Map to maintain the Adjacency List representation of spread sheet. The Mapping is from CellName to GraphNode. Each GraphNode contains the list of nodes that it depends on. Hashmap is the choosen representation for the sheet over a matrix as this representation will perform better in case the sheet is sparse. It's because we won't have to iterate over empty cells while evaluating.

We read the spread sheet as a csv from the specified input file if it exists. Then we create a dependency Graph as specified above by reading the contents of a Cell. During the Graph Creation we check for proper cell referencing and bad arguments if present in the Cell.

This is followed by a traversal of Graph in a Depth First fashion. We evaluate all the depending cells first and then try to evaluate current Cell. We check for Circular references while evaluating the children and check for correctness of expressions while evaluating the Cell.

This solution is recommended as it presents most optimal way to resolve dependencies and detect circular references, i.e., using Depth First Search. Also the current implementation allows for extending operators by augmenting *mathOperation* function and allowed *operations* list.

### Complexity
#### Time Complexity: O(V+E)
We'll take O(V) to read the sheet, create a Graph and output the solved sheet. The evaluation takes O(V' + E) time.
#### Space Complexity: O(V+E)
The auxillary space used by generated Graph and spreadsheet matrix is O(V+E).

where,  
V'= Number of non-empty Cells  
V = Number of Cells  
E = Total number of inter-cell References
