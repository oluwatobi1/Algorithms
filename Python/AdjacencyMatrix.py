
data = {"A":{"B": 2,"D":4}, "B": {"C": 1}, "C": {"A": 3, "D": 1}, "D": {"B": 1}}


def sparsify(data):
    """
    Function named sparsify that takes in an adjacency dictionary and returns the corresponding sparse matrix as a list of lists.
Example: sparsify({"A":{"B: 2,"D":4}, "B": {"C": 1}, "C": {"A": 3, "D": 1}, "D": {"B": 1}}) 
returns
[[0, 0, 3, 0], [2, 0, 0, 1], [0, 1, 0, 0], [4, 0, 1, 0]]
    """
    
    return [[data[str(j)].get(str(i), 0) for j in data.keys()] for i in data.keys()]



print(sparsify (data))

"""
Adjacency - Matrix
An adjacency dictionary is a collection of key & value pairs where the keys refer to the nodes in a graph and the values are dictionaries containing the outgoing edges as keys and weight as values.
For example if we have: adj_dict= {"A": {"B":1}, "B":{"C":2}, "C":{"A":1,"D":1}, "D":{}}
This means that the node "A" points to the node "B" with a weight of 1, node "B" to the node "C" with a weight of 2, node "C" to the nodes "A" and "D" with weights of 1 and 1 and node "D" to nothing.
A sparse matrix is one that contains a majority of zero entries. For this purpose it shall be a list of lists where each sub list is a row. The row and column indices represent all nodes in alphabetical order. The column is the start node and the row is where it points to. An element in the matrix will have a corresponding to the weight if the column index maps to its row index from the adjacency dictionary. Thus the above dictionary transforms to :
   A B  C D
[ [0, 0, 1, 0], A
[1, 0, 0, 0],   B
[0, 2, 0, 0],   C
[0, 0, 1, 0] ]  D

Armed with this knowledge, write a function named sparsify that takes in an adjacency dictionary and returns the corresponding sparse matrix as a list of lists.
Example: sparsify({"A":{"B: 2,"D":4}, "B": {"C": 1}, "C": {"A": 3, "D": 1}, "D": {"B": 1}}) returns
[[0, 0, 3, 0], [2, 0, 0, 1], [0, 1, 0, 0], [4, 0, 1, 0]]
N.B:
• Weights are strictly integers and nodes are uppercase letters.
•No inbuilt module should be used
•Raise only AssertionErrors.
"""

