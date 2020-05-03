import pandas as pd
import censusdata
from tabulate import tabulate
import plotly.figure_factory as ff

df = censusdata.download('acs5', 2015,
                             censusdata.censusgeo([('state', '36'), ('tract', '*')]),
                             ['B08301_001E', 'B08301_010E'])

print(df.head)
