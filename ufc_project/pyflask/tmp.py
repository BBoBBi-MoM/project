#%%
from flask import Flask,request
from flask import render_template
from sklearn.ensemble import GradientBoostingClassifier
import pickle
import joblib

model = joblib.load('./best_model.pkl')
# %%
