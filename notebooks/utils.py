from tqdm import tqdm
import pandas as pd

def time_series_workload(df, city_name, start_col='open_date', end_col='close_date', label_col='department'):
    """Function for adding the workload for time series. Dataframe should only contain one city."""

    alldates = pd.date_range(start=df[start_col].min(),end=df[end_col].max(),freq='D')
    dates, labels = [], []
    for d in tqdm(alldates, desc="Collecting active records by date"):
        tmp = df[(df[start_col] <= d)&(df[end_col] >= d)][label_col].tolist()
        dates += [d]*len(tmp)
        labels += tmp

    print("Calculating the workload...")
    workload = pd.DataFrame(zip(*[dates,labels]), columns=['date', 'label'])
    workload = (
        workload
        .pivot_table(index='date', columns='label', aggfunc=len, fill_value=0)
        .reset_index()
        .melt(id_vars='date')
    )

    workload['city'] = city_name

    return workload