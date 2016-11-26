import numpy as np

from stl import mesh
from print_graph.draw_3d_shapes import Cube, Pyramid, Pyramid2, join_points


def convert_pandas_to_stl(df, x_step=1, y_step=1, z_step=1):
    df = df.fillna(0.0)

    faces = _walk_df_and_draw_shapes_3d(df, x_step=x_step, y_step=y_step, z_step=z_step)
    data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
    data['vectors'] = faces
    return mesh.Mesh(data)


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
    frequencies.append(cur_freq)
    return zip(values, frequencies)


def _square(x1, x2, y1, y2, z1, z2, first=False, last=False):
    arrays = []

    cube = Cube(x1, x2, 0, y2, z1, z2)

    # arrays.extend(cube.top_face())
    # arrays.extend(cube.bottom_face())

    # if first:
    #     arrays.extend(cube.front_right_face())
    # elif last:
    #     arrays.extend(cube.back_left_face())
    return arrays


def _walk_df_and_draw_shapes_3d(df, x_step=1, y_step=1, z_step=1):
    arrays = []
    for col_idx, column in enumerate(df):
        if col_idx == len(df.columns) - 1:
            break

        first_column = col_idx == 0
        last_column = col_idx == len(df.columns) - 2

        last_point = None
        last_point_second = None

        first_valid_point = None
        first_valid_point_second = None

        for idx in range(len(df[column])):
            current_point = df.iloc[idx, col_idx]
            current_point_second = df.iloc[idx, col_idx+1]

            if first_valid_point is None and current_point > 0:
                first_valid_point = True

            if first_valid_point_second is None and current_point_second > 0:
                first_valid_point_second = True

            if idx == 0:
                last_point = current_point
                last_point_second = current_point_second
                continue

            if idx == 1:
                x1 = 0
                x2 = 1 + x_step

            else:
                x1 = x2
                x2 = x1 + x_step

            z1 = col_idx * z_step
            z2 = (col_idx + 1) * z_step

            y11 = last_point * y_step
            y12 = current_point * y_step
            y21 = last_point_second * y_step
            y22 = current_point_second * y_step

            if current_point == last_point:
                # This is a square, we can draw it all the way to the base
                arrays.extend(_square(x1, x2, y11, y12, z1, z2, first=first_column, last=last_column))
                arrays.extend(_square(x1, x2, y21, y22, z1, z2, first=first_column, last=last_column))
            else:
                cube = Cube(x1, x2, 0, min(y11, y12), z1, z2)
                stuff = join_points(x1, x2, y11, y12, y21, y22, z1, z2)
                arrays.extend(stuff)


                # if first_valid_point:
                #     arrays.extend(cube.back_left_face())
                # elif last_column:
                #     arrays.extend(cube.front_right_face())
                #
                # cube2 = Cube(x1, x2, 0, min(y21, y22), z21, z22)
                # if first_valid_point_second:
                #     arrays.extend(cube2.back_left_face())
                # elif last_column:
                #     arrays.extend(cube2.front_right_face())
                #
                # pyramid = Pyramid(x1, x2, y11, y12, z11, z12)
                # if first_valid_point:
                #     arrays.extend(pyramid.back_face())
                # elif last_column:
                #     arrays.extend(pyramid.front_face())
                #
                # pyramid2 = Pyramid(x1, x2, y21, y22, z21, z22)
                # if first_valid_point_second:
                #     arrays.extend(pyramid2.back_face())
                # elif last_column:
                #     arrays.extend(pyramid2.front_face())


                # if idx == 1:
                #     arrays.extend(cube.front_left_face())
                #     arrays.extend(pyramid.left_side())
                # elif idx == (len(df) - 1):
                #     arrays.extend(cube.back_right_face())
                #     arrays.extend(pyramid.right_side())
                #
                # if y2 > y1:
                #     arrays.extend(pyramid.left_side())
                # else:
                #     arrays.extend(pyramid.right_side())

            last_point = current_point
            last_point_second = current_point_second
            first_valid_point = False
            first_valid_point_second = False

    # arrays.extend(_add_bottom_raft(x1, z22))
    return np.array(arrays)


def _walk_df_and_draw_shapes(df, x_step=1, y_step=1, z_step=1):
    last_point = None

    # optimised = _optimise_dataframe(df)
    arrays = []
    # for idx, (current_point, freq) in enumerate(optimised):
    for idx in range(len(df)):
        current_point = df.iloc[idx, 0]
        freq = 1

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

            arrays.extend(cube.back_left_face())
            arrays.extend(cube.front_right_face())

            arrays.extend(pyramid.back_face())
            arrays.extend(pyramid.front_face())

            if idx == 1:
                arrays.extend(cube.front_left_face())
                arrays.extend(pyramid.left_side())
            elif idx == (len(df) - 1):
                arrays.extend(cube.back_right_face())
                arrays.extend(pyramid.right_side())

            if y2 > y1:
                arrays.extend(pyramid.left_side())
            else:
                arrays.extend(pyramid.right_side())

        last_point = current_point

    arrays.extend(_add_bottom_raft(x2, z2))
    return np.array(arrays)


def _add_bottom_raft(x_max, z_max):
    arrays = []
    cube = Cube(0, x_max, -2, 0, 0, z_max)
    arrays.extend(cube.back_left_face())
    arrays.extend(cube.back_right_face())
    arrays.extend(cube.front_right_face())
    arrays.extend(cube.front_left_face())
    arrays.extend(cube.bottom_face())
    return arrays


def convert_1d_pandas_to_stl(df, x_step=1, y_step=1, z_step=1):
    df = df.fillna(0.0)

    faces = _walk_df_and_draw_shapes(df, x_step=x_step, y_step=y_step, z_step=z_step)
    data = np.zeros(len(faces), dtype=mesh.Mesh.dtype)
    data['vectors'] = faces
    return mesh.Mesh(data)
