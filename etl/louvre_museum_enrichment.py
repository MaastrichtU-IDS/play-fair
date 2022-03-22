# to run .\etl\[..].py

import pandas as pd
from rdflib import ConjunctiveGraph, Graph, RDFS, URIRef, Literal
# from rdflib.namespaces import RDFS

class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

g = ConjunctiveGraph()
g.parse("data/tableGames.csv.nq", format='nquads')

df = pd.read_csv("./data/collections-louvreM.csv", delimiter = ';')


rich_g = ConjunctiveGraph()

graph_uri = URIRef('https://w3id.org/ludeme/images')

# def check_uri(uri):
#     if str(uri).startswith('http://') or str(uri).startswith('https://'):
#         return True
#     return False

# count = 0
for s, p, o in g.triples((None, RDFS.label, None)):
    game_label = str(o).lower()
    print(f'🔍 Searching for {game_label}...')

    # Find rows in british collection that match our Ludeme game
    # TODO: improve the matching process (we just do basic matching right now)
    pic_df = df[df['Titre'].str.contains(game_label, case = False)]
    if len(pic_df) > 0:
        print(f"✅ Found {color.BOLD}{len(pic_df)}{color.END} entries for {color.YELLOW}{color.BOLD}{game_label}{color.END} in the British Museum Collection")

    for index, row in pic_df.iterrows():
        # try:
        #     rich_g.add((s, URIRef('https://schema.org/image'), URIRef(row['Image']), graph_uri))
        # except Exception as e:
        #     pass

        try:
            rich_g.add((s, URIRef('https://schema.org/productionDate'), Literal(row['Date de création']), graph_uri))
        except Exception as e:
            pass

        try:
            rich_g.add((s, URIRef('https://www.wikidata.org/wiki/Q11514315'), Literal(row['Culture']), graph_uri))
        except Exception as e:
            pass

        try:
            rich_g.add((s, URIRef('https://schema.org/identifier'), Literal(row['Numéro d’inventaire']), graph_uri))
        except Exception as e:
            pass

        # try:
        #     rich_g.add((s, URIRef('https://schema.org/material'), Literal(row['Materials']), graph_uri))
        # except Exception as e:
        #     pass

rich_g.serialize('data/enriched_pic_louvre.nq', format='nquads')
