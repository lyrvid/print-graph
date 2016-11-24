import requests
import datetime
import pandas as pd

from xml.etree import ElementTree as ET
from print_graph.thing import convert_pandas_to_stl, convert_1d_pandas_to_stl


def get_ny_treasury_xml():
    url = "http://data.treasury.gov/feed.svc/DailyTreasuryYieldCurveRateData"
    response = requests.get(url)
    return response.text


def convert_ny_treasury_xml_to_list_of_dicts(ny_treasury_xml):
    ns = {"d": "http://schemas.microsoft.com/ado/2007/08/dataservices",
          "m": "http://schemas.microsoft.com/ado/2007/08/dataservices/metadata"}
    tree = ET.fromstring(ny_treasury_xml)
    property_tags = tree.findall(".//m:properties", namespaces=ns)

    list_of_dicts = list()
    i = 0
    for pt in property_tags:
        if i > 1000:
            break
        d = dict()
        for c in pt.getchildren():
            column = c.tag.split('}')[-1]
            data = c.text

            type = c.get([a for a in c.attrib if 'type' in a][0])

            if data:
                if type in ['Edm.Double']:
                    data = float(data)
                elif type in ['Edm.DateTime']:
                    data = datetime.datetime.strptime(data, "%Y-%m-%dT%H:%M:%S")
                elif type in ['Edm.Int32']:
                    data = int(data)
                else:
                    raise ValueError('Unrecognised data type!')

            d.update({column: data})
            list_of_dicts.append(d)
            i += 1
    return list_of_dicts


def generate_stl_for_ny_treasury_yield_rates():
    ny_treasury_xml = get_ny_treasury_xml()
    data = convert_ny_treasury_xml_to_list_of_dicts(ny_treasury_xml)
    df = pd.DataFrame(data)
    del df['Id']

    # stl = convert_pandas_to_stl(df)
    for c in df.columns:
        if c != "BC_3MONTH":
            del df[c]

    stl = convert_1d_pandas_to_stl(df, x_step=0.001, y_step=1.2, z_step=5)

    filename = '_example_ny_treasury_stl.stl'
    stl.save(filename)


if __name__ == "__main__":
    generate_stl_for_ny_treasury_yield_rates()
