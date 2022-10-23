from meshObjects import *

# Generates and writes mesh files for various specimen geometries

# NOTE: avoid using Mesh.plot3D() for large meshes!!

# 11 x 6 x 0.2 specimen:
length = 11
width = 6
thickness = 0.2
# Unit cube element edge length:
R = float(thickness/2)
name = "Large_Specimen_Mesh"
specimen = Mesh(length, width, thickness, name, R)
print("Number of Nodes in L Direction: ", specimen.Nl)
print("Number of Nodes in W Direction: ", specimen.Nw)
print("Number of Nodes in T Directio: ", specimen.Nt)
print("Mesh Quality: ", specimen.skewness)
specimen.generateMesh()
print(specimen)
specimen.printNodes()
specimen.printElements()
specimen.writeMesh()