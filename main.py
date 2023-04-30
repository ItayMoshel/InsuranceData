import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('insurance.csv')
df_shape = df.shape

print(f"{df_shape[0]} rows and {df_shape[1]} columns in this dataset.")

print()

for col in df:
    print(f"{col} count: {df[col].count()}")

print()

for col in df:
    print(f"{col} unique values: {df[col].nunique()}")

print()

for col in df:
    print(f"{col} data type: {df[col].dtype}")

print()

for col in df:
    print(f"number of missing data for {col} column: {df[col].isnull().sum()}")

print()

print(f"Minimum of charges: {df.charges.min()}")
print(f"Low 25% of charges: {df.charges.quantile(.25)}")
print(f"Low 50% of charges: {df.charges.quantile(.50)}")
print(f"Low 75% of charges: {df.charges.quantile(.75)}")
print(f"Mean: {df.charges.mean()}")
print(f"Median: {df.charges.median()}")
print(f"Mode: {df.charges.mode().values[0]}")
print(f"Maximum of charges: {df.charges.max()}")

print()

print(f"Standard deviation: {df.charges.std()}")
print(f"Skewness: {df.charges.skew()}")
print(f"Kurtosis: {df.charges.kurt()}")

corr_df = pd.DataFrame(columns=['r', 'p'])
for col in df:
    if pd.api.types.is_numeric_dtype(df[col]) and col != "charges":
        r, p = stats.pearsonr(df.charges, df[col])
        corr_df.loc[col] = [round(r, 3), round(p, 3)]

print(corr_df)

df_smoker = df[df['smoker'] == 'yes'].sample(200)
df_nonsmoker = df[df['smoker'] == 'no'].sample(200)
m, b, r, p, err = stats.linregress(df.age, df.charges)
x = range(18, 65)
y = m * x + b

plt.plot(x, y, color='black')
plt.scatter(df_smoker.age, df_smoker.charges, label='Smokers', marker='^')
plt.scatter(df_nonsmoker.age, df_nonsmoker.charges, label='Non-smokers', marker='o')
plt.title('Insurance Age versus Charges')
plt.xlabel('Age')
plt.ylabel('Charges')
plt.legend()
plt.show()
