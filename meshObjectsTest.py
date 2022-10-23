from audioop import mul
from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testUnitMesh(self):
        ''' Tests unit mesh generation by defining a 1 x 1 x 1 unit
        size box that is defined by (Nl - 1)(Nw - 1)(Nt - 1) = 1 element.
        '''
        length = 1
        width = 1
        thickness = 1
        Nl = 2
        Nw = 2
        Nt = 2
        name = "unitMesh"
        assert Nl == 2 and Nw == 2 and Nt == 2, "Only want 1 element for this test!"
        unitMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        unitMesh.generateMesh()
        self.assertEqual(Nl * Nw * Nt, unitMesh.getNumberofNodes())
        self.assertEqual(1, unitMesh.getNumberofElements())
        self.assertTrue(([0, length] == unitMesh.lpos).all())
        self.assertTrue(([0, width] == unitMesh.wpos).all())
        self.assertTrue(([0, thickness] == unitMesh.tpos).all())

    def testGetters(self):
        ''' Tests getter functions with a unitMesh example.
        '''
        length = 1
        width = 1
        thickness = 1
        Nl = 2
        Nw = 2
        Nt = 2
        name = "getters"
        assert Nl == 2 and Nw == 2 and Nt == 2, "Only want 1 element for this test!"
        unitMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        unitMesh.generateMesh()
        self.assertEqual(Nl * Nw * Nt, unitMesh.getNumberofNodes())
        self.assertEqual(Nl * Nw * Nt, len(unitMesh.getNodeX()))
        self.assertEqual(Nl * Nw * Nt, len(unitMesh.getNodeY()))
        self.assertEqual(Nl * Nw * Nt, len(unitMesh.getNodeZ()))

    def testMultiElementMesh(self):
        ''' Tests multi-element mesh generation by defining a 2 x 2 x 2 unit
        size box that is defined by (Nl - 1)(Nw - 1)(Nt - 1) = 2 x 2 x 2 = 8 elements.
        '''
        length = 2
        width = 2
        thickness = 2
        Nl = 3
        Nw = 3
        Nt = 3
        name = "multiElement"
        assert Nl == 3 and Nw == 3 and Nt == 3, "Want 24 elements for this test!"
        multiMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        multiMesh.generateMesh()
        multiMesh.plot3D()
        print(multiMesh)
        self.assertEqual(Nl * Nw * Nt, multiMesh.getNumberofNodes())
        self.assertEqual((Nl - 1) * (Nw - 1)* (Nt - 1), multiMesh.getNumberofElements())

    def testUnitElementGeneration(self):
        ''' Tests unit element generation by using self.R parameter instead of
            Nl, Nw, and Nt parameters.
        '''
        length = 5
        width = 5
        thickness = 5
        R = 2
        name = "unit"
        testMesh = Mesh(length, width, thickness, name, R)
        testMesh.generateMesh()
        #testMesh.plot3D()

    def test3DPlotting(self):
        ''' Tests 3D plotting with a variety of geometric test variables.
        '''
        length = 11
        width = 6
        thickness = 0.2
        Nl = 6
        Nw = 4
        Nt = 3
        name = "plotting"
        testMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        testMesh.generateMesh()
        #testMesh.plot3D()

if __name__ == '__main__':
    unittest.main()