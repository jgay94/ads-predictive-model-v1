# ads-predictive-model-v1
 Helps identify what is best for a given product based on the historical data. 

## RUN
Download the repository and unzip it.

In your terminal, run the following commands:
```
cd src
```
Then:
```
python main.py
```

## OUTPUT
```
                            OLS Regression Results                            
==============================================================================
Dep. Variable:                   CM $   R-squared:                       0.839
Model:                            OLS   Adj. R-squared:                  0.838
Method:                 Least Squares   F-statistic:                     868.6
Date:                Wed, 28 Jun 2023   Prob (F-statistic):          8.18e-198
Time:                        08:05:04   Log-Likelihood:                -5255.5
No. Observations:                 504   AIC:                         1.052e+04
Df Residuals:                     500   BIC:                         1.054e+04
Df Model:                           3                                         
Covariance Type:            nonrobust                                         
=======================================================================================
                          coef    std err          t      P>|t|      [0.025      0.975]
---------------------------------------------------------------------------------------
const                2218.4080    490.609      4.522      0.000    1254.499    3182.317
Gross Revenue           0.1840      0.004     41.726      0.000       0.175       0.193
Promotion Expense      -0.6399      0.057    -11.310      0.000      -0.751      -0.529
Advertising Expense     0.3072      0.187      1.641      0.102      -0.061       0.675
==============================================================================
Omnibus:                      199.580   Durbin-Watson:                   2.226
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             2268.621
Skew:                          -1.391   Prob(JB):                         0.00
Kurtosis:                      13.014   Cond. No.                     1.85e+05
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.85e+05. This might indicate that there are
strong multicollinearity or other numerical problems.
```