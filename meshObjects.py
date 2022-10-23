import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

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

    def __eq__(self, other):
        ''' Equality method that determines whether two nodes are equivalent
            based on their coordinates
        '''
        return all([self.x == other.x, self.y == other.y, self.z == other.z])

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
            nodes: set of globally defined local node objects that uniquely describe an element

        Attributes (static variables):
            nodes: set of globally defined local node objects that uniquely describe an element
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

    def __init__(self, l, w, t, *args):
        ''' Initializing instance of a mesh given a set of geometry and 
        meshing parameters. 
        
        Note that Nl, Nw, and Nt in application 
        correspond to the number of linearly spaced coordinates, so add
        1 to Nl, Nw, and Nt to appropriately define the number of elements
        along the l, w, and t directions.

        Initialization (input variables):
            l, w, t: length, width, and thickness of mesh, 
                     where (li, wi, ti) corresponds to an (x, y, z) coordinate system
            *args: R - unit element edge length OR [Nl, Nw, Nt] - number of elements along
                     the length, width, and thickness directions
                     ** Note that the R parameter works best when your specimen geometry is cubic
                     because R must be smaller than the shortest of the length, width, and thickness **

        Attributes (static variables):
            l, w, t: length, width, and thickness of mesh
            R: unit element edge length
            Nl, Nw, Nt: number of elements along the length, width, and thickness directions
            lpos, wpos, tpos: linspace of discrete x, y, z positions given by l, w, t and Nl, Nw, Nt
            globalNodes: set of all global node objects
            elements: set of all element objects
        '''
        # Resetting node IDs for new mesh:
        Node.lastID = 0

        # Instance Variables:
        assert l > 0 and w > 0 and t > 0, "Geometries must be positive!"
        assert len(args) == 1 or len(args) == 3, "*args parameter must be of length 1 or length 3!"
        if len(args) == 1:
            self.R = args[0]
            assert self.R <= l and self.R <= w and self.R <= t, "Unit edge lengths must be smaller than specien geometry!"
            self.Nl = int(l//self.R + 1)
            self.Nw = int(w//self.R + 1)
            self.Nt = int(t//self.R + 1)
        elif len(args) == 3:
            self.R = None
            self.Nl = args[0]
            self.Nw = args[1]
            self.Nt = args[2]
        assert self.Nl > 1 and self.Nw > 1 and self.Nt > 1, "Number of elements must be greater than 0!"
        self.l = l
        self.w = w
        self.t = t
        self.globalNodes = []
        self.elements = []
        # Linearly spaced unit coordinates are defined such that there
        # are N(l, w, t) - where N(l, w, t) corresponds to either Nl, 
        # Nw, or Nt - coordinate nodes along the given direction, and 
        # hence N(l, w, t) - 1 elements along the given direction as 
        # well.
        self.lpos = np.linspace(0, l, self.Nl)
        self.wpos = np.linspace(0, w, self.Nw)
        self.tpos = np.linspace(0, t, self.Nt)

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
        xcoords = np.empty(dim)
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
        ycoords = np.empty(dim)
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
        zcoords = np.empty(dim)
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
        ''' Plots array of nodes in the form of a voxel mesh with matplotlib library functions
        '''
        # Initializing figure
        fig = plt.figure()
        # Syntax for 3-D projection
        ax = fig.gca(projection = '3d')
        ax.set_aspect('auto')
        # Plotting
        filled = np.ones((self.Nl - 1, self.Nw - 1, self.Nt - 1))
        x, y, z = np.indices(np.array(filled.shape) + 1)
        ax.voxels(x * self.l/(self.Nl - 1), 
                    y * self.w/(self.Nw - 1), 
                    z * self.t/(self.Nt - 1), 
                    filled, facecolors = '#1f77b430', edgecolors = 'gray')
        ax.set_title('Voxel Mesh Plot')
        ax.set_xlabel('X axis - Length')
        ax.set_ylabel('Y axis - Width')
        ax.set_zlabel('Z axis - Thickness')
        plt.show()

    def genNodes(self):
        ''' Generates array of nodes in O(Nl * Nw * Nt) time.
        '''
        cornerNodes = []
        for l in self.lpos[:-1]:
            for w in self.wpos[:-1]:
                for t in self.tpos[:-1]:
                    # Creating a node object with the (l, w, t) coordinates
                    node = Node(l, w, t)
                    # Appending newly constructed node to global node list in mesh object
                    cornerNodes.append(node)
                    self.globalNodes.append(node)
        delX = int(self.l/(self.Nl - 1))
        delY = int(self.w/(self.Nw - 1))
        delZ = int(self.t/(self.Nt - 1))
        for cornerNode in cornerNodes:
            X = cornerNode.x
            Y = cornerNode.y
            Z = cornerNode.z
            print("Bottom Corner Node Coord Part 2: ", [X, Y, Z])
            newNodes = [Node(X, Y, Z + delZ), 
                            Node(X, Y + delY, Z), 
                            Node(X, Y + delY, Z + delZ),
                            Node(X + delX, Y, Z),
                            Node(X + delX, Y, Z + delZ),
                            Node(X + delX, Y + delY, Z),
                            Node(X + delX, Y + delY, Z + delZ)]
            elementNodes = []
            for node in newNodes:
                if not self.nodeInMesh(node):
                    self.globalNodes.append(node)
                elementNodes.append(node)     
            element = Element(elementNodes)
            self.elements.append(element)

    def nodeInMesh(self, node):
        ''' Subroutine that determins whether the input node is already
            defined within the context of the mesh.
        '''
        for meshNode in self.globalNodes:
            if meshNode == node:
                return True
        return False

