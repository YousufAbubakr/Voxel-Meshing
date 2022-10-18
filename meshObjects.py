import numpy as np
import matplotlib.pyplot as plt

# Defines Node, Element, and Mesh classes for voxel mesh generation

class Node:

    ''' A "Node" instance is a meshing object such that an overall
    mesh is discretized into a set of points in space. Each of these
    points are called nodes and are defined by their coordinate
    location (and in the FEM, they are also defined by their degrees
    of freedom).

    2 Node Example:
    
                     Node IDs = [1, 2]
    1_ _ _ _ 2       Node 1 Coordinate Location: (x1, y1, z1)
                     Node 2 Coordinate Location: (x2, y2, z2)
    '''

    # Global node IDs are defined on a rolling basis, which means 
    # that after given a starting node ID, every node has an ID 
    # which is 1 more than the previously defined node ID. The 
    # starting node ID is called lastID and is defined as:
    lastID = 0

    def __init__(self, x, y, z):
        ''' Initializing instance of a node given a set of (x, y, z)
        coordinates. Note that every time a node is initialized,
        Node.lastID (a Node class variable) is increased by 1.

        Initialization (input variables):
            x, y, z: (x, y, z) coordinate location of node

        Attributes (static variables):
            x, y, z: (x, y, z) coordinate location of node
            coord: (x, y, z) tuple of node coordinate
            id: global node ID
        '''
        # Instance Variables:
        self.x = x
        self.y = y
        self.z = z
        self.coord = (x, y, z)
        self.id = Node.lastID
        Node.lastID += 1

class Element:
    ''' An "Element" instance is a meshing object such that an overall
    mesh is spactially partitioned into an array of unit cells. Each of
    these cells are an element, and in this voxel meshing scheme, are
    uniquely described by a set of local node IDs. 

    Example 2D Voxel Mesh Case:
    
    1_ _ _ _ 2      Elements = [E1]
    |       |       E1 Local Node IDs = [1, 2, 3, 4]
    |   E1  |       Global Node IDs = [1, 2, 3, 4] 
    |3 _ _ _|4
    '''

    # Similar to global node IDs, element IDs are defined on a 
    # rolling basis. The starting element ID is called lastID and
    # is defined as:
    lastID = 0

    def __init__(self, nodes):
        ''' Initializing instance of a element given a set of nodes. 
        Note that every time an element is initialized, Element.lastID 
        (an Element class variable) is increased by 1.

        Initialization (input variables):
            nodes: set of local node IDs that uniquely describe an element

        Attributes (static variables):
            nodes: set of local node IDs that uniquely decribe an element
                ** Note: Local node IDs [N1, N2, ..., N8] are only defined 
                in the context of element objects **
            centroid: (xc, yc, zc) coordinate of centroid of element
            id: element ID
        '''
        # Instance Variables:
        self.nodes = nodes
        self.id = Element.lastID
        Element.lastID += 1

