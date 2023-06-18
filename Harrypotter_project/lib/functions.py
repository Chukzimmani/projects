import pandas as pd
import numpy as np
import spacy
from spacy import displacy
import networkx as nx 

import matplotlib.pyplot as plt

def ner(file_name):
    """
    Function to process text from a text file (.txt) using Spacy.

    params:
    file_name -- name of a txt file as string

    Returns:
    a processed doc file using Spacy Ecglish language model
    
    """

    # Load spacy English language model
    nlp = spacy.load("en_core_web_sm")
    nlp.max_length = 1700000
    book_doc = nlp(open(file_name, encoding = "utf-8").read())    
    
    return book_doc


def get_ne_list_per_sentence(spacy_doc):
    """
    Get a list of entites per sentence of a Spacy document and store in a dataframe

    Params:
    spacy_doc -- a Spacy processed document

    Returns:
    a dataframe containing the sentences and corresponding list os recognised names in the sentences
    """
    sent_entity_df = []

    # Loop through sentences, store named entity list for each sentence
    for sent in spacy_doc.sents:
        entity_list = [ent.text for ent in sent.ents]
        sent_entity_df.append ({"sentence":sent, "entities": entity_list})

    sent_entity_df = pd.DataFrame(sent_entity_df)

    return sent_entity_df


def filter_entity(ent_list, character_df):
    """
    Function to filter out non-character entities.

    Params:
    ent_list -- list of entities to be filtered
    character_df -- a dataframe containing characters' names and  characters' first names

    Returns: 
    a list of entities that are characters (matching by names or first names)

    
    """
    return [ent for ent in ent_list
           if ent in list (character_df.character)
           or ent in list (character_df.first_name)]

def create_relationships(df, window_size):

    """
    Create dataframe of relationships based on the df dataframe (containing characters per sentence) and the window size of n sentences.

    Params:
    df -- a dataframe containing a column called character_entities with the characters for each sentence of a document.

    Returns:
    a relationship dataframe containing 3 columns: source, target, value.
    """
    ralationships = []

    for i in range (df.index[-1]):
        end_i = min(i+5, df.index[-1])
        char_list = sum((df.loc[i:end_i].character_entities), [])
    
     #Remove duplicated characters that are next to each other
        char_unique = [char_list[i] for i in range (len(char_list))
                  if (i==0) or char_list[i] != char_list[i-1]] 
    
        if len(char_unique) > 1:
            for idx, a in enumerate(char_unique[:-1]):
                b = char_unique[idx + 1]
                ralationships.append({'source': a, 'target':b})

        relationships_df = pd.DataFrame(ralationships)
        # Sort the cases with a ->b and b->a
        # relationships_df = pd.DataFrame(np.sort(relationships_df.values, axis = 1),
        #                                 columns=relationships_df.columns)
        # relationships_df["value"] = 1
        # relationships_df = relationships_df.groupby(["source", "target"], sort=False,
        #                                             as_index=False).sum()

        return relationships_df


    




