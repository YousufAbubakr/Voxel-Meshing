import matplotlib.pyplot as plt
import numpy as np

# Defines Node, Element, and Mesh classes for voxel mesh generation

class Node:

    # Initializing instance of a node:
    def __init__(self, x, y, z):
        # Instance Variables:
        self.x = x
        self.y = y
        self.z = z

class Element:

    # Initializing instance of an element:
    def __init__(self, nodes):
        # Instance Variables:
        self.nodes = nodes

class Mesh:

    # Initializing instance of a mesh:
    def __init__(self, elements):
        # Instance Variables:
        self.elements = elements
