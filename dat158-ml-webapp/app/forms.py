from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.fields.core import FloatField
from wtforms.validators import NumberRange



class DataForm(FlaskForm):
    OverallQual=IntegerField("Overall quality of the house(1-10)",validators=[NumberRange(min=0,max=10)])
    YearBuilt=IntegerField("Year the house was built")
    YearRemodAdd=IntegerField("Year remodeled")
    MasVnrArea=FloatField("MasVnrArea")
    TotalBsmtSF=IntegerField("Total basement square footage")
    FirstFlrSF=IntegerField("First floor square footage")
    GrLivArea=IntegerField("Ground living area")
    FullBath=IntegerField("Number of full bathrooms in the house")
    TotRmsAbvGrd=IntegerField("Total rooms above ground")
    Fireplaces=IntegerField("Fireplaces")
    GarageYrBlt=IntegerField("Garage year built")
    GarageCars=IntegerField("Amount of possible cars in garage")
    GarageArea=IntegerField("Garage area")
    WoodDeckSF=IntegerField("Wood deck square footage")
    OpenPorchSF=IntegerField("Open porch square footage")

    submit = SubmitField("Send inn")