from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testBasicMeshCoordinates(self):
        length = 1
        width = 1
        thickness = 1
        Nl = 2
        Nw = 2
        Nt = 2
        testMesh = Mesh(length, width, thickness, Nl, Nw, Nt)
        testMesh.createBMesh()

if __name__ == '__main__':
    unittest.main()