import numpy as np

from stl import mesh
from print_graph.draw_3d_shapes import Cube, Pyramid


def convert_pandas_to_stl(df):
    raise NotImplementedError("ohnoes")


def _optimise_dataframe(df):
    df = df.round(2)

    values = []
    frequencies = []

    cur_freq = 1
    for idx in range(len(df)):
        val = df.iloc[idx, 0]
        if not values:
            values.append(val)
        else:
            if val == values[-1]:
                cur_freq += 1
            else:
                frequencies.append(cur_freq)
                values.append(val)
                cur_freq = 1
    return zip(values, frequencies)




def _walk_df_and_draw_shapes(df, x_step=1, y_step=1, z_step=1):
    last_point = None

    optimised = _optimise_dataframe(df)
    arrays = []
    for idx, (current_point, freq) in enumerate(optimised):
    # for idx in range(len(df)):
        # current_point = df.iloc[idx, 0]
        if idx == 0:
            last_point = current_point
            continue

        if idx == 1:
            x1 = 0
            x2 = 1 + (freq * x_step)
        else:
            x1 = x2
            x2 = x1 + (freq * x_step)

        z1 = 0
        z2 = 1 * z_step

        y1 = last_point * y_step
        y2 = current_point * y_step

        if current_point == last_point:
            # This is a square, we can draw it all the way to the base
            cube = Cube(x1, x2, 0, y2, z1, z2)
            arrays.extend(cube.top_face())
            arrays.extend(cube.bottom_face())
            arrays.extend(cube.back_left_face())
            arrays.extend(cube.front_right_face())

            if idx == 1:
                arrays.extend(cube.front_left_face())
            elif idx == (len(df) - 1):
                arrays.extend(cube.back_right_face())
        else:
            pyramid = Pyramid(x1, x2, y1, y2, z1, z2)
            cube = Cube(x1, x2, 0, min(y1, y2), z1, z2)

            arrays.extend(cube.bottom_face())
            arrays.extend(cube.back_left_face())
            arrays.extend(cube.front_right_face())

            arrays.extend(pyramid.back_face())
            arrays.extend(pyramid.front_face())

            if idx == 1:
                arrays.extend(cube.front_left_face())
                arrays.extend(pyramid.left_side())
            elif idx == (len(optimised) - 1):
                arrays.extend(cube.back_right_face())
                arrays.extend(pyramid.right_side())

            if y2 > y1:
                arrays.extend(pyramid.left_side())
            else:
                arrays.extend(pyramid.right_side())

        last_point = current_point
    return np.array(arrays)


def convert_1d_pandas_to_stl(df, x_step=1, y_step=1, z_step=1):
    df = df.fillna(0.0)

    faces = _walk_df_and_draw_shapes(df, x_step=x_step, y_step=y_step, z_step=z_step)
    data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
    data['vectors'] = faces
    return mesh.Mesh(data)
