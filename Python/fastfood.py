import pandas as pd
import statsmodels.api as sm

predict_calories = pd.read_csv("fastfood.csv")

X = predict_calories[["total_fat", "sat_fat", "cholesterol", "sodium"]]
Y = predict_calories[["calories"]]

X = sm.add_constant(X)

sm_model = sm.OLS(Y, X)

model = sm_model.fit()

print(model.mse_total.round(2))
print(model.rsquared.round(2))
print(model.params.round(2))
print(model.pvalues.round(2))
