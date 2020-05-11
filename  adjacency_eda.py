import pandas as pd
import percent_public_trasnpo
import networkx as nx
from tabulate import tabulate
import matplotlib.pyplot as plt

def filter_tuples(df):
    #takes in an adjancency df and filters out symetrical and self adjacencies
    #this was counties won't have two edges between eachother
    all_tuples = list(df.itertuples(index=False, name=None))
    final_tuples = []

    for tuple in all_tuples:
        #check for symetry
        if (tuple[1],tuple[0]) not in final_tuples:
            #check for self-adjacencies
            if tuple[1] != tuple[0]:
                final_tuples.append((str(tuple[0]),str(tuple[1])))

    return final_tuples

def process_counties_to_nodes(df):
    #takes in a county df and returns a list of 2 tuples ready to be entered as nodes
    #first tuple element is just the county number
    #the second is a dictionary representing node attributes
    final_list = []
    for index, row in df.iterrows():
        node = (str(index), {'percent_public_transpo': row['percent_public_transpo'], 'county_name': row['county_name']})
        final_list.append(node)
    return final_list


def draw_graph(G):
    #takes in a graph object and creates a rendering of it
    plt.close()
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    return


def adjacency_graph():

    df = percent_public_trasnpo.create_dataframe()
    #get ny transpo census data
    county_FIPS_list = list(df.index)
    county_FIPS = process_counties_to_nodes(df)
    #make a list of each county

    adj_df = pd.read_csv('county_adjacency2010.csv')
    #read in adjancency data
    adj_df = adj_df[adj_df['fipscounty'].isin(county_FIPS_list)]
    adj_df = adj_df[adj_df['fipsneighbor'].isin(county_FIPS_list)]
    #filter down to only NY counties
    adj_df = adj_df[['fipscounty', 'fipsneighbor']]
    #remove all columns but FIPS
    fips_tuples = filter_tuples(adj_df)

    G = nx.Graph()
    G.add_nodes_from(county_FIPS)
    G.add_edges_from(fips_tuples)
    #instantiate graph and add nodes for each county FIPS

    draw_graph(G)


#adjacency_graph()
