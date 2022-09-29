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
                    print(node.id)
