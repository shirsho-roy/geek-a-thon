import streamlit as st
import pandas as pd
import pickle

#Model Import
model = pickle.load(open('model.pkl','rb'))

#Vertical space adding function
def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')

#Input
st.header("BodyFat Prediction!")
st.write("Input your data as per requirement to get an estimate for your bodyfat. You can use the converter to get the values in the required unit before feeding it to the model.")
st.warning("The model is trained to function for biological males. It may lead to inaccurate values in other cases.")

st.subheader("Unit Converters")
st.write("**Kilograms to Pounds**")
kgs=st.number_input("Enter your weight in kg")
st.text("Your weight in lbs is "+str(round(2.20462*kgs,2)))

st.write("**Centimeters to Inches**")
cms=st.number_input("Enter your height in cms")
st.text("Your height in inches is "+str(round(0.393701*cms,2)))
v_spacer(2,sb=False)

st.write("**Bodyfat Predictor**")
col1,col2=st.columns(2)
Age=st.number_input("Enter your age")
with col1:
    Weight=st.number_input("Enter your weight in pounds ")
    Height=st.number_input("Enter height in inches ")
    Neck=st.number_input("Enter neck circumference in cms ")
    Chest=st.number_input("Enter chest circumference in cms ")
    Abdomen=st.number_input("Enter abdomen circumference in cms ")
    Hip=st.number_input("Enter hip circumference in cms ")
with col2:
    Thigh=st.number_input("Enter thigh circumference in cms ")
    Knee=st.number_input("Enter knee circumference in cms ")
    Ankle=st.number_input("Enter ankle circumference in cms ")
    Biceps=st.number_input("Enter bicep circumference in cms ")
    Forearm=st.number_input("Enter forearm circumference in cms ")
    Wrist=st.number_input("Enter wrist circumference in cms ")

list=[[Age,Weight,Height,Neck,Chest,Abdomen,Hip,Thigh,Knee,Ankle,Biceps,Forearm,Wrist]]
ans=float(model.predict(list))
st.write(ans)