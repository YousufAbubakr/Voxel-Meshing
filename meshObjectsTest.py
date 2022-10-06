from meshObjects import *
import unittest

class TestStringMethods(unittest.TestCase):

    def testUnitNodes(self):
        ''' Tests unit mesh generation by defining a 1 x 1 x 1 unit
        size box that is defined by 1 (Nl, Nw, Nt - 1) element.
        '''
        length = 1
        width = 1
        thickness = 1
        Nl = 2
        Nw = 2
        Nt = 2
        assert Nl == 2 and Nw == 2 and Nt == 2, "Only want 1 element for this test!"
        unitMesh = Mesh(length, width, thickness, Nl, Nw, Nt)
        unitMesh.genNodes()
        self.assertEqual(Nl * Nw * Nt, len(unitMesh.globalNodes))
        self.assertTrue(([0, length] == unitMesh.lpos).all())
        self.assertTrue(([0, width] == unitMesh.wpos).all())
        self.assertTrue(([0, thickness] == unitMesh.tpos).all())

if __name__ == '__main__':
    unittest.main()