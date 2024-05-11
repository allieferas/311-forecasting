from tqdm import tqdm
import pandas as pd
import numpy as np
from datetime import timedelta

def time_series_workload(df, city_name, start_col='open_date', end_col='close_date', label_col='department'):
    """Function for adding the workload for time series. Dataframe should only contain one city."""

    alldates = pd.date_range(start=df[start_col].dt.date.min(),end=df[end_col].max(),freq='D')

    final = (
        pd.MultiIndex
        .from_product([alldates,df[label_col].unique()], names=['date',label_col])
        .to_frame(index=False)
    )
    final['date'] = final['date'].dt.date

    df[start_col] = df[start_col].dt.date
    df[end_col] = df[end_col].dt.date

    counts = pd.DataFrame()
    for d in tqdm(final['date'].unique()):
        tmp = (
            df[
                (df[start_col] <= d)
                &(
                    (df[end_col] >= d)
                    |(df[end_col].isna())
                )][label_col]
            .value_counts()
            .reset_index()
        )
        tmp['date'] = d
        counts = pd.concat([counts, tmp])
    
    final = final.merge(counts, how = 'left').fillna(0)

    final['city'] = city_name

    return final

def time_series_newtix(df, city_name, start_col='open_date', end_col='close_date', label_col='department'):
    """Function for adding the workload for time series. Dataframe should only contain one city."""

    df['week_start'] = (df[start_col] - df[start_col].dt.weekday * timedelta(days=1)).dt.date

    start = df['week_start'].min() - timedelta(days=7)
    end = df['week_start'].max()
    alldates = pd.date_range(start=start,end=end,freq='W') + timedelta(days=1)

    ywl = (
        pd.MultiIndex
        .from_product([alldates,df[label_col].unique()], names=['week_start',label_col])
        .to_frame(index=False)
    )

    counts = df.groupby(['week_start',label_col]).size().reset_index().rename(columns={0: 'count'})
    counts['week_start'] = pd.to_datetime(counts['week_start'])
    final = ywl.merge(counts, how = 'left').fillna(0)

    final['city'] = city_name

    return final