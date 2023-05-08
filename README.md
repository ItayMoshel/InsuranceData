# InsuranceData

This is a Django based API that uses a machine learning model to predict the cost of insurance for a given customer.
Users can input customer data and the application returns a fair price based on a dataset with more than 1300 pieces of
data that contains varius attributes such as age, sex, BMI, number of children, smoker status, region, and insurance
charges.  
This dataset is useful for analyzing the factors that affect medical insurance costs and for building predictive models
to estimate the insurance costs of individuals based on their attributes.

## Usage

This application has been deployed to PythonAnywhere, and can be accessed
at http://itaymoshel.pythonanywhere.com/customers/.

## Usage (local)

To use the web interface, open a web browser and navigate to http://localhost:8000/customers/.  
Here, you can input customer data and get a predicted insurance cost.  
To use the API, you can send a POST request to http://localhost:8000/customers/ with customer data in the request body
like the following:

```
{
    "age": 18,
    "sex": "male",
    "bmi": 16,
    "children": 0,
    "smoker": "no",
    "region": "northeast"
}
```  

The API will return a JSON object with the predicted cost:

```commandline
{
    "id": 1,
    "age": 18,
    "sex": "male",
    "bmi": 16.0,
    "children": 0,
    "smoker": "no",
    "region": "northeast",
    "predicted_price": 1626.89
}
```

## Installation

To install and run the application:

1. Clone the repository: `git clone https://github.com/ItayMoshel/InsuranceData.git`
2. Install the required packages: pip install -r requirements.txt
3. Run the application: python manage.py runserver




