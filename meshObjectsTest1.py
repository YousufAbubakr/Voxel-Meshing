from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testFiberFinding(self):
        ''' Tests findFibers() method.
        '''
        length = 11
        width = 6
        thickness = 0.2
        Nl = 6
        Nw = 20
        Nt = 20
        name = "Find_Fibers"
        testMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        testMesh.generateMesh()
        testMesh.findFibers()
        testMesh.plot3D()

if __name__ == '__main__':
    unittest.main()
