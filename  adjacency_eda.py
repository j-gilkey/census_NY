import pandas as pd
import percent_public_trasnpo
import networkx as nx

def process_tuples(tuple_input):
    final_tuples = []

    for tuple in tuple_input:
        if (tuple[1],tuple[0]) not in final_tuples:
            if tuple[1] != tuple[0]:
                final_tuples.append(tuple)

    return final_tuples


def adjacency_graph():

    df = percent_public_trasnpo.create_dataframe()
    #get ny transpo census data
    county_FIPS = list(df.index)
    #make a list of each county

    adj_df = pd.read_csv('county_adjacency2010.csv')
    #read in adjancency data
    adj_df = adj_df[adj_df['fipscounty'].isin(county_FIPS)]
    #filter down to only NY counties
    adj_df = adj_df[['fipscounty', 'fipsneighbor']]
    #remove all columns but FIPS
    fips_tuples = list(adj_df.itertuples(index=False, name=None))
    print(len(fips_tuples))
    fips_tuples = process_tuples(fips_tuples)
    print(len(fips_tuples))

    G = nx.Graph()
    G.add_nodes_from(county_FIPS)
    #instantiate graph and add nodes for each county FIPS


    print(adj_df.head)
    print(fips_tuples)
    #print(df.head)

adjacency_graph()
