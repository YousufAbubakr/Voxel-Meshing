import matplotlib.pyplot as plt
import numpy as np

# Defines Node, Element, and Mesh classes for voxel mesh generation

class Node:

    lastID = 0

    # Initializing instance of a node:
    def __init__(self, x, y, z):
        # Instance Variables:
        self.x = x
        self.y = y
        self.z = z
        self.id = Node.lastID
        Node.lastID += 1

class Element:

    # Initializing instance of an element:
    def __init__(self, nodes, id):
        # Instance Variables:
        self.nodes = nodes
        self.id = id

class Mesh:
    ''' A "Mesh" instance is an object that describes and generates
    the meshing features and files characteristic of a voxel meshing
    scheme.

    Example 2D Voxel Mesh Case:
    
    1_ _ _ _2_ _ _ _5        Elements = [E1, E2, E3, E4]
    |       |       |        E1 Local Node IDs = [1, 2, 3, 4]
    |  E1   |  E2   |        E2 Local Node IDs = [2, 5, 4, 6]
    |3 _ _ 4|_ _ _ _|6       E3 Local Node IDs = [3, 4, 7, 8]
    |       |       |        E4 Local Node IDs = [4, 6, 8, 9]
    |  E3   |  E4   |        Global Node IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    |7 _ _ 8|_ _ _ _|9       Mesh = Elements
    
    Input Variables:
        l, w, t: length, width, and thickness of mesh, 
                 where (li, wi, ti) corresponds to an (x, y, z) coordinate system
        Nl, Nw, Nt: number of elements along the length, width, and thickness directions

    Attributes (static variables):
        l, w, t: length, width, and thickness of mesh
        Nl, Nw, Nt: number of elements along the length, width, and thickness directions
        lpos, wpos, tpos: linspace of discrete x, y, z positions given by l, w, t and Nl, Nw, Nt
    '''

    # Initializing instance of a mesh:
    def __init__(self, l, w, t, Nl, Nw, Nt):
        # Instance Variables:
        self.l = l
        self.w = w
        self.t = t
        self.Nl = Nl
        self.Nw = Nw
        self.Nt = Nt
        self.lpos = np.linspace(0, self.l, self.Nl)
        self.wpos = np.linspace(0, self.w, self.Nw)
        self.tpos = np.linspace(0, self.t, self.Nt)

        print(f"L values: \n {self.lpos}")
        print(f"W values: \n {self.wpos}")
        print(f"T values: \n {self.tpos}")
    
    def createBMesh(self):
        for l in self.lpos:
            for w in self.wpos:
                for t in self.tpos:
                    node = Node(l, w, t)
                    print("Node ID: ", node.id)
                    print("Node coords: ", [node.x, node.y, node.z])
