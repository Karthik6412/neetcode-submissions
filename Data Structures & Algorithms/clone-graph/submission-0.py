"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clones = {}

        def clone(node):
            if node is None:
                return None
            if node in clones:
                return  clones[node]
            copy = Node(node.val) # create an object called copy so it accomadate value and neighbors
            clones[node] = copy
            for neighbor in node.neighbors:
                neighbor_clone = clone(neighbor)
                copy.neighbors.append(neighbor_clone)
            
            return copy



        return clone(node)
            




