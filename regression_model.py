{
 "cells": [
  {
   "metadata": {},
   "cell_type": "raw",
   "source": [
    "import pandas as pd\n",
    "from pycaret.regression import *\n",
    "\n",
    "# Load the dataset\n",
    "data = pd.read_excel(\"TG_T_CashValues_Rel (2).xlsx\")\n",
    "\n",
    "# Basic exploration\n",
    "print(data.head())\n",
    "print(data.info())\n",
    "\n",
    "# Initialize the PyCaret regression setup\n",
    "setup(\n",
    "    data=data,\n",
    "    target='PPV',\n",
    "    categorical_features=['Gender'],  # Specify categorical columns\n",
    "    numeric_features=['Age', 'Dur'],  # Specify numeric columns\n",
    "    session_id=123                   # Set a seed for reproducibility\n",
    ")\n",
    "# Compare models and choose the best one based on RMSE\n",
    "best_model = compare_models(sort='RMSE')\n",
    "\n",
    "rf_model = create_model('rf')  # Train a Random Forest model\n",
    "tuned_rf_model = tune_model(rf_model)  # Hyperparameter tuning\n",
    "# Evaluate the tuned model\n",
    "evaluate_model(tuned_rf_model)\n",
    "\n",
    "# Predict on unseen data\n",
    "predictions = predict_model(tuned_rf_model)\n",
    "print(predictions.head())\n"
   ],
   "id": "eb083f40df69cf31"
  }
 ],
 "metadata": {},
 "nbformat": 5,
 "nbformat_minor": 9
}
