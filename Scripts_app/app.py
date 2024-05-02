#import library
import pickle
import streamlit as st

#read model
model_predict = pickle.load(open('Attrition.sav', 'rb'))

#create web title
st.title('Attrition Prediction')

#create input column
col1, col2, col3, col4 = st.columns(4)

with col1 :
    Age = st.text_input('Age')

with col1 :
    Department = st.text_input('Department')

with col2 :
    JobLevel = st.text_input('JobLevel')

with col2 :
    Gender = st.text_input('Gender')

with col3 :
    PercentSalaryHike = st.text_input('PercentSalaryHike')

with col3 :
    YearsInCurrentRole = st.text_input('YearsInCurrentRole')

with col4 :
    YearsAtCompany = st.text_input('YearsAtCompany')

#prediction code
attrition_predic=''

#create prediction button
if st.button('Attrition prediction test'):
    attrition_prediction = model_predict.predict([[Age, Department, JobLevel,
                                                   Gender, PercentSalaryHike,
                                                    YearsInCurrentRole,YearsAtCompany]])
    
    if(attrition_prediction[0] == 0):
        attrition_predic = 'Karyawan masih bekerja'
    else :
        attrition_predic = 'Karyawan sudah tidak bekerja'
    st.success(attrition_predic)