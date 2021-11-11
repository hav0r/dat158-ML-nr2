from flask import sessions
from flask.app import iscoroutinefunction
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.fields.core import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange



class DataForm(FlaskForm):
    # MSSubClass=IntegerField('MSSubClass')
    # MSZoning=SelectField('MSZoning',choices=['NaN', 'FV', 'RH', 'RM', 'C (all)', 'RL'])
    # LotFrontage=FloatField('LotFrontage')
    # Street=SelectField('Street',choices=['NaN', 'Pave', 'Grvl'])
    # #dropper Alley fordi 91 av 1400 er ikke nan
    # LotShape=SelectField("LotShape",choices=['NaN', 'IR2', 'IR1', 'IR3', 'Reg'])
    # LandContour=SelectField("LandContour",choices=['NaN', 'Bnk', 'Low', 'HLS', 'Lvl'])
    # Utilities=SelectField("Utilities",choices=['NaN', 'AllPub', 'NoSeWa'])
    # LotConfig=SelectField("LotConfig",choices=['NaN', 'FR2', 'FR3', 'Inside', 'Corner', 'CulDSac'])
    # LandSlope=SelectField("LandSlope",choices=['NaN', 'Mod', 'Sev', 'Gtl'])
    # Neighborhood=SelectField("Neighborhood",choices=['NaN', 'Blueste',
    #                                                 'Crawfor',
    #                                                 'OldTown',
    #                                                 'Veenker',
    #                                                 'Mitchel',
    #                                                 'NWAmes',
    #                                                 'Blmngtn',
    #                                                 'BrDale',
    #                                                 'NAmes',
    #                                                 'MeadowV',
    #                                                 'CollgCr',
    #                                                 'BrkSide',
    #                                                 'NridgHt',
    #                                                 'Somerst',
    #                                                 'Timber',
    #                                                 'IDOTRR',
    #                                                 'NoRidge',
    #                                                 'Edwards',
    #                                                 'Gilbert',
    #                                                 'SWISU',
    #                                                 'StoneBr',
    #                                                 'NPkVill',
    #                                                 'Sawyer',
    #                                                 'ClearCr',
    #                                                 'SawyerW'])
    # Condition1=SelectField("Condition1",choices=['NaN', 'RRAn', 'Feedr', 'PosA', 'Norm', 'RRNe', 'RRNn', 'PosN', 'RRAe', 'Artery'])
    # Condition2=SelectField("Condition2",choices=['NaN', 'RRAn', 'Feedr', 'PosA', 'Norm', 'RRNn', 'PosN', 'RRAe', 'Artery'])
    # BldgType=SelectField("BldgType",choices=['NaN', 'TwnhsE', 'Twnhs', '1Fam', 'Duplex', '2fmCon'])
    # HouseStyle=SelectField("HouseStyle",choices=['NaN', 'SFoyer', 'SLvl', '2.5Unf', '2Story', '1.5Fin', '1Story', '1.5Unf', '2.5Fin'])
    OverallQual=IntegerField("Overall quality of the house(1-10)",validators=[NumberRange(min=0,max=10)])
    #OverallCond=SelectField("OverallCond",choices=['NaN', 1, 2, 3, 4, 5, 6, 7, 8, 9])
    YearBuilt=IntegerField("Year the house was built")
    YearRemodAdd=IntegerField("YearRemodAdd")
    # RoofStyle=SelectField("RoofStyle",choices=['NaN', 'Mansard', 'Shed', 'Flat', 'Gable', 'Gambrel', 'Hip'])
    # RoofMatl=SelectField("RoofMatl",choices=['NaN', 'Membran','CompShg', 'ClyTile', 'WdShngl', 'Roll', 'WdShake', 'Metal', 'Tar&Grv'])
    # Exterior1st=SelectField("Exterior1st",choices=['NaN', 'BrkComm', 'CBlock', 'HdBoard', 'Stucco', 'VinylSd', 'CemntBd', 'Plywood', 'Stone', 'BrkFace', 'AsphShn', 'AsbShng', 'MetalSd', 'WdShing', 'Wd Sdng', 'ImStucc'])
    # Exterior2nd=SelectField("Exterior2nd",choices=['NaN', 'CBlock', 'HdBoard', 'Wd Shng', 'Other', 'Stucco', 'VinylSd', 'Plywood', 'Brk Cmn', 'Stone', 'BrkFace', 'AsbShng', 'CmentBd', 'MetalSd', 'AsphShn', 'Wd Sdng', 'ImStucc'])
    #MasVnrType=SelectField("MasVnrType",choices=['NaN', 'BrkCmn', 'Stone', 'BrkFace', 'None'])
    MasVnrArea=FloatField("MasVnrArea")
    # ExterQual=SelectField("ExterQual",choices=['NaN', 'Gd', 'Fa', 'Ex', 'TA'])
    # ExterCond=SelectField("ExterCond",choices=['NaN', 'Fa', 'Ex', 'TA', 'Gd', 'Po'])
    # Foundation=SelectField("Foundation",choices=['NaN', 'Slab', 'Wood', 'Stone', 'PConc', 'BrkTil', 'CBlock'])  
    # BsmtQual=SelectField("BsmtQual",choices=['NaN', 'Fa', 'Ex', 'Gd', 'TA'])
    # BsmtExposure=SelectField("BsmtExposure",choices=['NaN', 'Mn', 'Gd', 'No', 'Av'])
    # BsmtFinType1=SelectField("BsmtFinType1",choices=['NaN', 'Rec', 'Unf', 'GLQ', 'ALQ', 'LwQ', 'BLQ'])
    # BsmtFinSF1=IntegerField("BsmtFinSF1")
    # BsmtFinType2=SelectField("BsmtFinType2",choices=['NaN', 'Rec', 'Unf', 'GLQ', 'ALQ', 'LwQ', 'BLQ'])
    # BsmtFinSF2=IntegerField("BsmtFinSF2")
    # BsmtUnfSF=IntegerField("BsmtUnfSF")
    TotalBsmtSF=IntegerField("Total basement square footage")
    # Heating=SelectField("Heating",choices=['NaN', 'OthW', 'Grav', 'GasW', 'GasA', 'Wall', 'Floor'])
    # HeatingQC=SelectField("HeatingQC",choices=['NaN', 'Fa', 'Ex', 'Gd', 'TA', 'Po'])
    # CentralAir=SelectField("CentralAir",choices=['NaN', 'N', 'Y'])
    # Electrical=SelectField("Electrical",choices=['NaN', 'FuseF', 'Mix', 'FuseA', 'FuseP', 'SBrkr'])
    FirstFlrSF=IntegerField("1stFlrSF")
    # SecondFlrSF=IntegerField("Second Floor square footage")
    # LowQualFinSF=IntegerField("LowQualFinSF")
    GrLivArea=IntegerField("GrLivArea")
    # BsmtFullBath=IntegerField("BsmtFullBath")
    # BsmtHalfBath=IntegerField("BsmtHalfBath")
    FullBath=IntegerField("Number of full bathrooms in the house")
    # HalfBath=IntegerField("HalfBath")
    # BedroomAbvGr=IntegerField("BedroomAbvGr")
    # KitchenAbvGr=IntegerField("KitchenAbvGr")
    # KitchenQual=SelectField("KitchenQual",choices=['NaN', 'Gd', 'Fa', 'Ex', 'TA'])
    TotRmsAbvGrd=IntegerField("Total rooms above ground")
    # Functional=SelectField("Functional",choices=['NaN', 'Min1', 'Typ', 'Sev', 'Maj1', 'Maj2', 'Mod', 'Min2'])
    Fireplaces=IntegerField("Fireplaces")
    # FireplaceQu=SelectField("FireplaceQu",choices=['NaN', 'Fa', 'Ex', 'Gd', 'TA', 'Po'])
    # GarageType=SelectField("GarageType",choices=['NaN', '2Types', 'BuiltIn', 'Detchd', 'Attchd', 'CarPort', 'Basment'])
    GarageYrBlt=IntegerField("GarageYrBlt")
    # GarageFinish=SelectField("GarageFinish",choices=['NaN', 'Fin', 'RFn', 'Unf'])
    GarageCars=IntegerField("Amount of possible cars in garage")
    GarageArea=IntegerField("Garage area")
    # GarageQual=SelectField("GarageQual",choices=['NaN', 'Fa', 'Ex', 'TA', 'Gd', 'Po'])
    # GarageCond=SelectField("GarageCond",choices=['NaN', 'Fa', 'Ex', 'TA', 'Gd', 'Po'])
    # PavedDrive=SelectField("PavedDrive",choices=['NaN', 'N', 'Y', 'P'])
    WoodDeckSF=IntegerField("WoodDeckSF")
    OpenPorchSF=IntegerField("OpenPorchSF")
    # EnclosedPorch=IntegerField("EnclosedPorch")
    # ThreeSsnPorch=IntegerField("3SsnPorch")
    # ScreenPorch=IntegerField("ScreenPorch")
    # PoolArea=IntegerField("PoolArea")
    # PoolQC=SelectField("PoolQC",choices=['NaN', 'Fa', 'Ex', 'Gd'])
    # Fence=SelectField("Fence",choices=['NaN', 'MnPrv', 'GdPrv', 'GdWo', 'MnWw'])
    # MiscFeature=SelectField("MiscFeature",choices=['NaN', 'Othr', 'TenC', 'Shed', 'Gar2'])
    # MiscVal=IntegerField("MiscVal")
    # MoSold=SelectField("MoSold",choices=['NaN', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # YrSold=IntegerField("YrSold")
    # SaleType=SelectField("SaleType",choices=['NaN', 'CWD', 'ConLI', 'COD', 'ConLw', 'New', 'Con', 'Oth', 'ConLD', 'WD'])
    # SaleCondition=SelectField("SaleCondition",choices=['NaN', 'AdjLand', 'Normal', 'Partial', 'Abnorml', 'Alloca', 'Family'])

    
    submit = SubmitField("Send inn")