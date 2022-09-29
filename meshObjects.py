import matplotlib.pyplot as plt
import numpy as np

# Defines Node, Element, and Mesh classes for voxel mesh generation

class Node:

    # Initializing instance of a node:
    def __init__(self, x, y, z, id):
        # Instance Variables:
        self.x = x
        self.y = y
        self.z = z
        self.id = id

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
    
    def createBMesh(self):
        lcoords, wcoords, tcoords = np.meshgrid(self.lpos, self.wpos, self.tpos, indexing = 'ij')
        for l in lcoords:
            for w in wcoords:
                for t in tcoords:
                    print("coordinate: ", str([l, w, t]))
