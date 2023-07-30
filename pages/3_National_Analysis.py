import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image

#Read csv into DataFrame 
df=pd.read_csv("Data/athlete_events.csv")
df['BMI']=(df['Weight']/(df['Height']*df['Height']))*10000
nations=sorted(list(df['NOC'].unique()))
#Page load waali bakchodi
st.set_page_config(
    page_title="OlympData - National Analysis",
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
st.sidebar.success("Nation-Wise Analysis")

#Page Content
st.title("Nation-Wise Analysis")

#Mean imputation
df2=df
df2['Age']=df2['Age'].fillna(df2['Age'].mean())
df2['Height']=df2['Height'].fillna(df2['Height'].mean())
df2['Weight']=df2['Weight'].fillna(df2['Weight'].mean())

#Sidebar parameter optimisation
val=st.sidebar.selectbox("Pick a nation, for deeper analysis",options=nations)
st.sidebar.write("All nations are indexed and abbreviated to 3 letters to represent the nation.")

#Dataframe adjustments
df_nation = df2.loc[df2['NOC'] == val]
df_nation['Age']=df_nation['Age'].apply(np.floor)
array_temp=list(df_nation['Age'])
array_temp_unique=list(df_nation['Age'].unique())
counts=[]
for i in array_temp_unique:
    temp=array_temp.count(i)
    counts.append(temp)
age_count={'age':array_temp_unique,'count':counts}
age_count_df=pd.DataFrame(age_count)

#Content waali bakchodi again
st.subheader("Let's take a deeper dive into the member nations!")
st.write("Pick the nation you want to analyse further from the sidebar, based on the nation's 3 letter abbreviation. You can then navigate to the parameter whose variation you wish to study on this page and dig in to your heart's content. There are multiple visualisation options for the same data, so pick whichever pleases you!")

#Mein chutiya hoon, shift this to Year-Wise analysis. Nvm unintentionally looks cool here.
#Heatmap of occurence
st.subheader("**National Storehouse**")
st.write("**Here you can look for the presence of a certain type of award/medal in a nation's aresenal.**")
params=alt.Chart(df_nation).mark_bar().encode(
        x=alt.X('Sport',title="Sport"),
        y=alt.Y('Medal',title="Medals")
    )
st.altair_chart(params,use_container_width=True)

v_spacer(2,sb=False)
#Age Variation
st.subheader("Age Demographics")
st.write("You can study how the age demographic of each member nation is distributed and how various other parameters vary with respect to age. Height-Weight variations can be studied via the BMI charts. All substantial variations can be studied via the plotted curves.")

#Better scaling
minage=9999
maxage=0
for i in df_nation['Age']:
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

v_spacer(2,sb=False)
st.write("**2. How do different generations of players differ in height?**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median height for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")

check_height=st.radio("Do you want to see the outlying datapoints in height?",options=['No','Yes'],horizontal=True)
if(check_height=='No'):
    params=alt.Chart(df_nation).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Height',title="Height in cm",scale=alt.Scale(domain=[140,200],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_nation).mark_boxplot().encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Height',title="Height in cm",scale=alt.Scale(domain=[140,200],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

v_spacer(2,sb=False)
st.write("**3. Times have changed, how have the weights?**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median weight for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")

check_weight=st.radio("Do you want to see the outlying datapoints in weight?",options=['No','Yes'],horizontal=True)
if(check_weight=='No'):
    params=alt.Chart(df_nation).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Weight',title="Weight in kg",scale=alt.Scale(domain=[25,125],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_nation).mark_boxplot().encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('Weight',title="Weight in kg",scale=alt.Scale(domain=[25,125],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

v_spacer(2,sb=False)
st.write("**4. Let's talk Somatotypes**")
st.write("Hover on each of the boxes, to get more details about that age group, including minimum, maximum and median ***BMI*** for that given age group. You have the option to individually view datapoints that are ***outliers***, i.e. they do not fall in the bounds of the box produced by the boxplot. For a larger number of datapoints, this may make the visualisation messy.")
st.write("**BMI -** *BMI or Mody Mass Index, is the parameter we've made use of to better convey averages. While there are better parameters like the FFMI or Fat Free Mass Index, but considering the availability of data, BMI seems to be a better fit for the situation.*")

check_BMI=st.radio("Do you want to see the outlying datapoints in BMI?",options=['No','Yes'],horizontal=True)
if(check_BMI=='No'):
    params=alt.Chart(df_nation).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('BMI',title="Body Mass Index",scale=alt.Scale(domain=[12,32],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_nation).mark_boxplot().encode(
            x=alt.X('Age',title="Age",scale=alt.Scale(domain=[minage,maxage],clamp=True)),
            y=alt.Y('BMI',title="Body Mass Index",scale=alt.Scale(domain=[12,32],clamp=True))
        )
    st.altair_chart(params,use_container_width=True)

st.write("**Somatotypes -** Let's take a bit of an unconventional route to understanding somatotypes.")
st.write("Imagine that every person has a special body type, just like everyone has a unique personality. Somatotypes are a way to describe these different body types. There are three main somatotypes: endomorphs, mesomorphs, and ectomorphs.")
st.write("Now, let's imagine these somatotypes as different kinds of toys. Endomorphs are like soft and cuddly teddy bears. They tend to have rounder bodies and carry a bit of extra weight. Mesomorphs are like action figures. They have strong and athletic bodies with lots of muscles. Ectomorphs are like long and skinny action figures. They have lean bodies and are often quite tall.")
v_spacer(1,sb=False)
st.write("-Here, we classify **BMI values<=19** as **ectomorphs**,")
st.write("-Here, we classify **BMI values between 19 and 25** as **mesomorphs**,")
st.write("-Here, we classify **BMI values>=25** as **endomorphs**,")

#Counting somatotypes
endo=0
meso=0
ecto=0
for i in df_nation['BMI']:
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
type_somatotype=st.radio(label="Pick how you'd like to visualize the count.",options=['Bar Chart','Line Chart'],horizontal=True)
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
st.write("**5. What's cool among the kids?**")
st.write("Let's have a look at which sport is played by people across age groups. Hover over each box for more details!")

check_sport_age=st.radio("Do you want to see the outlying datapoints in the distribution?",options=['No','Yes'],horizontal=True)
if(check_sport_age=='No'):
    params=alt.Chart(df_nation).mark_boxplot(outliers=False).encode(
            x=alt.X('Age',title="Age"),
            y=alt.Y('Sport',title="Sport")
        )
    st.altair_chart(params,use_container_width=True)

else:
    params=alt.Chart(df_nation).mark_boxplot().encode(
            x=alt.X('Age',title="Age"),
            y=alt.Y('Sport',title="Sport")
        )
    st.altair_chart(params,use_container_width=True)

#Medals
st.subheader("Let's talk medals!")
st.write("Here we crunch data and visualise the medal count and their distribution across sports for the nation in question.")
medals=['Silver','Bronze','Gold']
gold=0
silver=0
bronze=0
for i in df_nation['Medal']:
    if i=='Gold':
        gold+=1
    elif i=='Silver':
        silver+=1
    else:
        bronze+=1
count_medals=[silver,bronze,gold]
total_medal={'medal_type':medals,'occurence':count_medals}
total_medal_df=pd.DataFrame(total_medal)

#Corresponding Plot
type_medal_count=st.radio(label="Pick how you'd like to visualize the number of medal.",options=['Bar Chart','Line Chart'],horizontal=True)
if(type_medal_count=='Bar Chart'):
    params=alt.Chart(total_medal_df).mark_bar().encode(
        x=alt.X('medal_type',title="Medals"),
        y=alt.Y('occurence',title="Number of medals")
    )
    st.altair_chart(params,use_container_width=True)
else:
    params=alt.Chart(total_medal_df).mark_line().encode(
        x=alt.X('medal_type',title="Medals"),
        y=alt.Y('occurence',title="Number of medals")
    )
    st.altair_chart(params,use_container_width=True)
st.write("This plot reflects the number of medals that the nation has accumulated **across their entire course of participation in the Olympic games.**")
df_nation=df_nation.fillna("-None")

#Athlete by sport count
v_spacer(2,sb=False)
st.subheader("Popular Sports!")
st.write("Here you can view which Olympic sport has the most number of athletes in the given nation.")
sports_list=sorted(list(df_nation['Sport'].unique()))
sport_count=[]
for i in sports_list:
    temp=list(df_nation['Sport']).count(i)
    sport_count.append(temp)

#Most Popular Sport
max_sport_count_idx=0
max_sport_count=0
for i in range(len(sport_count)):
    temp_num=sport_count[i]
    if temp_num>max_sport_count:
        max_sport_count=temp_num
        max_sport_count_idx=i

pop_sport=sports_list[max_sport_count_idx]

#Create corresponding dictionary and dataframe
v_spacer(2,sb=False)
sports_freq_dict={'sports':sports_list,'sport_freq':sport_count}
df_sports_freq=pd.DataFrame(sports_freq_dict)

#Corresponding Plot
params=alt.Chart(df_sports_freq).mark_bar().encode(
    x=alt.X('sport_freq',title="Number of athletes"),
    y=alt.Y('sports',title="Sport")
)
st.altair_chart(params,use_container_width=True)
v_spacer(1,sb=False)
st.success("Most popular Olympic sport in the nation is " + pop_sport + " with " + str(max_sport_count) + " players.")

#Ending content waali bakchodi, thoda aur likh lena
st.write("That wraps up all substantial variations with the nation being a driving parameter. Visit other pages to similarly study other variations!")