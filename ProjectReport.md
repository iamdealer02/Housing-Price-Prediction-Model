# Project Report: House Price Prediction

## 1. Introduction

This project focuses on predicting house prices using supervised machine learning techniques. The goal is to estimate the selling price of a house from structural and location-related features such as area, number of bedrooms, bathrooms, stories, parking capacity, and amenities. House price prediction is a practical regression problem because the target variable is continuous and depends on multiple interacting factors.

The project follows a complete machine learning workflow: data loading, exploratory data analysis, preprocessing, model training, evaluation, and comparative analysis.

## 2. Objective

The main objective of this project is to build and compare multiple regression models in order to identify which one predicts house prices most effectively on the selected dataset.

More specifically, the project aims to:

- Understand the structure and quality of the dataset
- Prepare the data for machine learning
- Train several regression algorithms
- Evaluate model performance using standard regression metrics
- Compare results and identify the best-performing model

## 3. Dataset Description

The dataset used in this project is the Kaggle dataset `yasserh/housing-prices-dataset`. It contains housing records with numerical and categorical attributes.

### Dataset summary

- Number of rows: `545`
- Number of columns: `13`
- Missing values: `0`

### Features

The dataset includes the following columns:

- `price`
- `area`
- `bedrooms`
- `bathrooms`
- `stories`
- `mainroad`
- `guestroom`
- `basement`
- `hotwaterheating`
- `airconditioning`
- `parking`
- `prefarea`
- `furnishingstatus`

### Observations from the raw data

- The target variable is `price`
- The dataset contains both numerical and categorical features
- No missing values were found
- Outliers are present in variables such as `area` and `price`
- Several amenities are represented as binary categorical values (`yes/no`)

## 4. Exploratory Data Analysis

Exploratory analysis was carried out in `01.data-exploration.ipynb`. The purpose of this phase was to understand feature distributions and the relationship between predictors and house price.

The following analyses were performed:

- Distribution of house prices
- Distribution of house area
- Relationship between `area` and `price`
- Relationship between `bedrooms` and `price`
- Relationship between `stories` and `price`
- Correlation heatmap for numeric variables
- Price comparison across categorical variables
- Outlier inspection with boxplots

### Key insights

- House price tends to increase with area
- Houses with more bedrooms, bathrooms, and stories generally have higher prices
- Categorical amenities such as air conditioning, guest room, basement, and preferred area appear to influence price
- Outliers could distort model training, especially in `price` and `area`

## 5. Data Preprocessing

Preprocessing was implemented in `02.preprocessing.ipynb`.

### Steps performed

1. Binary encoding was applied to categorical columns with `yes/no` values:

- `mainroad`
- `guestroom`
- `basement`
- `hotwaterheating`
- `airconditioning`
- `prefarea`

2. One-hot encoding was applied to:

- `furnishingstatus`

3. Outlier handling was performed using the Interquartile Range (IQR) method on:

- `area`
- `price`

Instead of removing extreme rows, values outside the accepted range were capped at the lower or upper boundary. This keeps all rows while reducing the influence of extreme values.

4. The processed dataset was split into:

- `x.csv` for input features
- `y.csv` for the target variable

## 6. Model Building

Model training was carried out in `03.Models.ipynb`.

The processed data was divided into training and testing sets using:

- Test size: `0.23`
- Random state: `42`

### Models trained

The following regression models were trained and evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. Gradient Boosting Regressor
5. XGBoost Regressor

### Tuning strategy

- `GridSearchCV` was used for Linear Regression, Decision Tree, Random Forest, and Gradient Boosting
- `RandomizedSearchCV` was used for XGBoost
- `KFold` cross-validation with `5` folds was used for model selection

### Additional training details

- Linear Regression was combined with `MinMaxScaler` and `RFE` for feature selection
- Trained models were saved as `.pkl` files in the `models/` directory
- Prediction outputs for each model were saved in `models/predictions/`

## 7. Evaluation Metrics

The models were compared using the following regression metrics:

- `R2`: measures how well the model explains variance in house price
- `RMSE`: measures the average size of prediction error with stronger penalty on large errors
- `MAE`: measures the average absolute prediction error

For this project:

- Higher `R2` is better
- Lower `RMSE` is better
- Lower `MAE` is better

## 8. Results

The final saved model results are shown below.

| Model | RMSE | R2 | MAE |
|---|---:|---:|---:|
| Linear Regression | 1,083,668.23 | 0.7014 | 835,546.51 |
| Decision Tree | 1,429,795.45 | 0.4802 | 1,109,590.81 |
| Random Forest | 1,138,949.52 | 0.6701 | 884,789.52 |
| Gradient Boosting | 1,138,218.50 | 0.6706 | 879,303.47 |
| XGBoost | 1,137,618.93 | 0.6709 | 867,479.96 |

### Best model

Based on the saved results, `Linear Regression` achieved the best overall performance:

- Best `R2`: `0.7014`
- Lowest `RMSE`: `1,083,668.23`
- Lowest `MAE`: `835,546.51`

### Interpretation

Although ensemble methods such as Random Forest, Gradient Boosting, and XGBoost are often powerful, in this project Linear Regression performed slightly better. This suggests that the relationship between the processed features and house price may be reasonably linear after encoding and outlier treatment.

The Decision Tree model performed worst among all tested models. This likely happened because a single decision tree can overfit the training data and generalize less effectively than boosted or averaged models.

## 9. Post-Model Analysis

Additional model analysis was performed in `08.Analysis.ipynb`.

This phase included:

- Bar charts comparing `R2`, `RMSE`, and `MAE`
- Actual vs predicted scatter plots
- Residual analysis
- Error behavior inspection for each model

These plots help visually confirm how close each model's predictions are to the true prices and whether prediction errors are balanced or patterned.

## 10. Conclusion

This project successfully built a complete machine learning pipeline for house price prediction. The workflow covered dataset preparation, exploratory analysis, feature engineering, model selection, evaluation, and visual comparison.

Among the five models tested, Linear Regression produced the strongest saved performance on the test set. This result shows that simpler models can still perform very well when the data is clean and preprocessing is effective.

Overall, the project demonstrates:

- A clear regression workflow
- Practical preprocessing for mixed-type housing data
- Comparative evaluation across multiple algorithms
- Reproducible storage of trained models and prediction outputs

## 11. Limitations

The project also has some limitations:

- The notebooks use hard-coded absolute Windows paths, which reduce portability
- The dataset is relatively small, with only 545 rows
- Feature engineering is limited to encoding and outlier treatment
- No deployment or end-user prediction interface is included
- The work is notebook-based rather than structured as reusable Python modules

## 12. Future Improvements

This project can be improved in several ways:

- Replace absolute paths with relative paths
- Add a `requirements.txt` file for reproducible setup
- Convert notebook logic into reusable scripts or modules
- Add feature importance and interpretability analysis
- Try additional regression methods and stacked ensembles
- Build a small application for predicting the price of a custom house entry

## 13. Files Produced by the Project

Important outputs generated in this project include:

- Dataset file in `data/Housing.csv`
- Processed feature file in `data/x.csv`
- Target file in `data/y.csv`
- Trained models in `models/`
- Prediction files in `models/predictions/`
- Evaluation summary in `models/model_results.csv`

## 14. Final Summary

This project shows that machine learning can be effectively applied to estimate house prices from housing characteristics. By comparing several regression models, the project identifies Linear Regression as the strongest saved performer on this dataset, while also demonstrating the value of preprocessing, hyperparameter tuning, and visual error analysis in a real-world prediction task.
