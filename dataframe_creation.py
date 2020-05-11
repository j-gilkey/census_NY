import pandas as pd
import censusdata

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)



def create_dataframe():
    column_names = ['total_workforce', 'total_unemployed', 'total_transpo', 'drove_alone', 'carpooled', 'total_public_transpo', 'bus', 'streetcar', 'subway', 'railroad', 'ferry', 'taxi', 'motorcycle', 'bike','walked', 'other', 'wfh']
    #descriptive column names to

    df = censusdata.download('acs5', 2015,
                                 censusdata.censusgeo([('state', '36'), ('county', '*')]),
                                 ['B23025_002E', 'B23025_005E', 'B08301_001E', 'B08301_003E', 'B08301_004E', 'B08301_010E', 'B08301_011E', 'B08301_012E', 'B08301_013E','B08301_014E', 'B08301_015E',
                                    'B08301_016E', 'B08301_017E', 'B08301_018E','B08301_019E', 'B08301_020E', 'B08301_021E'])
    #uses the censusdata package to download census information
    #the state numbers is a FIPS code that indicates New York
    #the * in county indicates all counties should be selected
    #the list of codes like 'B23025_002E' refers to specfic tables of census date that were looked up beforehand


    df = pd.DataFrame(df)
    df.columns = column_names
    df['percent_unemployed'] = df.apply(lambda row: row['total_unemployed']/row['total_workforce'] , axis = 1)
    #create percentage unemployment column
    df['percent_public_transpo'] = df.apply(lambda row: row['total_public_transpo']/row['total_transpo'] , axis = 1)
    #create percentage public transit use

    index_list = df.index.tolist()
    new_indices = []
    county_names = []

    for index in index_list:
        new_index = index.geo[0][1] + index.geo[1][1]
        new_indices.append(new_index)

        county_name = index.name.split(',')[0]
        county_names.append(county_name)


#create_dataframe()
