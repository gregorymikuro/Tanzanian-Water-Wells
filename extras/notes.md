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


'region', 'management' 





__Exploratory Data Analysis__
Univariate
Bivariate 
Multivariate



__Modeling, Evaluation and Deployment__ 


import the cleaned data files data/cleaned_test_set and data/cleaned_training_set

change all categorical variables with less than 25 unique values to numbers
train model using data/cleaned_train_set using all numerical variables except id column, the categorical variables that have been changed as predictors and the status_group which is the target variable. 
scale and encode the data
train in 70 and 30 using the following classifiers
1. Simple Decision Tree - Baseline Model
2. Tuned Decision Tree(Hyperparameter Tuning)
3. KNN
3. Random Forest
4. XGBoost 
5. Combine the top three classifiers 

Evaluation 
For each check for overfitting and underfitting (use l1 or l2 where applicable)
Use the confusion matrix 
Check the best classifier by creating a table on their performances based on the above and create the pickle file for it 

Create user input values for creating streamlit application and ensure that user must input the values or else won't run 

create a new csv file using best performimg model based on values from data/cleaned_test_set that has only 2 rows id and status_group as prediction_result.csv



__Recommendations and Conclusion__




Class Design and Inheritance
Create a set of classes using inheritance to handle a machine learning workflow. The classes should be Modeling, Evaluation, and Deployment.

The Modeling class should:

Import cleaned data from data/cleaned_training_set.csv and data/cleaned_test_set.csv.
Encode all categorical variables with less than 25 unique values as numerical values.
Train several models (Simple Decision Tree, Tuned Decision Tree, KNN, Random Forest, XGBoost) using the cleaned training set. Use a 70/30 train-test split.
Scale and encode the data appropriately.
Combine the top three classifiers into an ensemble model.

The Evaluation class should:

Evaluate each model for overfitting and underfitting (using L1 or L2 regularization where applicable).
Use confusion matrices to evaluate the models.
Create a table comparing the performance of each model.
Save the best performing model as a pickle file.
The Deployment class should:

Allow user input values for a Streamlit application, ensuring all required values are provided.
Use the best performing model to make predictions on the test set and save the results to prediction_result.csv. The output CSV should have two columns: id and status_group.


Data Preprocessing and Model Training
Detail the data preprocessing and model training steps for a machine learning project.

Import the cleaned data from data/cleaned_training_set.csv and data/cleaned_test_set.csv.
Convert all categorical variables with fewer than 25 unique values to numerical values using encoding.
Train the models using all numerical variables, excluding the id column, with the target variable being status_group.
Perform data scaling and encoding.
Train models with a 70/30 train-test split using:
Simple Decision Tree as a baseline model.
Tuned Decision Tree with hyperparameter tuning.
KNN classifier.
Random Forest classifier.
XGBoost classifier.
Combine the top three performing classifiers into an ensemble model.


Model Evaluation
Explain the process of evaluating multiple machine learning models.

Evaluate each model for overfitting and underfitting. Apply L1 or L2 regularization where applicable.
Use confusion matrices to assess the performance of each model.
Create a performance table for comparison, including metrics like accuracy, precision, recall, and F1-score.
Determine the best performing model and save it as a pickle file.
Prompt 4: Deployment and Prediction
Describe the deployment phase of a machine learning project.

Develop a Streamlit application that requires user input for prediction.
Ensure the application only runs if all necessary values are provided by the user.
Use the best performing model to predict outcomes on the test set from data/cleaned_test_set.csv.
Save the predictions to prediction_result.csv with columns id and status_group.
Additional Details
Provide extra implementation details for the classes and methods described:

