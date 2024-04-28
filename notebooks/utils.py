from tqdm import tqdm
import pandas as pd

def time_series_workload(df, city_name, start_col='open_date', end_col='close_date', label_col='department'):
    """Function for adding the workload for time series. Dataframe should only contain one city."""

    alldates = pd.date_range(start=df[start_col].min(),end=df[end_col].max(),freq='D')

    final = (
        pd.MultiIndex
        .from_product([alldates,df['department'].unique()], names=['date','department'])
        .to_frame(index=False)
    )
    final['date'] = pd.to_datetime(final['date'].dt.date)

    counts = pd.DataFrame()
    for d in tqdm(final['date'].unique()):
        tmp = (
            df[
                (df['open_date'] <= d)
                &(
                    (df['close_date'] >= d)
                    |(df['close_date'].isna())
                )]['department']
            .value_counts()
            .reset_index()
        )
        tmp['date'] = d
        counts = pd.concat([counts, tmp])
    
    final = final.merge(counts, how = 'left').fillna(0)

    final['city'] = city_name

    return final