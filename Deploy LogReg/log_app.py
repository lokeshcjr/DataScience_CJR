import pandas as pd
import numpy as np
from pickle import load
import streamlit as st
 
st.title('Logistic Regression Model')

st.sidebar.write('Enter Passanger Details')

def create_page():
	pclass = st.sidebar.radio('Passanger Calss :' ,[1,2,3])
	sex=st.selectbox('Select Sex',[0,1])
	age=st.number_input('Enter age : ')
	sibsp=st.number_input(' Enter no.of sibblings or spouse : ')
	parch=st.number_input('Enter no parents or children : ')
	fare=st.number_input('Enter Fare : ')
	embarked=st.selectbox('Place of pickup : ',[0,1,2])
	
	data = {'Pclass':pclass,
	'Sex':sex,
	'Age':age,
	'SibSp':sibsp,
	'Parch':parch,
	'Fare':fare,
	'Embarked':embarked
	}

	df=pd.DataFrame(data, index=[0])
	return df
features=create_page()

if st.button('Submit'):
	st.write(features)

loaded_model=load(open('Logreg.pkl','rb'))
res=loaded_model.predict(features)

st.write('Are They Survived ? ')
if res == 1:
	msg='No , Passanger is not alive ❌'
else:
	msg='Yes , Passanger is alive ✅'
st.write(msg)




















