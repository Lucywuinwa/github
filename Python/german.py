import pandas as pd
import statsmodels.api as sm

predict_credit = pd.read_csv("german_credit_data.csv")

X = predict_credit[["Age", "Duration"]]
Y = predict_credit[["Credit amount"]]
predict_credit.rename(columns={"Credit amount": "Credit_amount"},inplace=True)

X = sm.add_constant(X)

sm_model = sm.OLS(Y,X)
model = sm_model.fit()

print(model.params.round(2))
print(model.rsquared.round(2))