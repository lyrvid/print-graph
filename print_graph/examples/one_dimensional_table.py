import pandas as pd
import numpy as np

from print_graph.thing import convert_1d_pandas_to_stl


def generate_1d_pandas_table():
    return pd.DataFrame(np.random.random_sample((1, 20)), index=['Random']).transpose()


def generate_1d_stl_from_pandas():
    df = generate_1d_pandas_table()
    stl = convert_1d_pandas_to_stl(df)

    filename = '/data/_example_one_dimension.stl'
    stl.save(filename)


if __name__ == "__main__":
    generate_1d_stl_from_pandas()
