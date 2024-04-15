from tqdm import tqdm
import pandas as pd

def time_series_workload(df, start_col='Open Date', end_col='Closed Date', label_col='Subject'):
    """Function for adding the workload for time series."""

    alldates = pd.date_range(start=df[start_col].min(),end=df[end_col].max(),freq='D')
    dates, labels = [], []
    for d in tqdm(alldates):
        tmp = df[(df[start_col] <= d)&(df[end_col] >= d)][label_col].tolist()
        dates += [d]*len(tmp)
        labels += tmp

    workload = pd.DataFrame(zip(*[dates,labels]), columns=['date', 'label'])
    workload = workload.groupby('date').value_counts().reset_index()

    return workload