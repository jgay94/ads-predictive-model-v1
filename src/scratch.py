import pandas as pd
import numpy as np
import statsmodels.api as sm 
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.metrics import r2_score

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

# Function to identify "hot" products based on defined criteria
def is_hot_product(trend, seasonal, cm):
    # Dummy criteria for illustrative purposes
    if trend > 0 and abs(seasonal) < 0.05 and cm.mean() > 5000:
        return True
    else:
        return False

# Load data
df = pd.read_csv('../data/data.csv')

# Print DataFrame columns
print(df.columns)

# Get list of departments
departments = df["Department"].unique()

for department in departments:
    # Select data for current department
    department_df = df[df["Department"] == department]

    # Each department has its own time-series data. Reshape the data for each department.
    department_df = department_df.melt(
       id_vars="Department", var_name="Week", value_vars=df.columns[1:]
    )

    # Extract Gross Revenue, Promotion Expense, Advertising Expense, and CM $ into separate columns
    # department_df["GrossRevenue"] = department_df["value"].apply(lambda x: x[0])
    # department_df["PromotionExpense"] = department_df["value"].apply(lambda x: x[1])
    # department_df["AdvertisingExpense"] = department_df["value"].apply(lambda x: x[2])
    # department_df["CM$"] = department_df["value"].apply(lambda x: x[3])

    department_df = department_df.drop("value", axis=1)

    # Preprocess data
    department_df = department_df.dropna()  # remove rows with missing values

    # Define independent variables (X) and dependent variable (y)
    X = department_df[["AdvertisingExpense", "PromotionExpense", "GrossRevenue"]]

    y = department_df["CM$"]

    # Calculate correlation coefficients and categorize them
    correlation = department_df.corr()

    correlation["CM$"] = correlation["CM$"].apply(categorize_coefficient)

    print(f"Correlation for {department}:\n", correlation["CM$"])

    # Add a constant to the independent value
    X = sm.add_constant(X)

    # Split data in a time-based manner
    train_size = int(len(department_df) * 0.8)

    X_train, X_test = X[:train_size], X[train_size:]

    y_train, y_test = y[:train_size], y[train_size:]

    # Create an OLS model
    model = sm.OLS(y_train, X_train)

    # Fit the model
    results = model.fit()

    # Print out the coefficients
    coeff_df = pd.DataFrame(results.params, columns=["Coefficient"])

    print(f"Coefficients for {department}:\n", coeff_df)

    # Predict y for the test set
    y_pred = results.predict(X_test)

    # Calculate and print R-squared for test set
    print("R-squared for test data for {department}:", r2_score(y_test, y_pred))

    # Seasonality detection using seasonal decomposition
    decomposition = seasonal_decompose(y, model="additive", period=1)

    # Identify if it's a "hot" product or not
    hot_product = is_hot_product(
        decomposition.trend.dropna(), decomposition.seasonal, department_df["CM$"]
    )

    print(f"Is {department} a hot product? ", hot_product)
