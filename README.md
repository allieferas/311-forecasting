# 311-forecasting

Predicting the current workload for 311 service requests for city officials

Project steps:

* clean_data.ipynb - pull down raw data, place cleaned data in data/raw
* workload.ipynb - maps departments that belong together based on research, calculates workload per city/department/day
* seasonality_analysis.ipynb - analyzing trends and seasonality by city and department. Dropping departments for which there are insufficient data/trend. Produced merged dataset in data/out