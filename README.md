# House Price Prediction

This project predicts house prices using a supervised machine learning workflow built around the Kaggle Housing Prices dataset. It covers dataset loading, exploratory data analysis, preprocessing, model training, and post-training comparison across several regression models.

## Project Overview

The repository uses the dataset from `yasserh/housing-prices-dataset` and evaluates multiple regression algorithms to estimate house prices from housing features such as area, bedrooms, bathrooms, stories, parking, and amenities.

## Repository Structure

```text
.
├── 00.dataset.py               # Downloads/loads the dataset with kagglehub
├── 01.data-exploration.ipynb   # Exploratory data analysis and visualizations
├── 02.preprocessing.ipynb      # Encoding, outlier handling, feature/target export
├── 03.Models.ipynb             # Model training, tuning, evaluation, model export
├── 08.Analysis.ipynb           # Model comparison charts and prediction diagnostics
├── data/
│   ├── Housing.csv             # Source dataset
│   ├── x.csv                   # Processed features
│   └── y.csv                   # Target column
└── models/
    ├── *.pkl                   # Trained models saved with joblib
    ├── model_results.csv       # Summary metrics for each model
    └── predictions/            # Actual vs predicted outputs per model
```

## Workflow

### 1. Dataset loading

`00.dataset.py` loads `Housing.csv` from Kaggle using `kagglehub`.

### 2. Data exploration

`01.data-exploration.ipynb` explores the dataset with:

- Price and area distributions
- Price vs area regression plot
- Price vs bedrooms and stories boxplots
- Correlation heatmap
- Categorical feature analysis
- Outlier inspection

### 3. Preprocessing

`02.preprocessing.ipynb` prepares the data by:

- Converting binary categorical fields from `yes/no` to `1/0`
- One-hot encoding `furnishingstatus`
- Capping outliers in `area` and `price` with the IQR method
- Exporting processed features to `data/x.csv`
- Exporting the target to `data/y.csv`

### 4. Model training

`03.Models.ipynb` trains and evaluates:

- Linear Regression with `MinMaxScaler` and `RFE`
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor
- XGBoost Regressor

Model tuning is performed with cross-validation using `GridSearchCV` or `RandomizedSearchCV`, and trained models are saved to the `models/` directory.

### 5. Analysis

`08.Analysis.ipynb` compares model performance and visualizes:

- R2, RMSE, and MAE comparison charts
- Actual vs predicted scatter plots
- Residual diagnostics
- Error distribution behavior by model

## Results

Current saved metrics from `models/model_results.csv`:

| Model | RMSE | R2 | MAE |
|---|---:|---:|---:|
| Linear Regression | 1,083,668.23 | 0.7014 | 835,546.51 |
| Decision Tree | 1,429,795.45 | 0.4802 | 1,109,590.81 |
| Random Forest | 1,138,949.52 | 0.6701 | 884,789.52 |
| Gradient Boosting | 1,138,218.50 | 0.6706 | 879,303.47 |
| XGBoost | 1,137,618.93 | 0.6709 | 867,479.96 |

Best result in the current saved run:

- Best `R2`: Linear Regression (`0.7014`)
- Best `RMSE`: Linear Regression (`1,083,668.23`)
- Best `MAE`: Linear Regression (`835,546.51`)

## Requirements

This project uses Python plus the following main libraries:

- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `statsmodels`
- `xgboost`
- `joblib`
- `kagglehub`
- `jupyter`

Example install command:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn statsmodels xgboost joblib kagglehub jupyter
```

## How to Run

### Option 1: Run the notebooks

Open Jupyter and run the files in this order:

1. `01.data-exploration.ipynb`
2. `02.preprocessing.ipynb`
3. `03.Models.ipynb`
4. `08.Analysis.ipynb`

### Option 2: Load the dataset script

```bash
python 00.dataset.py
```

## Important Note About Paths

Several notebooks use an absolute Windows path:

```python
DATA_DIR = "D:/Machine-Learning/HousePrice prediction/data"
```

If you move this project to a different location or run it on another machine, update that path or replace it with a relative path such as:

```python
DATA_DIR = "./data"
```

## Outputs

After running the project, you will have:

- Processed datasets in `data/`
- Trained model files in `models/`
- Prediction CSV files in `models/predictions/`
- Evaluation summary in `models/model_results.csv`

## Possible Improvements

- Replace hard-coded paths with relative paths everywhere
- Add a `requirements.txt` file for reproducible setup
- Convert notebook logic into reusable Python modules
- Add a prediction script for new custom house inputs
- Add feature importance plots and model interpretability notes

## Author

Machine learning project for house price prediction using regression models and comparative analysis.
