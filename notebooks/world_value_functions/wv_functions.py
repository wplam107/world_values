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

def a_given_b(df, a=[], b=[]):
    temp = df
    for trait in b:
        temp = temp.loc[temp[trait] == True]

def apriori(df, country='ALL', selected_traits=[]):
    # Preprocessing
    df = _build_working_df(df)
    df = _select_country(df, country)

    # Total observations
    total_obs = len(df)

    # Subset of selected traits
    b_sub = _select_traits(df, selected_traits=selected_traits)

    # Proportion of subset
    st_obs = len(sub)
    proportion_sub = round(st_obs / total_obs, 4)

    # List of unselected traits
    ns_traits = [ trait for trait in TRAITS if trait not in selected_traits ]

    # DataFrame of proportions
    overall_p = [ round(sum(sub[trait]) / total_obs, 4) for trait in ns_traits ]
    agb_p = [ round(sum(sub[trait]) / st_obs, 4) for trait in ns_traits ]
    data = pd.DataFrame()
    data['A'] = ns_traits
    data['B'] = ', '.join(selected_traits)
    data['A and B Proportion'] = overall_p
    data['A given B Proportion'] = agb_p

    return data
