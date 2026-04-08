import streamlit as st
import pandas as pd
import joblib


st.set_page_config(page_icon='💖',page_title='HEART DISEASE PREDITION',layout='wide')

with st.sidebar:
     st.title('heart disease prediction')
     st.image('heart2.jpeg',width=300)

df=pd.read_csv('hdcleaned_df.csv')

with open('Log_model.joblib','rb') as file:
    model=joblib.load(file)

with st.container(border=True):

    col1,col2,col3=st.columns(3)

    with col1:
        age=st.number_input("Age", min_value=1, max_value=100)
        sex=st.radio('sex: ',options=[0,1],horizontal=True)
        
        d1={'typical angina':0,'atypical angina':1,'non-anginal pain':2,'asymptomatic':3}
        chest_pain_type=st.selectbox('chest_pain_type: ',options=d1.keys())
        chest_pain_type=d1[chest_pain_type]

        resting_bp=st.selectbox('resting_bp: ',options=sorted(df['resting_bp'].unique()))


    with col2:
        d1={'normal':0,'having ST - T wave abnormality':1,'hypertrophy':2}
        restecg=st.selectbox('rest_ecg',options=d1.keys())
        restecg=d1[restecg]

        d2={'upsloping':0,'flat':1,'downsloping':2}
        slope=st.selectbox('SLOPE',options=d2.keys())
        slope=d2[slope]

        num_vessels=st.selectbox('number of major vessels',options=[0,1,2,3])

        d3={'normal':3,'fixed_defect':6,'reversely defect':7}
        thal=st.selectbox('THAL:',options=d3.keys())
        thal=d3[thal]

    with col3:
        cholesterol=st.selectbox('cholesterol: ',sorted(df['cholesterol'].unique()))
        fbs=st.radio('fasting_bloodsugar',options=['0','1'],horizontal=True)
        fbs=int(fbs)

        max_heart=st.selectbox('max_heartrate: ',sorted(df['max_heart_rate'].unique()))
        exang=st.radio('exercise_angina',options=['0','1'],horizontal=True)
        exang=int(exang)

        oldpeak=st.selectbox('oldpeak: ',sorted(df['st_depression'].unique()))

    if st.button('PREDICT'):
        data=[[age,sex,chest_pain_type,resting_bp,cholesterol,fbs,restecg,max_heart,exang,oldpeak,slope,num_vessels,thal]]

        pred=model.predict(data)[0]

        if pred==0:
            st.subheader('LOW RISK OF HEART DISEASE')
            st.image('heart2.jpeg',width=200)
        else:
            st.subheader('HIGH RISK OF HEART DISEASE')
            st.image('heart1.jpeg',width=200)

