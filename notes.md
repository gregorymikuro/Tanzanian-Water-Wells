__Data Extractor__
Data importation  - we have training-set-labels.csv and training-set-values.csv and test-set-values.csv in the data folder.
Connect the traning set values and labels by adding the labels row based on the id column as they have similar ids, particulary the introduction of status_group column from  training-set-labels.csv to training-set-values.csv. after that you'll name a new csv as test_set. then change test-set-values.csv name to test-set.csv.

__Data Overview__
info
head and tail with all columns (40) shown
describe
duplicates
percentage of unique values in each column
missing values and null values percentage


__Data Cleaning__
change date_recorded to year_recorded to incude only the year then delete the date_recorded column
impute 'funder', 'installer', 'subvillage', 'public_meeting', 'scheme_management', 'permit' columns missing values

impute zero values in 'construction_year'


drop 'num_private' 'recorded_by', scheme_name, 'extraction_type_group, 'extraction_type', 'payment', 'water_quality', 'quantity_group', 'source', 'source_type', 'waterpoint_type_group', 'iga', 'ward' columns 







__Exploratory Data Analysis__



__Modeling__ 
drop 'region', 'management' 

__Evaluation__



__Deployment__



__Recommendations and Conclusion__