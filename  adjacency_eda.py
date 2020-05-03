import pandas as pd


def adjacency_graph():
    adj_df = pd.read_csv('county_adjacency2010.csv')

    df = censusdata.download('acs5', 2015,
                                 censusdata.censusgeo([('state', '36'), ('county', '*')]),
                                 ['B08301_001E', 'B08301_010E'])

print(df.head)
