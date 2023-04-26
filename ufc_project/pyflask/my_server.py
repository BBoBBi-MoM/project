#%%
from flask import Flask,request
from flask import render_template
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import joblib
import pandas as pd
import numpy as np

train_df = pd.read_csv('sample.csv')
input_df= train_df.iloc[0,:-1]
input_data = input_df.values.reshape(1,-1)
model = joblib.load('./best_model.pkl')

age_max = 47
age_min = 19
height_max = 210.82
height_min = 152.4
reach_max = 213.36
reach_min = 152.4
weight_max = 265
weight_min = 115


app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
      
        
        result = request.form
        blue_height = (int(request.form['b_height_input'])-height_min)/(height_max-height_min)
        red_height = (int(request.form['r_height_input'])-height_min)/(height_max-height_min)
        
        blue_reach = (int(request.form['b_reach_input'])-reach_min)/(reach_max-reach_min)
        red_reach = (int(request.form['r_reach_input'])-reach_min)/(reach_max-reach_min)
        
        blue_weight = (int(request.form['b_weight_input'])-weight_min)/(weight_max-weight_min)
        red_weight = (int(request.form['r_weight_input'])-weight_min)/(weight_max-weight_min)

        b_age = (int(request.form['b_age_input'])-age_min)/(age_max-age_min)
        r_age = (int(request.form['r_age_input'])-age_min)/(age_max-age_min)
        
        input_df['B_Height_cms']=blue_height
        input_df['R_Height_cms']=red_height
        
        input_df['B_Weight_lbs']=blue_weight
        input_df['R_Weight_lbs']=red_weight
        
        input_df['B_Reach_cms']=blue_reach
        input_df['R_Reach_cms']=red_reach
        
        input_df['B_age']=b_age
        input_df['R_age']=r_age

        input_data = input_df.values.reshape(1,-1)
        pred=model.predict(input_data)
        return render_template("result.html",
                                result=result,
                                d = input_data,
                                pred= pred.item()

                                )


    
if __name__ =='__main__':
    app.run()
# %%
