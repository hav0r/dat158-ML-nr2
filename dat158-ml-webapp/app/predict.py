from typing import List
import joblib
import pandas as pd
import numpy as np

model = joblib.load('flask test/models/rf_model.joblib')

def get_form_data(data):

    feature_values = { 
'MSSubClass':20,
'LotFrontage':60.0,
'LotArea':7200,
'OverallQual':5,
'OverallCond':5,
'YearBuilt':2006,
'YearRemodAdd':1950,
'MasVnrArea':0.0,
'BsmtFinSF1':0,
'BsmtFinSF2':0,
'BsmtUnfSF':0,
'TotalBsmtSF':0,
'1stFlrSF':864,
'2ndFlrSF':0,
'LowQualFinSF':0,
'GrLivArea':864,
'BsmtFullBath':0,
'BsmtHalfBath':0,
'FullBath':2,
'HalfBath':0,
'BedroomAbvGr':3,
'KitchenAbvGr':1,
'TotRmsAbvGrd':6,
'Fireplaces':0,
'GarageYrBlt':2005.0,
'GarageCars':2,
'GarageArea':0,
'WoodDeckSF':0,
'OpenPorchSF':0,
'EnclosedPorch':0,
'3SsnPorch':0,
'ScreenPorch':0,
'PoolArea':0,
'MiscVal':0,
'MoSold':6,
'YrSold':2009,
'MSZoning':'RL',
'Street':'Pave',
'Alley':'Grvl',
'LotShape':'Reg',
'LandContour':'Lvl',
'Utilities':'AllPub',
'LotConfig':'Inside',
'LandSlope':'Gtl',
'Neighborhood':'NAmes',
'Condition1':'Norm',
'Condition2':'Norm',
'BldgType':'1Fam',
'HouseStyle':'1Story',
'RoofStyle':'Gable',
'RoofMatl':'CompShg',
'Exterior1st':'VinylSd',
'Exterior2nd':'VinylSd',
'MasVnrType':'None',
'ExterQual':'TA',
'ExterCond':'TA',
'Foundation':'PConc',
'BsmtQual':'TA',
'BsmtCond':'TA',
'BsmtExposure':'No',
'BsmtFinType1':'Unf',
'BsmtFinType2':'Unf',
'Heating':'GasA',
'HeatingQC':'Ex',
'CentralAir':'Y',
'Electrical':'SBrkr',
'KitchenQual':'TA',
'Functional':'Typ',
'FireplaceQu':'Gd',
'GarageType':'Attchd',
'GarageFinish':'Unf',
'GarageQual':'TA',
'GarageCond':'TA',
'PavedDrive':'Y',
'PoolQC':'Gd',
'Fence':'MnPrv',
'MiscFeature':'Shed',
'SaleType':'WD',
'SaleCondition':'Normal'
    }

    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]
        
    return feature_values

def get_form_data_simple(data):
    feature_values = {
    'OverallQual':5,
    'YearBuilt':2006,
    'TotalBsmtSF':0,
    'FullBath':2,
    'TotRmsAbvGrd':6,
    'GarageCars':2,
    'GarageArea':0
    }
    for key in [k for k in data.keys() if k in feature_values.keys()]:
        feature_values[key] = data[key]
    
    return feature_values

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