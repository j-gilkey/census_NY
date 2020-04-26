import pandas as pd
import censusdata

pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.precision', 2)

# sample = censusdata.search('acs5', 2015, 'concept', 'transportation')#[160:170]
#
# print(len(sample))
#
# for item in sample:
#     print(item)




censusdata.printtable(censusdata.censustable('acs5', 2015, 'B08301'))
#
# states = censusdata.geographies(censusdata.censusgeo([('state', '*')]), 'acs5', 2015)
#
#
# counties = censusdata.geographies(censusdata.censusgeo([('state', '36'), ('county', '*')]), 'acs5', 2015)
#
# #print(counties)
#
# # data = censusdata.download('acs5', 2015,
# #                              censusdata.censusgeo([('state', '36'), ('county', '081'), ('block group', '*')]),
# #                              ['B23025_001E', 'B23025_002E', 'B23025_003E', 'B23025_004E', 'B23025_005E',
# #                               'B23025_006E', 'B23025_007E'])
#
data = censusdata.download('acs5', 2015,
                             censusdata.censusgeo([('state', '36'), ('county', '*')]),
                             [ 'B08301_003E', 'B08301_004E','B08301_011E', 'B08301_012E', 'B08301_013E','B08301_014E', 'B08301_015E',
                                'B08301_016E', 'B08301_017E', 'B08301_018E','B08301_019E', 'B08301_020E', 'B08301_021E'])
print(data.head)
