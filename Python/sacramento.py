import pandas as pd
import statsmodels.api as sm


def map_num_bathrooms_to_0_1(num_bathrooms: int) -> int:
    if num_bathrooms <= 1:
        return 0
    else:
        return 1


predict_house = pd.read_csv(
    "sacramento.csv"
)
predict_house["baths"] = predict_house["baths"].transform(map_num_bathrooms_to_0_1)

x = predict_house[["beds", "sqft", "price"]]
y = predict_house[["baths"]]

x = sm.add_constant(x)
logit_mod = sm.Logit(y, x)
mod= logit_mod.fit()

print(mod.params.round(2))
print(mod.pvalues.round(2))
print("The smallest p-value is for sqft")
