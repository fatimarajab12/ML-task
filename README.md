# PPV Prediction Project

This project aims to predict the **PPV** value using machine learning techniques with the PyCaret library. The dataset includes several features such as `Gender`, `Age`, `Dur`, and the target variable `PPV`. The primary goal is to create a robust regression model to accurately predict the `PPV` value.

---

## **Project Steps**

### 1. Data Preprocessing
- The dataset is loaded from an Excel file.
- The `Gender` column is encoded into numerical format:
  - `Male` → `1`
  - `Female` → `0`
- Missing values and duplicates are checked and addressed.
- The correlation between features and the target variable is calculated.

### 2. Data Visualization
- Visualizations are created using **Seaborn** to understand data distribution and feature relationships:
  - Histograms for `Age`, `Dur`, and `Gender`.
  - KDE plots to visualize density.
  - Correlation matrix to evaluate relationships between variables.

### 3. Model Building
- PyCaret is used to streamline the model-building process.
- The data is split into:
  - **Features** (`Gender`, `Age`, `Dur`)
  - **Target Variable** (`PPV`)
- PyCaret's `setup` function is used to prepare the data, normalize it, and enable reproducibility.

### 4. Model Comparison
- Various regression models are compared using PyCaret's `compare_models` function.
- The best model is selected based on:
  - R² (coefficient of determination)
  - RMSE (Root Mean Squared Error)

### 5. Model Tuning
- The selected model's hyperparameters are tuned using PyCaret's `tune_model` function.

### 6. Model Evaluation
- Cross-validation is performed to assess the stability and generalization of the tuned model.
- Evaluation metrics include:
  - **RMSE**: Measures the average error magnitude.
  - **MAE**: Measures the average absolute error.

### 7. Model Saving
- The final, tuned model is saved for future use with PyCaret's `save_model` function.

---

## **Requirements**
1. Python 3.x
2. Libraries:
   - `pandas`
   - `seaborn`
   - `pycaret`
   - `openpyxl`
3. Dataset: `TG_T_CashValues_Rel (2).xlsx`

---

## **How to Run the Code**

1. **Install Dependencies**
   Ensure you have Python and the following libraries installed:
   ```bash
   pip install pandas seaborn pycaret openpyxl
   ```

2. **Run the Script**
   - If using a Jupyter Notebook, open and run the notebook file (`PPV_Prediction.ipynb`).
   - If using a Python script, execute the file in your terminal:
     ```bash
     python ppv_model.py
     ```

3. **Output**
   - The script outputs the best-performing model, evaluation metrics, and a saved model file named `best_model.pkl`.

---

## **Files Included**
- `PPV_Prediction.ipynb` or `ppv_model.py`: The main script for the project.
- `TG_T_CashValues_Rel (2).xlsx`: The dataset used for training the model.
- `README.md`: Documentation for the project.
- `best_model.pkl`: The saved trained model.

---

## **Justification for Chosen Model**
The model was chosen based on its performance on key evaluation metrics such as R² and RMSE. After hyperparameter tuning, the model's performance improved significantly, making it the most suitable choice for predicting the PPV value.

---

## **Team Members**
- **Fatima Rajab**
- **Shahd Orr**
- **Ameen Shalabi**

---

## **Author**
Fatima Rajab and Team  
**Date**: December 2024
