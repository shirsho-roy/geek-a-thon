import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image

df=pd.read_csv("Data/athlete_events.csv")
df['BMI']=(df['Weight']/(df['Height']*df['Height']))*10000
nations=sorted(list(df['NOC'].unique()))
sports=sorted(list(df['Sport'].unique()))
years=sorted(list(df['Year'].unique()))
nations.insert(0,"NA")
sports.insert(0,"NA")
years.insert(0,"NA")

#Page load waali bakchodi
st.set_page_config(
    page_title="OlympData - Analysis",
    page_icon="🏅",
    layout="wide",
)

with open("style.css") as f:
        custom_css = f.read()
        st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

#Vertical space adding function
def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')
v_spacer(3, sb=False)




#Sidebar waali bakchodi
# st.sidebar.success("Parametric Analysis")

#Page Content
st.title("Parametric Analysis")
val_nation=st.sidebar.selectbox("Pick a nation, for deeper analysis",options=nations,index=42)
val_sport=st.sidebar.selectbox("Pick a sport, for deeper analysis",options=sports)
val_year=st.sidebar.selectbox("Pick a year, for deeper analysis",options=years)



#Sidebar Warning
st.sidebar.warning("Running visualisations over the entire dataset, i.e. having 'NA' across all parameters may cause slow response and can cause the webpage to crash.")

#Mean imputation
df2=df
df2['Age']=df2['Age'].fillna(df2['Age'].mean())
df2['Height']=df2['Height'].fillna(df2['Height'].mean())
df2['Weight']=df2['Weight'].fillna(df2['Weight'].mean())
df2['Age']=df2['Age'].apply(np.floor)

if val_nation=="NA" and val_sport=="NA" and val_year=="NA":
    df_res=df2
elif val_nation=="NA" and val_sport=="NA" and val_year!="NA":
    df_res=df2.loc[df2['Year']==val_year]
elif val_nation=="NA" and val_sport!="NA" and val_year=="NA":
    df_res=df2.loc[df2['Sport']==val_sport]
elif val_nation!="NA" and val_sport=="NA" and val_year=="NA":
    df_res=df2.loc[df2['NOC']==val_nation]
elif val_nation!="NA" and val_sport!="NA" and val_year=="NA":
    df_res=df2.loc[df2['NOC']==val_nation]
    df_res=df_res.loc[df_res['Sport']==val_sport]
elif val_nation=="NA" and val_sport!="NA" and val_year!="NA":
    df_res=df2.loc[df2['Year']==val_year]
    df_res=df_res.loc[df_res['Sport']==val_sport]
elif val_nation!="NA" and val_sport=="NA" and val_year!="NA":
    df_res=df2.loc[df2['Year']==val_year]
    df_res=df_res.loc[df_res['NOC']==val_nation]
else:
    df_res=df2.loc[df2['NOC']==val_nation]
    df_res=df_res.loc[df_res['Sport']==val_sport]
    df_res=df_res.loc[df_res['Year']==val_year]

array_temp=list(df_res['Age'])
array_temp_unique=list(df_res['Age'].unique())
counts=[]
for i in array_temp_unique:
    temp=array_temp.count(i)
    counts.append(temp)
age_count={'age':array_temp_unique,'count':counts}
age_count_df=pd.DataFrame(age_count)

#Age Variation
st.subheader("All Demographics")
st.write("You can study how the age demographic of each member nation is distributed and how various other parameters vary with respect to several different parameters including age of the athlete, sex of the athlete and many more. Height-Weight variations can be studied via the BMI charts. All substantial variations can be studied via the plotted curves.")

#Better scaling
minage=9999
maxage=0
for i in df_res['Age']:
    minage=min(minage,i)
    maxage=max(maxage,i)
#Limit to 50. Buddho ko analyse nahi karna bc. Sharam karo USA waalon. Vridhashram bhejo inhe bc.
maxage=min(maxage,50)
v_spacer(2,sb=False)