class Mesh:
    ''' A "Mesh" instance is a meshing object that describes and generates
    the meshing features and files characteristic of a voxel meshing scheme.

    Example 2D Voxel Mesh Case:
    
    1_ _ _ _2_ _ _ _3        Elements = [E1, E2, E3, E4]
    |       |       |        E1 Local Node IDs = [1, 2, 4, 5]
    |  E1   |  E2   |        E2 Local Node IDs = [2, 3, 5, 6]
    |4 _ _ 5|_ _ _ _|6       E3 Local Node IDs = [4, 5, 7, 8]
    |       |       |        E4 Local Node IDs = [5, 6, 8, 9]
    |  E3   |  E4   |        Global Node IDs = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    |7 _ _ 8|_ _ _ _|9       Mesh = Elements
    '''

    def __init__(self, l, w, t, Nl, Nw, Nt):
        ''' Initializing instance of a mesh given a set of geometry and 
        meshing parameters. 
        
        Note that Nl, Nw, and Nt in application 
        correspond to the number of linearly spaced coordinates, so add
        1 to Nl, Nw, and Nt to appropriately define the number of elements
        along the l, w, and t directions.

        Initialization (input variables):
            l, w, t: length, width, and thickness of mesh, 
                     where (li, wi, ti) corresponds to an (x, y, z) coordinate system
            Nl, Nw, Nt: number of elements along the length, width, and thickness directions

        Attributes (static variables):
            l, w, t: length, width, and thickness of mesh
            Nl, Nw, Nt: number of elements along the length, width, and thickness directions
            lpos, wpos, tpos: linspace of discrete x, y, z positions given by l, w, t and Nl, Nw, Nt
            globalNodes: set of all global node objects
            elements: set of all element objects
        '''
        # Resetting node IDs for new mesh:
        Node.lastID = 0

        # Instance Variables:
        assert l > 0 and w > 0 and t > 0, "Geometries must be positive!"
        assert Nl > 1 and Nw > 1 and Nt > 1, "Number of elements must be greater than 0!"
        self.l = l
        self.w = w
        self.t = t
        self.Nl = Nl
        self.Nw = Nw
        self.Nt = Nt
        self.globalNodes = []
        self.elements = []
        # Linearly spaced unit coordinates are defined such that there
        # are N(l, w, t) - where N(l, w, t) corresponds to either Nl, 
        # Nw, or Nt - coordinate nodes along the given direction, and 
        # hence N(l, w, t) - 1 elements along the given direction as 
        # well.
        self.lpos = np.linspace(0, l, Nl)
        self.wpos = np.linspace(0, w, Nw)
        self.tpos = np.linspace(0, t, Nt)

        print(f"X Coordinates: {self.lpos}")
        print(f"Y Coordinates: {self.wpos}")
        print(f"Z Coordinates: {self.tpos}")
    
    def getNodes(self):
        ''' Returns the nodes defined within the current context of the mesh.
        '''
        if len(self.globalNodes) == 0:
            print("Nodes have not been generated yet!")
            return None
        return self.globalNodes

    def getNodeX(self):
        ''' Returns an array of the nodes' x-coordinates nodes defined within 
            the current context of the mesh.
        '''
        if len(self.globalNodes) == 0:
            print("Nodes have not been generated yet!")
            return None
        dim = self.getNumberofNodes()
        nodes = self.getNodes()
        xcoords = np.empty([dim, 1])
        i = 0
        for node in nodes:
            xcoords[i] = node.x
            i += 1
        return xcoords

    def getNodeY(self):
        ''' Returns an array of the nodes' y-coordinates nodes defined within 
            the current context of the mesh.
        '''
        if len(self.globalNodes) == 0:
            print("Nodes have not been generated yet!")
            return None
        dim = self.getNumberofNodes()
        nodes = self.getNodes()
        ycoords = np.empty([dim, 1])
        i = 0
        for node in nodes:
            ycoords[i] = node.y
            i += 1
        return ycoords

    def getNodeZ(self):
        ''' Returns an array of the nodes' z-coordinates nodes defined within 
            the current context of the mesh.
        '''
        if len(self.globalNodes) == 0:
            print("Nodes have not been generated yet!")
            return None
        dim = self.getNumberofNodes()
        nodes = self.getNodes()
        zcoords = np.empty([dim, 1])
        i = 0
        for node in nodes:
            zcoords[i] = node.z
            i += 1
        return zcoords

    def getElements(self):
        ''' Returns the elements defined within the current context of the mesh.
        '''
        if len(self.elements) == 0:
            print("Elements have not been generated yet!")
            return None
        return self.elements

    def getNumberofNodes(self):
        ''' Returns the number of nodes defined within the current context of the mesh.
        '''
        if len(self.globalNodes) == 0:
            print("Nodes have not been generated yet!")
            return None
        return len(self.globalNodes)

    def getNumberofElements(self):
        ''' Returns the number of elements defined within the current context of the mesh.
        '''
        if len(self.elements) == 0:
            print("Elements have not been generated yet!")
            return None
        return len(self.elements)

    def plot3D(self):
        ''' Plots array of nodes
        '''

    def genNodes(self):
        ''' Generates array of nodes in O(Nl * Nw * Nt) time.
        '''
        nodeCount = 0
        nodeThres = 8
        nodeIDThres = nodeThres - 1
        for l in self.lpos:
            for w in self.wpos:
                for t in self.tpos:
                    # Creating a node object with the (l, w, t) coordinates
                    node = Node(l, w, t)
                    # Appending newly constructed node to global node list in mesh object
                    self.globalNodes.append(node)
                    print("Node ID: ", node.id)
                    print("Node coords: ", [node.x, node.y, node.z])
                    if node.id > 0 and node.id % nodeIDThres == 0:
                        # If you've generated 8 nodes, get the last 8 nodes,
                        # create an element, and reset the counter 
                        elementNodes = self.globalNodes[-nodeThres:]
                        element = Element(elementNodes)
                        # Appending newly constructed element to element list in mesh object
                        self.elements.append(element)
                        nodeCount = 0
                    nodeCount += 1
