import pandas as pd
import censusdata
from tabulate import tabulate
import plotly.figure_factory as ff


def create_dataframe():
    column_names = ['total_transpo', 'total_public_transpo']

    df = censusdata.download('acs5', 2015,
                                 censusdata.censusgeo([('state', '36'), ('county', '*')]),
                                 ['B08301_001E', 'B08301_010E'])

    df = pd.DataFrame(df)
    df.columns = column_names
    df['percent_public_transpo'] = df.apply(lambda row: round(row['total_public_transpo']/row['total_transpo']*100,2) , axis = 1)

    new_indices = []
    county_names = []

    for index in df.index.tolist():
        new_index = index.geo[0][1] + index.geo[1][1]
        new_indices.append(new_index)

        county_name = index.name.split(',')[0]
        county_names.append(county_name)

    df.index = new_indices
    df['county_name'] = county_names

    return df


# df = create_dataframe()
#
# fig = ff.create_choropleth(fips=df.index, scope=['New York'], values=df.percent_public_transpo,title='NY Public Transit Use by County', legend_title='% Public Transit', county_outline={'color': 'rgb(15, 15, 55)', 'width': 0.5})
# fig.layout.template = None
# fig.show()
