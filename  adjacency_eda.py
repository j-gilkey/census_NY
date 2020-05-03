import pandas as pd
import percent_public_trasnpo
import networkx as nx
import matplotlib.pyplot as plt

def process_tuples(tuple_input):
    final_tuples = []

    for tuple in tuple_input:
        if (tuple[1],tuple[0]) not in final_tuples:
            if tuple[1] != tuple[0]:
                final_tuples.append((str(tuple[0]),str(tuple[1])))

    return final_tuples

def process_counties(df):
    final_list = []
    for index, row in df.iterrows():
        node = (str(index), {'percent_public_transpo': row['percent_public_transpo'], 'county_name': row['county_name']})
        final_list.append(node)
    #print(final_list)
    return final_list


def draw_graph(G):
    plt.close()
    #plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    plt.show()
    return


def adjacency_graph():

    df = percent_public_trasnpo.create_dataframe()
    #get ny transpo census data
    county_FIPS_list = list(df.index)
    county_FIPS = process_counties(df)
    #make a list of each county

    adj_df = pd.read_csv('county_adjacency2010.csv')
    #read in adjancency data
    adj_df = adj_df[adj_df['fipscounty'].isin(county_FIPS_list)]
    adj_df = adj_df[adj_df['fipsneighbor'].isin(county_FIPS_list)]
    #filter down to only NY counties
    adj_df = adj_df[['fipscounty', 'fipsneighbor']]
    #remove all columns but FIPS
    fips_tuples = list(adj_df.itertuples(index=False, name=None))
    fips_tuples = process_tuples(fips_tuples)

    G = nx.Graph()
    G.add_nodes_from(county_FIPS)
    #print(G.nodes)
    G.add_edges_from(fips_tuples)
    #instantiate graph and add nodes for each county FIPS

    draw_graph(G)


    #print(adj_df.head)
    #print(fips_tuples)
    #print(df.head)

adjacency_graph()
