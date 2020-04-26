import pandas as pd
import censusdata

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)



censusdata.printtable(censusdata.censustable('acs5', 2015, 'B08301'))

column_names = ['total_workforce', 'total_unemployed', 'total_transpo', 'drove_alone', 'carpooled', 'total_public_transpo', 'bus', 'streetcar', 'subway', 'railroad', 'ferry', 'taxi', 'motorcycle', 'bike','walked', 'other', 'wfh']

df = censusdata.download('acs5', 2015,
                             censusdata.censusgeo([('state', '36'), ('county', '*')]),
                             ['B23025_002E', 'B23025_005E', 'B08301_001E', 'B08301_003E', 'B08301_004E', 'B08301_010E', 'B08301_011E', 'B08301_012E', 'B08301_013E','B08301_014E', 'B08301_015E',
                                'B08301_016E', 'B08301_017E', 'B08301_018E','B08301_019E', 'B08301_020E', 'B08301_021E'])


df = pd.DataFrame(df)
df.columns = column_names
df['percent_unemployed'] = df.apply(lambda row: row['total_unemployed']/row['total_workforce'] , axis = 1)
df['percent_public_transpo'] = df.apply(lambda row: row['total_public_transpo']/row['total_transpo'] , axis = 1)

print(df.head)
