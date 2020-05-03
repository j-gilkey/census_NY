import pandas as pd
import percent_public_trasnpo
import networkx as nx


def adjacency_graph():

    df = percent_public_trasnpo.create_dataframe()
    #get ny transpo census data
    county_FIPS = list(df.index)
    #make a list of each county

    adj_df = pd.read_csv('county_adjacency2010.csv')
    #read in adjancency data
    adj_df = adj_df[adj_df['fipscounty'].isin(county_FIPS)]
    #filter down to only NY counties

    G = nx.Graph()
    G.add_nodes_from(county_FIPS)
    #instantiate graph and add nodes for each county FIPS


    print(adj_df.head)
    #print(df.head)

adjacency_graph()
