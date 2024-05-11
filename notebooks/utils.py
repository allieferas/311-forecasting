from tqdm import tqdm
import pandas as pd

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

    df['year'] = df[start_col].dt.isocalendar().year
    df['week'] = df[start_col].dt.isocalendar().week
    df['year_week'] = (df['year'].astype(str) + df['week'].astype(str).str.zfill(2)).astype(int)

    yw = (
        pd.MultiIndex
        .from_product([range(df['year'].min(),df['year'].max()+1),range(1,53)], names=['year','week'])
        .to_frame(index=False)
    )
    yw['year_week'] = (yw['year'].astype(str) + yw['week'].astype(str).str.zfill(2)).astype(int)

    ywl = (
        pd.MultiIndex
        .from_product([yw['year_week'],df[label_col].unique()], names=['year_week',label_col])
        .to_frame(index=False)
    )

    counts = df.groupby(['year_week',label_col]).size().reset_index().rename(columns={0: 'count'})
    final = ywl.merge(counts, how = 'left').fillna(0)

    final['city'] = city_name

    return final