from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testFiberFinding(self):
        ''' Tests findFibers() method.
        '''
        length = 10
        width = 10
        thickness = 0.2
        Nl = 2
        Nw = 20
        Nt = 20
        name = "Find_Fibers"
        testMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        testMesh.generateMesh()
        testMesh.findFibers()
        testMesh.plot3D()
        writeFibers = True
        writeMatrix = True
        testMesh.writeMesh(writeFibers, writeMatrix)

if __name__ == '__main__':
    unittest.main()
