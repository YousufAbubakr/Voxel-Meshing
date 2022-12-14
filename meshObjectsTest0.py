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
        name = "Unit _Cell_Mesh"
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
        name = "Testing_Getters"
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
        name = "Multi_Element_Mesh"
        assert Nl == 3 and Nw == 3 and Nt == 3, "Want 24 elements for this test!"
        multiMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        multiMesh.generateMesh()
        print(multiMesh)
        multiMesh.printNodes()
        multiMesh.printElements()
        multiMesh.plot3D()
        self.assertEqual(Nl * Nw * Nt, multiMesh.getNumberofNodes())
        self.assertEqual((Nl - 1) * (Nw - 1)* (Nt - 1), multiMesh.getNumberofElements())

    def testNonUniformMesh(self):
        ''' Tests multi-element mesh generation by defining a 6 x 8 x 2 unit
        size box that is defined by (Nl - 1)(Nw - 1)(Nt - 1) = 3 x 5 x 7 = 105 elements.
        '''
        length = 6
        width = 8
        thickness = 2
        Nl = 4
        Nw = 6
        Nt = 8
        name = "Nonuniform_Mesh"
        assert Nl == 4 and Nw == 6 and Nt == 8, "Want 105 elements for this test!"
        nonuniform = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        nonuniform.generateMesh()
        print(nonuniform)
        nonuniform.printNodes()
        nonuniform.printElements()
        nonuniform.plot3D()
        self.assertEqual(Nl * Nw * Nt, nonuniform.getNumberofNodes())
        self.assertEqual((Nl - 1) * (Nw - 1) * (Nt - 1), nonuniform.getNumberofElements())

    def testUnitElementGeneration(self):
        ''' Tests unit element generation by using self.R parameter instead of
            Nl, Nw, and Nt parameters.
        '''
        length = 15
        width = 15
        thickness = 15
        R = 5
        name = "R_Generated_Mesh"
        testMesh = Mesh(length, width, thickness, name, R)
        testMesh.generateMesh()
        print(testMesh)
        testMesh.printNodes()
        testMesh.printElements()
        testMesh.plot3D()

    def test3DPlotting(self):
        ''' Tests 3D plotting with a 11 x 6 x 0.2 sized specimen.
        '''
        length = 11
        width = 6
        thickness = 0.2
        Nl = 6
        Nw = 4
        Nt = 3
        name = "Testing_Plotting"
        testMesh = Mesh(length, width, thickness, name, Nl, Nw, Nt)
        testMesh.generateMesh()
        print(testMesh)
        testMesh.printNodes()
        testMesh.printElements()
        testMesh.plot3D()
        self.assertEqual(Nl * Nw * Nt, testMesh.getNumberofNodes())
        self.assertEqual((Nl - 1) * (Nw - 1)* (Nt - 1), testMesh.getNumberofElements())

if __name__ == '__main__':
    unittest.main()
