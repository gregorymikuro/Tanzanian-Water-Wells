# Tanzanian Water Wells: Functionality Prediction

## Overview

This machine learning project aims to address the critical challenge of non-functional or malfunctioning water wells in Tanzania. By building a predictive model, we seek to classify water wells as "functional," "non-functional," or "functional needs repair," thereby enabling more efficient resource allocation for repairs and maintenance. The model is designed to assist both NGOs and government agencies in improving water access for Tanzanian communities.

## Project Structure

This project is organized into the following components, implemented as Python classes for modularity and reusability:

1.  **Data Extractor:** Loads and combines raw data.
2.  **Data Overview:** Provides a summary of the dataset (head, tail, descriptions, etc.).
3.  **Data Cleaning:** Cleans and prepares data for analysis.
4.  **Exploratory Data Analysis (EDA):**  Examines data distributions, relationships, and visualizations.
5.  **Modeling:** Trains and evaluates various machine learning models.
6.  **Evaluation:** Assesses model performance and selects the best-performing one(s).
7.  **Deployment:** Creates a Streamlit application for prediction based on user input.

## Business Understanding

**Problem Statement:** Tanzania struggles to provide clean water due to numerous non-functional or malfunctioning water wells, leading to health risks and hindering development.

**Objectives:**

1.  Develop a predictive model to classify water well functionality.
2.  Identify key factors influencing well functionality to inform future well design and maintenance.

**Proposed Solution:**
A machine learning classifier will be trained on historical data to predict the status of new wells. We aim for an accuracy score of at least 80%.

**Metrics:**
- Accuracy
- Precision
- Recall
- F1-Score

**Conclusion:** By identifying wells in need of repair, the project aims to improve water access and enhance the quality of life for Tanzanian communities.

## Data Understanding

**Source:**
The dataset was obtained from the DrivenData competition "Pump It Up: Data Mining the Water Table": [https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/](https://www.drivendata.org/competitions/7/pump-it-up-data-mining-the-water-table/page/23/)

**Datasets:**
- **`training-set-values`
- **`training-set-labels`
- **`test-set-values`

**Columns (Key Features):**
- `amount_tsh`: Total static head (amount of water available to pump).
- `funder`, `installer`: Entities responsible for funding and installation.
- `gps_height`: Altitude of the well.
- `longitude`, `latitude`: Geographic coordinates.
- `basin`: Geographic water basin.
- `population`: Population around the well.
- `public_meeting`: Indicator of a public meeting about the project.
- `scheme_management`: Entity managing the water supply scheme.
- `permit`: Indicator of a government construction permit.
- `construction_year`: Year of construction.
- `extraction_type_class`: Type of extraction technology.
- `management_group`: Management type of the well.
- `payment_type`: Water cost structure.
- `quality_group`: Water quality.
- `quantity`: Water quantity.
- `source_class`: General water source type.
- `waterpoint_type`: Type of well.
- `status_group`: Target variable (functional, non-functional, functional needs repair).


## Data Cleaning and Preparation

- Converted `date_recorded` to `year_recorded`.
- Imputed missing values in categorical columns using the mode.
- Imputed zero values in `construction_year`.
- Dropped irrelevant columns.
- Encoded categorical variables with less than 25 unique values.
- Scaled numerical features.


## Exploratory Data Analysis (EDA)

- **Univariate Analysis:** Examined distributions of individual features.
- **Bivariate Analysis:** Assessed correlations between numerical features and low-cardinality categorical features using a heatmap.
- **Multivariate Analysis:** Visualized the geographical distribution of well statuses using latitude, longitude, and a color-coded heatmap.

## Modeling and Evaluation

- **Models:**
    - Simple Decision Tree (Baseline)
    - Tuned Decision Tree (Hyperparameter tuning)
    - K-Nearest Neighbors (KNN)
    - Random Forest
    - XGBoost
    - Voting Classifier (Ensemble of top 3 models)
- **Evaluation:**
    - Used accuracy, confusion matrix, and classification report for evaluation.
    - Due to computational constraints, extensive hyperparameter tuning was not performed.

## Deployment

- A Streamlit application was created to allow users to input well features and get predictions on the well's functionality status.

## Conclusion and Recommendations

The Voting Classifier performed best with an accuracy level of 80%. The models show promise in predicting water well functionality, but there's room for improvement, especially for the 'functional needs repair' class. It's recommended to collect more data, especially for this class, and explore advanced feature engineering techniques. Alternative models and cost-sensitive learning approaches could also be considered.

Future work includes deployment, monitoring, and the creation of an interactive dashboard to visualize the results and gain further insights.
