from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testBasicMeshCoordinates(self):
        length = 10
        width = 10
        thickness = 10
        Nl = 10
        Nw = 10
        Nt = 10
        testMesh = Mesh(length, width, thickness, Nl, Nw, Nt)
        testMesh.createBMesh()

if __name__ == '__main__':
    unittest.main()