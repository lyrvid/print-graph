import numpy as np

from stl import mesh
from print_graph.draw_3d_shapes import draw_cube


def cube():
    faces = np.array(draw_cube(0, 5, 0, 5, 0, 5))
    data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
    data['vectors'] = faces
    object = mesh.Mesh(data)

    object.save("/cube.stl")


if __name__ == "__main__":
    cube()
