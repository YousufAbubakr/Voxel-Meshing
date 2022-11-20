from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testFiberFinding(self):
        ''' Tests findFibers() method.
        '''
        length = 10
        width = 2
        thickness = 2
        Nl = 2
        Nw = 21
        Nt = 21
        name = "Find_Fibers_Base_Case"
        baseMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt, diam = 0.5, spac = 0.5, ang = 0)
        baseMesh.generateMesh()
        baseMesh.findFibers()
        baseMesh.plot3D()

if __name__ == '__main__':
    unittest.main()
