from typing import List
import utils
import pandas as pd
import ast

def robustness(a:List, b:List):
    assert len(a) == len(b)
    return sum([abs(x-y) for x,y in zip(a,b)])/len(a)


# can also be considered as a group fairness metric
def demographic_parity(df: pd.DataFrame):

    labels = list(set(df['label'].tolist()))
    
    # create label ids
    df.loc[:,'label_id'] = [1 if labels[0]==label else 0 for label in df['label']]

    # subsets
    df_A = df[df['label_id'] == 0]
    df_B = df[df['label_id'] == 1]

    # compute demographic parity difference
    parity = abs(len(df_A[df_A['flagged'] == True])/len(df_A) - len(df_B[df_B['flagged'] == True])/len(df_B))

    return parity


def conditional_statistical_parity(df: pd.DataFrame, factors, factor:str):

    labels = list(set(df['label'].tolist()))

    # create label ids
    df.loc[:,'label_id'] = [0 if labels[0]==label else 1 for label in df['label']]

    df.loc[:,'factor'] = factors

    # subset data to keep common factor
    df = df[df['factor'] == factor]

    # subsets
    df_A = df[df['label_id'] == 0]
    df_B = df[df['label_id'] == 1]


    # compute conditional statistical parity
    parity = abs(len(df_A[df_A['flagged'] == True])/len(df_A) - len(df_B[df_B['flagged'] == True])/len(df_B))

    return parity