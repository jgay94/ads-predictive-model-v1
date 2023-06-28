# Step 1: Import dependencies
import pandas as pd
import numpy as np
import statsmodels.api as sm

# Step 2: Load data & log the DataFrame to make sure it's loaded correctly
df = pd.read_csv('../data/data.csv')
print(df.head())

# Compute and print the correlation matrix
corr_matrix = df.select_dtypes(include=[np.number]).corr()
print(corr_matrix)

# Function to categorize correlation coefficient
def categorize_coefficient(coef):
    if abs(coef) > 0.7:
        return "High"
    elif abs(coef) > 0.5:
        return "Medium High"
    elif abs(coef) > 0.3:
        return "Medium"
    elif abs(coef) > 0.1:
        return "Medium Low"
    else:
        return "Low"

# Apply the function to the correlation matrix
categorized_corr_matrix = corr_matrix.applymap(categorize_coefficient)
print(categorized_corr_matrix)

# Convert the 'Date' column to a datetime object and then set it as the index of the DataFrame.
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# Set 'Gross Revenue', 'Promotion Expense', and 'Advertising Expense' as independent variables.
X = df[['Gross Revenue', 'Promotion Expense', 'Advertising Expense']]
Y = df['CM $']
X = sm.add_constant(X) # adding a constant (intercept term) to the model

# Fit the model and print the summary
model = sm.OLS(Y, X).fit()
print(model.summary())

# This function calculates the predicted contribution margin (CM) based on advertising and promotion expenses.
def predict_cm(advertising_expense, promotion_expense):
    """    
    Parameters:
    advertising_expense (float): The amount of money spent on advertising.
    promotion_expense (float): The amount of money spent on promotions.

    Returns:
    predicted_cm (float): The predicted contribution margin.
    """
    # Coefficients from the model
    coef_advertising = 0.3072
    coef_promotion = -0.6399
    intercept = 2218.4080

    predicted_cm = coef_advertising * advertising_expense + coef_promotion * promotion_expense + intercept

    return predicted_cm

advertising_expense = 3126.5279  # Replace with actual value
promotion_expense = 57.97  # Replace with actual value

predicted_cm = predict_cm(advertising_expense, promotion_expense)
print(f"The predicted Contribution Margin for Advertising Expense of {advertising_expense} and Promotion Expense of {promotion_expense} is {predicted_cm}")
