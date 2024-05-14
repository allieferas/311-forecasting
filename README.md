# 311-forecasting

Predicting the current workload for 311 service requests for city officials

Project steps:

* clean_data.ipynb - pull down raw data, place cleaned data in data/raw
* newtix.ipynb - maps departments that belong together based on research, new tickets per week/city/department, seasonality analysis and selection of train/test data
* hyperparameters.ipynb - analyzing stationarity, seasonality, and selecting hyperparameters
* model_training.ipynb - training and predicting all 16 models based on hyperparameters
* visualization.ipynb


| City            | Compatible | Avalibility       | Notes / Errors      | Website                                                                                                      |
| :-------------: | :--------: | :---------------: | :-------------------------------: | :----------------------------------------------------------------------------------------------------------: |
| Austin, TX           | NO         | N/A               | Department Column N/A             | https://data.austintexas.gov/Utilities-and-City-Services/Austin-311-Public-Data/xwdj-i9he/about_data         |
| Baltimore, MD        | YES        | 2003 - Current    | N/A                               | https://data.baltimorecity.gov/City-Services/311-Customer-Service-Requests/9agw-sxsr                         |
| Boston, MA           | YES        | 2011 - 2024       | N/A                               | https://data.boston.gov/dataset/311-service-requests                                                         |
| Buffalo, NY          | YES        | JUL2008 - Current | N/A                               | https://data.buffalony.gov/Quality-of-Life/311-Service-Requests/whkc-e5vr/about_data                         |
| Chicago, IL          | NO         | N/A               | Export Server Error               | https://data.cityofchicago.org/Service-Requests/311-Service-Requests/v6vf-nfxy/about_data                    |
| Dallas, TX           | YES        | OCT2019 - SEP2020 | N/A                               | https://www.dallasopendata.com/Services/311-Service-Requests-October-1-2019-to-September-3/m36q-vtbr/explore |
| Denver, CO           | YES        | 2007 - Current    | N/A                               | https://www.denvergov.org/opendata/dataset/city-and-county-of-denver-311-service-requests-2007-to-current    |
| Houston, TX          | NO         | N/A               | Could Not Find Data               | https://andrew-friedman.github.io/jkan/datasets/311-City-of-Houston/                                         |
| Kansas City, MO      | NO         | N/A               | Export Server Error               | https://data.kcmo.org/311/311-Call-Center-Service-Requests-2007-March-2021/7at3-sxhp/about_data              |
| Las Vegas, CA        | NO         | N/A               | Could Not Find Data               | https://andrew-friedman.github.io/jkan/datasets/311-City-of-Las-Vegas/                                       |
| Los Angeles, CA      | YES        | 2019              | Coded departments                 | https://data.lacity.org/City-Infrastructure-Service-Requests/MyLA311-Service-Request-Data-2019/pvft-t768/about_data   |
| Louisville, KY       | YES        | 1997-Current      | Only Date, No Time                | https://data.louisvilleky.gov/search?tags=311%2520services                                                   |
| Memphis, TN          | YES        | 2016-Current      | N/A                               | https://data.memphistn.gov/dataset/Service-Requests-since-2016/hmd4-ddta/about_data                          |
| Miami, FL            | YES        | 2014-Current      | N/A                               | https://gis-mdc.opendata.arcgis.com/datasets/fce9527342684373adf6c52aa0cd1932_0/about                        |
| Milwaukee, WI        | NO         | N/A               | Department Column N/A             | https://data.milwaukee.gov/dataset/callcenterdatacurrent                                                     |
| Minneapolis, MN      | YES        | 2016-Current      | N/A                               | https://opendata.minneapolismn.gov/search?tags=311                                                           |
| Nashville, TN        | YES        | 2017-Current      | N/A                               | https://data.nashville.gov/Public-Services/hubNashville-311-Service-Requests/7qhx-rexh/about_data            |
| New Orleans, LA      | NO         | 2012-2018         | Department Column N/A             | https://data.nola.gov/City-Administration/311-Calls-Historic-Data-2012-2018-/3iz8-nghx/about_data            |
| Oakland, CA          | YES        | 2012-Current      | N/A                               | https://data.oaklandca.gov/Infrastructure/OAK-311-Service-Request-Map/yp8e-dukj                              |
| Philadelphia, PA     | YES        | 2015-Current      | N/A                               | https://opendataphilly.org/datasets/311-service-and-information-requests/                                    |
| Phoenix, AZ          | NO         | 2015-Current      | Department and Closed Columns N/A | https://www.phoenixopendata.com/dataset/calls-for-service                                                    |
| Sacramento, CA       | NO         | 2016-Current      | Closed Column N/A                 | https://data.cityofsacramento.org/search?tags=Service%2520Requests                                           |
| San Antonio, TX      | YES        | For The Last Year | Only Date, No Time                | https://data.sanantonio.gov/dataset/service-calls                                                            |
| San Diego, CA        | NO         | 2016-Current      | Department Column N/A             | https://data.sandiego.gov/datasets/get-it-done-311/                                                          |
| San Francisco, CA    | NO         | 2008-Current      | Export Server Error               | https://data.sfgov.org/City-Infrastructure/311-Cases/vw6y-z8j6/about_data                                    |
| Washington, D.C.     | YES        | 2009-Current      | Coded departments                               | https://opendata.dc.gov/datasets/cityworks-service-requests/explore                                          |

</div>
