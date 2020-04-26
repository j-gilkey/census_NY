import pandas as pd
import censusdata
from tabulate import tabulate

# pd.set_option('display.expand_frame_repr', False)
# pd.set_option('display.precision', 2)



def create_dataframe():
    column_names = ['total_transpo', 'total_public_transpo']

    df = censusdata.download('acs5', 2015,
                                 censusdata.censusgeo([('state', '36'), ('county', '*')]),
                                 ['B08301_001E', 'B08301_010E'])

    df = pd.DataFrame(df)
    df.columns = column_names
    df['percent_public_transpo'] = df.apply(lambda row: row['total_public_transpo']/row['total_transpo'] , axis = 1)

    #print(tabulate(df, headers='keys', tablefmt='psql'))
    #return

    #index_list = df.index.tolist()
    new_indices = []
    county_names = []

    for index in df.index.tolist():
        new_index = index.geo[0][1] + index.geo[1][1]
        new_indices.append(new_index)

        county_name = index.name.split(',')[0]
        county_names.append(county_name)

    df.index = new_indices
    df['county_name'] = county_names

    print(tabulate(df, headers='keys', tablefmt='psql'))

    #print(new_indices)
    #print(county_names)

    #for county in index_list:


create_dataframe()