from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testFiberFinding(self):
        ''' Tests findFibers() method.
        '''
        length = 10
        width = 1
        thickness = 1
        Nl = 2
        Nw = 31
        Nt = 31
        name = "Find_Fibers_Base_Case"
        baseMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt, diam = 0.5, spac = width - 0.5, ang = 0)
        baseMesh.generateMesh()
        baseMesh.findFibers()
        baseMesh.plot3D()

if __name__ == '__main__':
    unittest.main()
