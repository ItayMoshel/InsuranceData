from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import pandas as pd


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        insurance_data = pd.read_csv(
            r'/Users/itay/PycharmProjects/InsuranceData/InsurancePrice/PricePrediction/insurance.csv')

        cat_cols = ['sex', 'smoker', 'region']
        insurance_data = pd.get_dummies(insurance_data, columns=cat_cols)

        X_train = insurance_data.drop(columns=['charges'])
        y_train = insurance_data['charges']

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train_scaled, y_train)

        request_data = request.data

        new_customer = pd.DataFrame(request_data, index=[0])
        new_customer = pd.get_dummies(new_customer, columns=cat_cols)
        new_customer = new_customer.reindex(columns=X_train.columns,
                                            fill_value=0)
        new_customer_scaled = scaler.transform(new_customer)
        prediction = model.predict(new_customer_scaled)[0]
        prediction = max(prediction, 0)

        customer = Customer.objects.create(
            age=request_data['age'],
            sex=request_data['sex'],
            bmi=request_data['bmi'],
            children=request_data['children'],
            smoker=request_data['smoker'],
            region=request_data['region'],
            predicted_price=prediction
        )

        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
