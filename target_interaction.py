import pandas as pd

df = pd.read_csv("dataset.csv")

def check_interaction(drug, target):

    result = df[(df["Drug"].str.lower() == drug.lower()) & (df["Target"].str.lower() == target.lower())]
    if not result.empty:
        interaction = result.iloc[0]
        return f"Found, Type: {interaction["Type"]}"
    else:
        return "Not Found"

drug = str(input("Enter Drug: "))
target = str(input("Enter Target: "))
print(check_interaction(drug,target))
