# Tip Prediction

##### Linear Regression Model for Tip Prediction

##### Project Description
This demonstrates a simple linear regression model to predict tip amounts based on the total bill. The goal is to analyze the relationship between the observed total bill and the observed tip amount, build a predictive model, and evaluate its performance.

##### Setup and Installation
To run this notebook, you need to have the following Python libraries installed. You can install them using pip:

```bash
pip install numpy pandas seaborn matplotlib scikit-learn openpyxl
```

### Data
The notebook expects an Excel file named `tip-amount.xlsx` to be present in the `/content/` directory of your Colab environment. This file should contain at least two columns: 'Observed total bill(xi)' and 'Observed tip amount(yi)'. An optional 'Meal' column is dropped during preprocessing.

## Code Overview
The notebook performs the following steps:

1.  **Library Imports**: Imports essential libraries for data manipulation, visualization, and machine learning.
2.  **Data Loading**: Loads the `tip-amount.xlsx` file into a pandas DataFrame.
3.  **Data Preprocessing**: Drops irrelevant columns ('Meal').
4.  **Correlation Analysis**: Calculates and displays the correlation matrix between the total bill and tip amount to understand their relationship.
5.  **Target Splitting**: Separates the features (total bill) from the target variable (tip amount).
6.  **Train-Test Split**: Divides the dataset into training and testing sets to ensure robust model evaluation.
7.  **Model Training**: Initializes and trains a `LinearRegression` model using the training data.
8.  **Prediction**: Uses the trained model to make predictions on the test set.
9.  **Model Evaluation**: Evaluates the model's performance using Mean Squared Error (MSE) and R-squared (R2) score.
10. **Individual Prediction**: Demonstrates how to use the model to predict the tip for a new, arbitrary bill amount (e.g., $50).

## Results
The output includes:
*   The head of the DataFrame after loading and preprocessing.
*   The correlation matrix.
*   Predicted tip amounts for the test set.
*   Mean Squared Error and R-squared score, indicating the model's accuracy.
*   A prediction for a $50 bill amount.
```

