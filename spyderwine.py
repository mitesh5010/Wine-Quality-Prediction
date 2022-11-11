# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 12:04:01 2022

@author: Yash
"""
import streamlit as st
import joblib
import sklearn

def main():
    html_temp="""
    <div style="background-colour:lightblue; padding:16px">
    <h2 style ="color:black";text-align:center> Wine Quality Prediction Using Machine Learning </h2>
    </div>  
    
    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    model = joblib.load('wine_quality_prediction')
    
    
    p1 = st.number_input("Fixed Acidity")
    p2 = st.number_input("volatile acidity")
    #p3 = st.number_input("citric acid")
    p4 = st.number_input("residual sugar")
    #p5 = st.number_input("chlorides")
    #p6 = st.number_input("free sulfur dioxide")
    p7 = st.number_input("total sulfur dioxide")
    #p8 = st.number_input("density")
    p9 = st.number_input("pH")
    p10 = st.number_input("sulphates")
    p11 = st.number_input("alcohol")
    
    
    if st.button('Predict'):
        pread = model.predict([[p1,p2,p4,p7,p9,p10,p11]])
        
        if pread[0] == 0:
            st.error('Bad Quality Wine') 
        else:
            st.success('Good Quality Wine') 
            st.snow()
       
    
if __name__=='__main__':
    main()
