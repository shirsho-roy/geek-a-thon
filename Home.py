import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image

#Read csv into DataFrame 
df=pd.read_csv("Data/athlete_events.csv")
#Page load 
st.set_page_config(
    page_title="OlympData",
    page_icon="🏅",
    layout="wide",
)

def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')

v_spacer(3, sb=False)



with open("style.css") as f:
        custom_css = f.read()
        st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)



#Content waali bakchodi
st.title("OlympData!")
v_spacer(3, sb=False)
st.header("Uncovering the Goldmine of Olympic Insights!")


#Vertical space adding function
def v_spacer(height, sb=False) -> None:
    for _ in range(height):
        if sb:
            st.sidebar.write('\n')
        else:
            st.write('\n')

#Description waali bakchodi
st.write("Welcome to OlympData, your ultimate destination for comprehensive analysis of previous Olympic data. Whether you're a sports enthusiast, a researcher, or simply curious about the history of the Olympic Games, OlympData offers a wealth of information and insights to satisfy your curiosity. **We provide you the power to pick your parameters allowing you to zone in on a given nation, a given sport, a given year all at the same time, or pick any combinations of the 3. Additionally, we provide some parameters, to give you some broad-stroke analysis. These analyses include the variation of only 1 major parameter. The broad-stroke pages include mostly variations with respect to age and physical parameters for the sake of simplicity. For more personalised solutions, the 'Pick Your Parameters' page is all yours!**.")
st.write("Explore a wide range of statistical data on our website, including medal counts, individual and team performances, records, and historical trends. Our interactive visualizations and intuitive tools allow you to navigate the data effortlessly, enabling you to uncover fascinating patterns and gain unique perspectives on the Games.")
st.write("Using OlympData, you can filter and analyze the data according to your preferences, whether you're interested in a specific sport, country, or Olympic edition. Discover how countries have fared over time, track the evolution of Olympic records, or compare performances across different sports. Our user-friendly interface ensures that you can delve into the data and customize your exploration with ease.")
st.write("Whether you're an avid sports fan, a student conducting research, or someone seeking inspiration from the remarkable achievements of Olympic athletes, OlympData is your go-to resource. Uncover the hidden insights within Olympic data and embark on a captivating journey through the annals of the Games. Join us today and let the numbers tell their story!")
st.text("")
#New subheader waali bakchodi
st.header("Olympics you ask?")
st.markdown("*Just in case you've been living under a rock,*")

#New subheader ki description waali bakchodi
st.write("The Olympics is a globally celebrated sporting event that brings together athletes from around the world to compete in a wide array of sports disciplines. Held every four years, the Olympics symbolize unity, sportsmanship, and the pursuit of excellence. The event showcases the remarkable physical and mental abilities of athletes, while also promoting cultural exchange and understanding among nations.")

image = Image.open('Assets\XxjpseE007006_20210724_MVPFN0A001-696x439.jpg')
col1, col2, col3 = st.columns([0.5, 1.5, 0.5])
col2.image(image, use_column_width=True, caption="Tokyo Olympics 2022")

st.write("The modern Olympics trace their roots back to the ancient Olympic Games of Greece, which were held over 2,700 years ago. Revived in 1896, the modern Olympic Games have grown into one of the most prestigious and eagerly anticipated sporting spectacles worldwide. The International Olympic Committee (IOC) oversees the organization and governance of the Olympics, ensuring fair competition, adherence to rules, and the Olympic spirit.")
st.write("Beyond the competitive aspect, the Olympics foster cultural exchange and promote understanding among nations. Athletes and spectators from all corners of the globe come together to celebrate the shared values of sportsmanship, camaraderie, and fair play. The Olympic Games provide an opportunity for countries to showcase their culture, traditions, and hospitality, leaving a lasting impact on the host city and its people.")
st.write("As the world's largest sporting event, the Olympics captivate billions of viewers, ignite national pride, and serve as a testament to the power of sports to unite humanity. The Games represent a celebration of athletic prowess, cultural diversity, and the universal values of peace, friendship, and solidarity.")
st.text("")


st.header("We got that data!")
st.write("It is indeed very exciting, getting our hands on some quality data to explore what happens to be the largest sporting event in the world.While it is tempting to dive headfirst into this ocean of data, we acknowlege that evaluating data completeness and practicing transperency regarding the same is very important. So here goes! Here's the year wise completeness we have for the data in use!")
st.text("")
#Data manipulation to get Data Completeness vs Year curve
years=list(df['Year'].unique())
completeness_array=[]
for i in range(len(years)):
    var=df.loc[df["Year"]==years[i]].isna().sum().sum()
    varlen=len(df.loc[df["Year"]==years[i]])
    completeness=100-(((var/varlen)*100)/12)
    completeness_array.append(completeness)

#Sidebar
# st.sidebar.success("You are viewing the Home page.")
# st.sidebar.write("Use the sidebar on the 'Analysis' and 'Pick Your Parameters' pages to customize the parameters for your data visualisation and analytics.")
# v_spacer(height=16,sb=True)
# st.sidebar.write("**Team - East India Company**")


#Completeness plot
completeness_year={'completeness':completeness_array,'year':years}
completeness_df=pd.DataFrame(completeness_year)
params=alt.Chart(completeness_df).mark_line().encode(
    x=alt.X('year',title="Year"),
    y=alt.Y('completeness',scale=alt.Scale(domain=[75,95],clamp=True),title="Data Completeness")
)
st.altair_chart(params,use_container_width=True)
st.write("Methods of mean imputation were used to fill in empty data points!")
st.text("")
st.download_button(
    label="Download data as CSV",
    data="Data/athlete_events.csv",
    file_name='"athlete_events.csv"',
    mime='text/csv',
)