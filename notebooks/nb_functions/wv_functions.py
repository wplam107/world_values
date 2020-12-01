import numpy as np
import pandas as pd
import networkx as nx
import plotly.graph_objects as go

TRAITS = [
    'manners',
    'independence',
    'hard work',
    'responsibility',
    'imagination',
    'tolerance',
    'thrift',
    'determination',
    'faith',
    'unselfishness',
    'obedience'
]

def _build_working_df(df):
    temp = ['country'] + TRAITS
    if ', '.join((df.columns)) == ', '.join(temp):
        return df
    else:
        return df[['country'] + TRAITS]

def _select_country(df, country='ALL'):
    if country == 'ALL':
        return df
    else:
        assert country in df['country'].unique()
        return df.loc[df['country'] == country]

def _select_traits(df, selected_traits=[]):
    temp = df
    for trait in selected_traits:
        temp = temp.loc[temp[trait] == True]
    return temp

def apriori(df, country='ALL', selected_traits=[]):
    # Preprocessing
    data = _build_working_df(df)
    data = _select_country(data, country)

    # Total observations
    total_obs = len(data)

    # Subset of selected traits
    sub = _select_traits(data, selected_traits=selected_traits)

    # Proportion of subset
    st_obs = len(sub)
    proportion_sub = st_obs / total_obs

    # List of unselected traits
    ns_traits = [ trait for trait in TRAITS if trait not in selected_traits ]

    # Dictionary of proportions
    dict_ = { trait: round(sum(sub[trait]) / st_obs, 4) for trait in ns_traits }
    dict_[', '.join(selected_traits)] = proportion_sub

    return dict_
