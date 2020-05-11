import pandas as pd
import censusdata
from tabulate import tabulate
import plotly.figure_factory as ff


def create_dataframe():

    df = censusdata.download('acs5', 2015,
                                 censusdata.censusgeo([('state', '36'), ('county', '*')]),
                                 ['B08301_001E', 'B08301_010E'])
    df = pd.DataFrame(df)
    #download relevant data and store it in a dataframe

    df.columns = ['total_transpo', 'total_public_transpo']
    #set column names

    df['percent_public_transpo'] = df.apply(lambda row: round(row['total_public_transpo']/row['total_transpo']*100,2) , axis = 1)
    #define a new column that represents the % of public transportation used

    new_indices = []
    county_names = []
    for index in df.index.tolist():
        new_index = index.geo[0][1] + index.geo[1][1]
        new_indices.append(new_index)

        county_name = index.name.split(',')[0]
        county_names.append(county_name)
    #loop through the indices to extract coherent FIPS ids to use as better indices
    df.index = new_indices
    #set new indices
    df['county_name'] = county_names
    #and add a county name column


    return df
