# Code you have previously used to load data
import pandas as pd

# Path of the file to read
iowa_file_path = '../input/home-data-for-ml-course/train.csv'

home_data = pd.read_csv(iowa_file_path)

# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex3 import *

print("Setup Complete")
# print the list of columns in the dataset to find the name of the prediction target
print(home_data.columns)
y = home_data.SalePrice
# Create the list of features below
feature_names = ["LotArea", "YearBuilt", "1stFlrSF", "2ndFlrSF","FullBath", "BedroomAbvGr", "TotRmsAbvGrd"]
# Select data corresponding to features in feature_names
X = home_data[feature_names]
#Review data
print(X)
#print description or statistics from X
#print(X.description)
print(_)
#print the top few lines
print(X.head)
#print(_)
# from _ import _
#specify the model. 
#For model reproducibility, set a numeric value for random_state when specifying the model
from sklearn.tree import DecisionTreeRegressor
iowa_model = DecisionTreeRegressor(random_state=1)
# Fit the model
iowa_model.fit(X, y)
predictions = iowa_model.predict(X)
print(predictions)
