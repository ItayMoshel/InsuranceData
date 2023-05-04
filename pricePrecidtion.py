import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

insurance_data = pd.read_csv('insurance.csv')

cat_cols = ['sex', 'smoker', 'region']
insurance_data = pd.get_dummies(insurance_data, columns=cat_cols)

X_train, X_test, y_train, y_test = train_test_split(
    insurance_data.drop(columns=['charges']), insurance_data['charges'], test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

new_customer = pd.DataFrame({
    'age': [65],
    'sex': ['male'],
    'bmi': [30],
    'children': [4],
    'smoker': ['yes'],
    'region': ['northeast']
})

new_customer = pd.get_dummies(new_customer, columns=cat_cols)
new_customer = new_customer.reindex(columns=X_train.columns, fill_value=0)  # add missing columns with default values
new_customer_scaled = scaler.transform(new_customer)
prediction = model.predict(new_customer_scaled)
prediction = max(prediction, 0)

print('Predicted insurance cost: $', prediction[0])
