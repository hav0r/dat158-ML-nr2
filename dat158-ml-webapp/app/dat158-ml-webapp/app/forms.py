from flask import sessions
from flask.app import iscoroutinefunction
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.fields.core import FloatField, SelectField
from wtforms.validators import DataRequired, NumberRange



class DataForm(FlaskForm):
    OverallQual=IntegerField("Overall quality of the house(1-10)",validators=[NumberRange(min=0,max=10)])
    YearBuilt=IntegerField("Year the house was built")
    YearRemodAdd=IntegerField("YearRemodAdd")
    MasVnrArea=FloatField("MasVnrArea")
    TotalBsmtSF=IntegerField("Total basement square footage")
    FirstFlrSF=IntegerField("1stFlrSF")
    GrLivArea=IntegerField("GrLivArea")
    FullBath=IntegerField("Number of full bathrooms in the house")
    TotRmsAbvGrd=IntegerField("Total rooms above ground")
    Fireplaces=IntegerField("Fireplaces")
    GarageYrBlt=IntegerField("GarageYrBlt")
    GarageCars=IntegerField("Amount of possible cars in garage")
    GarageArea=IntegerField("Garage area")
    WoodDeckSF=IntegerField("WoodDeckSF")
    OpenPorchSF=IntegerField("OpenPorchSF")

    submit = SubmitField("Send inn")