import pandas as pd

class MyDF(pd.DataFrame): 
    def null_counts(df):
        return df.isnull().sum().sum()

    def train_test_split(df, frac):
        cutoff = round(len(df) * frac)
        return df[:cutoff], df[cutoff:]
    