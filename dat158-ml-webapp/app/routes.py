from matplotlib.figure import Figure
from pandas.io.stata import precision_loss_doc
from werkzeug.utils import send_file
from app import app, cache
from flask import render_template, session, redirect, url_for
from app.forms import DataForm
from app.predict import predict
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
import base64


app.config['SECRET_KEY']='HALVOR'

@app.route('/predict_page',methods=['GET','POST'])

def predict_page():
    
    form = DataForm()

    if form.validate_on_submit():
        for fieldname, value in form.data.items():
            session[fieldname] = value
        session['prediction'] = predict(session)
        return redirect(url_for('predict_page'))

    return render_template('predict_page.html',form=form)
    
@app.route('/',methods=['GET'])
@app.route('/home',methods=['GET'])

def home():
    return render_template('home.html')



# def explore_page():

#     return render_template('explore_page.html', name = heatmap)

@app.route('/explore_page',methods=['GET'])
@cache.cached(timeout=50)
def explore_page():
    train = pd.read_csv('dat158-ml-webapp/data/train.csv')

    unwanted=['Id','index','saleprice_cat']
    for feat in unwanted:
        if feat in train.columns:
            train=train.drop(feat,axis=1)

    f,ax = plt.subplots(figsize=(11,9))
    data = train['OverallQual']
    ax.hist(data)
    canvas=FigureCanvas(f)
    img = io.BytesIO()
    plt.xlabel('Quality (1-10)')
    plt.ylabel('Houses')
    plt.grid(True)
    plt.savefig(img)
    plt.close()
    img.seek(0)
    plot0_url = base64.b64encode(img.getvalue()).decode('utf8')

    corr = train.corr()
    mask = np.triu(np.ones_like(corr,dtype=bool))
    f,ax = plt.subplots(figsize=(11,11))
    cmap = sns.diverging_palette(230,20,as_cmap=True)
    heatmap = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1,center=0,square=True, linewidths=.5,cbar_kws={"shrink":.5})
    canvas=FigureCanvas(f)
    img = io.BytesIO()
    plt.savefig(img)
    plt.close()
    img.seek(0)
    plot1_url = base64.b64encode(img.getvalue()).decode('utf8')
    return render_template('explore_page.html',plot0_url=plot0_url, plot1_url=plot1_url)