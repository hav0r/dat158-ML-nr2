from pandas.io.stata import precision_loss_doc
from app import app
from flask import render_template, session, redirect, url_for
from app.forms import DataForm
from app.predict import predict
import pickle

app.config['SECRET_KEY']='HALVOR'

@app.route('/',methods=['GET','POST'])
@app.route('/index',methods=['GET','POST'])

def index():
    
    form = DataForm()

    if form.validate_on_submit():
        for fieldname, value in form.data.items():
            session[fieldname] = value
        session['prediction'] = predict(session)
        return redirect(url_for('index'))

    return render_template('index.html',form=form)