import numpy as np

from stl import mesh
from print_graph.draw_3d_shapes import Cube


def cube():
    cube = Cube(0, 5, 0, 5, 0, 5)
    faces = []
    faces.extend(cube.back_left_face())
    faces.extend(cube.back_right_face())
    faces.extend(cube.front_left_face())
    faces.extend(cube.front_right_face())
    faces.extend(cube.top_face())
    faces.extend(cube.bottom_face())

    faces = np.array(faces)
    data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
    data['vectors'] = faces
    object = mesh.Mesh(data)

    object.save("/cube.stl")


if __name__ == "__main__":
    cube()
