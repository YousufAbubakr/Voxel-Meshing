from meshObjects import *

# Generates and writes mesh files for various specimen geometries

# 11 x 6 x 0.2 specimen:
length = 11
width = 6
thickness = 0.2
# Unit cube element edge length:
R = float(thickness/10)
name = "Large_Specimen_Mesh"
specimen = Mesh(length, width, thickness, name, R)
specimen.generateMesh()
print(specimen)
specimen.printNodes()
specimen.printElements()
specimen.plot3D()
specimen.writeMesh()