#Age Plot
st.write("**1. Distribution of players across different ages**")
type_age=st.radio(label="Pick a method for graph visualisation.",options=['Bar Chart','Line Chart'],horizontal=True)
if(type_age=='Bar Chart'):
    params=alt.Chart(age_count_df).mark_bar().encode(
        x=alt.X('age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
        y=alt.Y('count',title="Number of athletes")
    )
    st.altair_chart(params,use_container_width=True)
else:
    params=alt.Chart(age_count_df).mark_line().encode(
        x=alt.X('age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
        y=alt.Y('count',title="Number of athletes")
    )
    st.altair_chart(params,use_container_width=True)

#Display count
num=len(df_res)
st.write("**The total number of athletes corresponding to the chosen parameters is :** " + str(num))

#Gender Distribution
male=0
female=0
for i in df_res['Sex']:
    if i=='M':
        male+=1
    else:
        female+=1
genders_array=["Male","Female"]
genders_count_array=[male,female]
gender_demographics={'gender':genders_array,'gender_freq':genders_count_array}
gender_demographics_df=pd.DataFrame(gender_demographics)

#Plot
v_spacer(1,sb=False)
st.write("**2. Distribution of athletes by gender**")
type_age=st.radio(label="Pick a method for visualisation of the plot.",options=['Bar Chart','Line Chart'],horizontal=True)
if(type_age=='Bar Chart'):
    params=alt.Chart(gender_demographics_df).mark_bar().encode(
        x=alt.X('gender',title="Gender"),
        y=alt.Y('gender_freq',title="Number of athletes")
    )
    st.altair_chart(params,use_container_width=True)
else:
    params=alt.Chart(gender_demographics_df).mark_line().encode(
        x=alt.X('gender',title="Gender"),
        y=alt.Y('gender_freq',title="Number of athletes")
    )
    st.altair_chart(params,use_container_width=True)

#Distribution of age vs height
v_spacer(2,sb=False)
st.write("**3. How do different generations of players differ in height?**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median height for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")

check_height=st.radio("Do you want to see the outlying datapoints in height?",options=['No','Yes'],horizontal=True)
if(check_height=='No'):
    params=alt.Chart(df_res).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Height',title="Height in cm",scale=alt.Scale(domain=[140,200],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_res).mark_boxplot().encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Height',title="Height in cm",scale=alt.Scale(domain=[140,200],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

#Distribution of age vs height
v_spacer(2,sb=False)
st.write("**4. Height distribution by sex**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median height for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")

check_height=st.radio("Do you want to see the outlying datapoints in the distribution?",options=['No','Yes'],horizontal=True)
if(check_height=='No'):
    params=alt.Chart(df_res).mark_boxplot(outliers=False,size=250).encode(
            x=alt.X('Sex',title="Sex"),
            y=alt.Y('Height',title="Height in cm",scale=alt.Scale(domain=[140,200],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_res).mark_boxplot(size=250).encode(
            x=alt.X('Sex',title="Sex"),
            y=alt.Y('Height',title="Height in cm",scale=alt.Scale(domain=[140,200],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

#Weight distribution by age
v_spacer(2,sb=False)
st.write("**5. Times have changed, how have the weights?**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median weight for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")

check_weight=st.radio("Do you want to see the outlying datapoints in weight?",options=['No','Yes'],horizontal=True)
if(check_weight=='No'):
    params=alt.Chart(df_res).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Weight',title="Weight in kg",scale=alt.Scale(domain=[25,125],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_res).mark_boxplot().encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Weight',title="Weight in kg",scale=alt.Scale(domain=[25,125],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

#Weight distribution by sex
v_spacer(2,sb=False)
st.write("**6. Weight distribution by sex**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median height for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")

check_height=st.radio("Do you want to see the outlying datapoints in this distribution?",options=['No','Yes'],horizontal=True)
if(check_height=='No'):
    params=alt.Chart(df_res).mark_boxplot(outliers=False,size=250).encode(
            x=alt.X('Sex',title="Sex"),
            y=alt.Y('Weight',title="Weight in kg",scale=alt.Scale(domain=[25,125],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_res).mark_boxplot(size=250).encode(
            x=alt.X('Sex',title="Sex"),
           y=alt.Y('Weight',title="Weight in kg",scale=alt.Scale(domain=[25,125],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)


v_spacer(2,sb=False)
st.write("**7. Let's talk Somatotypes**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median ***BMI*** for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")
st.write("**BMI -** *BMI or Mody Mass Index, is the parameter we've made use of to better convey averages. While there are better parameters like the FFMI or Fat Free Mass Index, but considering the availability of data, BMI seems to be a better fit for the situation.*")

check_BMI=st.radio("Do you want to see the outlying datapoints in BMI?",options=['No','Yes'],horizontal=True)
if(check_BMI=='No'):
    params=alt.Chart(df_res).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('BMI',title="Body Mass Index",scale=alt.Scale(domain=[12,32],clamp=True)),
            color=alt.Color('Sex')
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_res).mark_boxplot().encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('BMI',title="Body Mass Index",scale=alt.Scale(domain=[12,32],clamp=True)),
            color=alt.Color('Sex')
        )
    st.altair_chart(params,use_container_width=True)

#Counting somatotypes
endo=0
meso=0
ecto=0
for i in df_res['BMI']:
    if i<=19:
        ecto+=1
    elif i<25:
        meso+=1
    else:
        endo+=1

#Creating dictionary of somatotype and counts
classes=['ectomorph','mesomorph','endomorph']
count_classes=[ecto,meso,endo]
dict_classes={'bodytypes':classes,'frequency':count_classes}
df_somatotype_counts=pd.DataFrame(dict_classes)

v_spacer(1,sb=False)
st.write("**Count of different somatotypes**")

#Somatotypes Count Plot
type_somatotype=st.radio(label="Pick how you'd like to visualize the count here.",options=['Bar Chart','Line Chart'],horizontal=True)
if(type_somatotype=='Bar Chart'):
    params=alt.Chart(df_somatotype_counts).mark_bar().encode(
        x=alt.X('bodytypes',title="Somatotype"),
        y=alt.Y('frequency',title="Number of athletes")
    )
    st.altair_chart(params,use_container_width=True)
else:
    params=alt.Chart(df_somatotype_counts).mark_line().encode(
        x=alt.X('bodytypes',title="Somatotype"),
        y=alt.Y('frequency',title="Number of athletes")
    )
    st.altair_chart(params,use_container_width=True)

#Sport vs Age distribution
v_spacer(2,sb=False)
st.write("**8. What's cool among the kids?**")
st.write("Let's have a look at which sport is played by people across age groups. Hover over each box for more details!")

check_sport_age=st.radio("Do you want to see the outlying datapoints in the corresponding distribution?",options=['No','Yes'],horizontal=True)
if(check_sport_age=='No'):
    params=alt.Chart(df_res).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age"),
            y=alt.Y('Sport',title="Sport"),
            color=alt.Color('Sex')
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_res).mark_boxplot().encode(
            x=alt.X('Age',title="Age"),
            y=alt.Y('Sport',title="Sport"),
            color=alt.Color('Sex')
        )
    st.altair_chart(params,use_container_width=True)

