import numpy as np

from stl import mesh
from print_graph.draw_3d_shapes import draw_bottom_pyramid


def cube():
    faces = np.array(draw_bottom_pyramid(0, 5, 0, 5, 0, 5, left=False))
    data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
    data['vectors'] = faces
    object = mesh.Mesh(data)

    object.save("/pyramid.stl")


if __name__ == "__main__":
    cube()
