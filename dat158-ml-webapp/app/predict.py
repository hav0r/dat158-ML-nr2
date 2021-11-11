from typing import List
import joblib
import pandas as pd
import numpy as np

model = joblib.load('dat158-ml-webapp/models/rf_model.joblib')

def data_transformation_simple(data):
    
    if "index" in data.columns:
        data=data.drop("index",axis=1)
    if "Id" in data.columns:
        data=data.drop("Id",axis=1)
    if "SalePrice" in data.columns:
        labels = data["SalePrice"]
        data=data.drop("SalePrice",axis=1)
    else:
        labels=None
    unwanted=['MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street', 'Alley',
   'LotShape', 'LandContour', 'Utilities', 'LotConfig', 'LandSlope',
   'Neighborhood', 'Condition1', 'Condition2', 'BldgType', 'HouseStyle',
   'OverallCond', 'RoofStyle',
   'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType',
   'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond',
   'BsmtExposure', 'BsmtFinType1', 'BsmtFinSF1', 'BsmtFinType2',
   'BsmtFinSF2', 'BsmtUnfSF', 'Heating', 'HeatingQC',
   'CentralAir', 'Electrical', '2ndFlrSF', 'LowQualFinSF',
   'BsmtFullBath', 'BsmtHalfBath', 'HalfBath',
   'BedroomAbvGr', 'KitchenAbvGr', 'KitchenQual',
   'Functional', 'FireplaceQu', 'GarageType', 
   'GarageFinish', 'GarageQual', 'GarageCond',
   'PavedDrive', 'EnclosedPorch', '3SsnPorch',
   'ScreenPorch', 'PoolArea', 'PoolQC', 'Fence', 'MiscFeature', 'MiscVal',
   'MoSold', 'YrSold', 'SaleType', 'SaleCondition', 'saleprice_cat']
    for feat in unwanted:
        if feat in data.columns:
            data=data.drop(feat,axis=1)
    
    
    from sklearn.impute import SimpleImputer
    imputer = SimpleImputer(strategy="median")
    cat_imputer = SimpleImputer(strategy="most_frequent")

    data_num = data.select_dtypes(include=[np.number])
    
    data_imputed = imputer.fit_transform(data_num)
    
    features = list(data_num.columns)
    
    output = np.hstack([data_imputed])
    return output,labels,features
    
def predict(data):
    values = data

    column_order = ['OverallQual',
 'YearBuilt',
 'YearRemodAdd',
 'MasVnrArea',
 'TotalBsmtSF',
 'FirstFlrSF',
 'GrLivArea',
 'FullBath',
 'TotRmsAbvGrd',
 'Fireplaces',
 'GarageYrBlt',
 'GarageCars',
 'GarageArea',
 'WoodDeckSF',
 'OpenPorchSF']
    
    values = [values[feat] for feat in column_order]
    values = pd.DataFrame([list(values)],columns=[c for c in column_order])

    test_data, test_labels, test_features = data_transformation_simple(values)
    values = test_data
    pred = model.predict(values.reshape(1, -1))

    return pred[0]