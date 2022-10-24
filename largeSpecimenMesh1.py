from meshObjects import *

# Generates and writes mesh files for various specimen geometries

# NOTE: avoid using Mesh.plot3D() for large meshes!!

# 11 x 6 x 0.2 specimen, 10 elements across thickness (~20 minutes):
length = 11
width = 6
thickness = 0.2
# Unit cube element edge length:
R = float(thickness/2)
Nl = 61
Nw = 31
Nt = 11
name = "Large_Specimen_Mesh1"
specimen = Mesh(length, width, thickness, name, Nl, Nw, Nt)
print("Mesh Quality: ", specimen.skewness)
specimen.generateMesh()
specimen.writeMesh()
print(specimen)
specimen.printNodes()
specimen.printElements()
