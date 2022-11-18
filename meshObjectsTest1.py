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
        Nw = 4
        Nt = 3
        name = "Find_Fibers"
        testMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        testMesh.generateMesh()
        testMesh.findFibers()

if __name__ == '__main__':
    unittest.main()
