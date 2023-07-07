import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image

#Read csv into DataFrame 
df=pd.read_csv("Data/athlete_events.csv")
nations=list(df['NOC'].unique())

#Page load waali bakchodi
st.set_page_config(
    page_title="OlympData - National Analysis",
    page_icon="🏅",
    layout="wide",
)

#Sidebar waali bakchodi
st.sidebar.success("Nation-Wise Analysis")

#Page Content
st.title("Nation-wise Analysis")

#Mean imputation
df2=df
df2['Age']=df2['Age'].fillna(df2['Age'].mean())
df2['Height']=df2['Height'].fillna(df2['Height'].mean())
df2['Weight']=df2['Weight'].fillna(df2['Weight'].mean())

#Sidebar parameter optimisation
val=st.sidebar.selectbox("Pick a nation, for deeper analysis",options=nations)
st.sidebar.write("All nations are indexed and abbreviated to 3 letters to represent the nation.")
