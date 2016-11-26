import pandas as pd
import numpy as np

from print_graph.thing import convert_pandas_to_stl


def generate_2d_pandas_table():
    # return pd.DataFrame([[1, 2, 0.5, 1], [1, 2, 1, 1]], index=['one', 'two']).transpose()
    return pd.DataFrame(np.random.random_sample((2, 20)), index=['one', 'two']).transpose()


def generate_2d_stl_from_pandas():
    df = generate_2d_pandas_table()
    print df
    stl = convert_pandas_to_stl(df)

    filename = '/data/_example_two_dimension.stl'
    stl.save(filename)


if __name__ == "__main__":
    generate_2d_stl_from_pandas()
