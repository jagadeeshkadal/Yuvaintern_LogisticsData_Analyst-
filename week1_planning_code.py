# Week 1 illustrative Python workflow
# Actual LaDe-D column names and selected subset will be confirmed in Week 2.

import pandas as pd

df = pd.read_csv("data/raw/lade_delivery_subset.csv")

print(df.shape)
print(df.columns.tolist())
print(df.info())
print(df.isna().sum().sort_values(ascending=False).head(10))

# After confirming the timestamp semantics:
df["accept_time"] = pd.to_datetime(df["accept_time"], errors="coerce")
df["delivery_time"] = pd.to_datetime(df["delivery_time"], errors="coerce")

df["delivery_duration_min"] = (
    df["delivery_time"] - df["accept_time"]
).dt.total_seconds() / 60

print(df["delivery_duration_min"].describe())
