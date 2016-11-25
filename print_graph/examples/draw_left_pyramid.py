import numpy as np

from stl import mesh
from print_graph.draw_3d_shapes import Pyramid, Pyramid2, join_points


def cube():
    # pyramid = Pyramid(0, 5, 0, 5, 0, 5)
    pyramid = Pyramid2(0, 5, 5, 0, 3, 0, 0, 5)
    faces = []
    faces.extend(pyramid.left_side())
    faces.extend(pyramid.right_side())
    faces.extend(pyramid.back_face())
    faces.extend(pyramid.front_face())
    faces.extend(pyramid.bottom())
    faces = join_points(0, 5, 0, 5, 2, 0, 0, 5)
    faces = np.array(faces)
    data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
    data['vectors'] = faces
    object = mesh.Mesh(data)

    object.save("/pyramid.stl")


if __name__ == "__main__":
    cube()
