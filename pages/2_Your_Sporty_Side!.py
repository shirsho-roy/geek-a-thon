import streamlit as st
import pandas as pd
import pickle
from PIL import Image

#Model Import
model = pickle.load(open('model.pkl','rb'))

#Page initialization waali bakchodi
st.set_page_config(
    page_title="Me!",
    page_icon="🏅",
    layout="wide",
)

#Vertical space adding function
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

#Input
st.header("BodyFat Prediction!")
st.write("Input your data as per requirement to get an estimate for your bodyfat. You can use the converter to get the values in the required unit before feeding it to the model. The ideal percentage of body fat differs between men and women. This is primarily because they have differences in body composition. Body composition is the proportion of fat relative to lean tissue, such as muscles, organs, bones. It's a clear indicator for fitness, which reveals the amount of fat mass instead of total weight.")

st.subheader("Unit Converters")
st.write("**Kilograms to Pounds**")
kgs=st.number_input("Enter your weight in kg")
st.success("Your weight in lbs is "+str(round(2.20462*kgs,2)))
st.write("**Pounds to Kilograms**")
lbs=st.number_input("Enter your weight in lbs")
st.success("Your weight in lbs is "+str(round(lbs/20462,2)))
v_spacer(2,sb=False)

st.write("**Centimeters to Inches**")
cms=st.number_input("Enter your height in cms")
st.success("Your height in inches is "+str(round(0.393701*cms,2)))
st.write("**Inches to Centimeters**")
inc=st.number_input("Enter your height in inches")
st.success("Your height in inches is "+str(round(2.54*inc,2)))
v_spacer(2,sb=False)

st.write("**Bodyfat Predictor**")
st.warning("The model is trained to function for biological males. It may lead to inaccurate values in other cases.")
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
st.success(ans)

st.subheader("Hop in on your own journey!")
st.write("We would love to be a part of your journey. Let's take the first step and figure out the best dietary habits for you!")

image = Image.open('Assets\healthy-body-comparison.jpg')
col1, col2, col3 = st.columns([0.25, 12.5, 0.25])
col2.image(image, use_column_width=True)
v_spacer(2,sb=False)

st.subheader("Fat Free Mass Index (FFMI)")
st.write("FFMI stands for Fat-Free Mass Index, and it is a numerical value used to estimate the amount of lean body mass a person has relative to their height. It is often employed in the context of fitness and bodybuilding to assess an individual's muscularity and is considered an alternative to the Body Mass Index (BMI).")
st.write("The FFMI depends upon lean body mass in contrast to the total body-weight used by BMI. Lean body mass includes all non-fat tissues in the body, such as muscle, bone, and organs. The additional constant of 6.1 in the formula accounts for the natural amount of fat-free mass present in the body.")

st.warning("You can determine your bodyfat percentage from the calculator on this page.")
ffmi_weight=st.number_input("Enter your weight in kilograms")
ffmi_height=st.number_input("Enter your height in meters",value=1.00)
ffmi_bodyfat=st.number_input("Enter you bodyfat percentage")

lean_mass=(1-(ffmi_bodyfat/100))*ffmi_weight
ffmi=(lean_mass/(ffmi_height*ffmi_height))+6.1*(1.8-ffmi_height)
v_spacer(1,sb=False)
st.success("**Your fat free mass index or FFMI is**" + " " +str(round(ffmi,2)))

st.write("FFMI is measured on a scale where a value of 25 is considered the upper limit for individuals with little to no use of anabolic steroids, as it is believed to be the natural physiological limit for most people. Values significantly higher than 25 might indicate the use of performance-enhancing substances, though FFMI alone cannot definitively prove steroid use.")
st.write("It's essential to note that FFMI is a simplified assessment tool and should not be considered the sole indicator of an individual's overall health or fitness level. Consulting with healthcare professionals and fitness experts can provide a more comprehensive evaluation of one's body composition and well-being.")

v_spacer(2,sb=False)
st.subheader("Calorie Calculation")

val_weight=st.number_input("Enter your weight in kgs")
val_height=st.number_input("Enter your height in cm")
val_age=st.number_input("Enter your age in years")
val_act=st.selectbox("Select your activity level",options=['sedentary (little or no exercise)',
                                                           'lightly active (light exercise/sports 1-3 days​/week)',
                                                           'moderately active (moderate exercise/sports 3-5 days/week)',
                                                           'very active (hard exercise/sports 6-7 days a week)',
                                                           'extra active (very hard exercise/sports & physical job or 2x training)'])



bmr=0
colo1,colo2=st.columns(2)
with colo2:
    val_gender=st.radio("Select your biological gender",options=['Male','Female'])
    if(val_gender=='Male'):
        bmr=(10*val_weight)+(6.25*val_height)-(5*val_age)+5 
    else:
        bmr=(10*val_weight)+(6.25*val_height)-(5*val_age)-161

multiplier=0
if val_act=='sedentary (little or no exercise)':
    multiplier=1.2
elif val_act=='lightly active (light exercise/sports 1-3 days​/week)':
    multiplier=1.375
elif val_act=='moderately active (moderate exercise/sports 3-5 days/week)':
    multiplier=1.55
elif val_act=='moderately active (moderate exercise/sports 3-5 days/week)':
    multiplier=1.725
else:
    multiplier=1.9

addendum=0
with colo1:
    val_change=st.radio("Select your goal",options=['Gain Weight','Maintain Weight','Lose Weight'])
    if val_change=='Gain Weight':
        addendum=300
    elif val_change=='Lose Weight':
        addendum=-300
    else:
        addendum=100

st.success("**Your personalized calorie recommendation is**" + " " + str(round(bmr*multiplier,2)+addendum)+" "+"**calories**")
v_spacer(2,sb=False)

st.subheader("Takeaway!")
st.write("How many calories you need per day depends on whether you want to maintain, lose, or gain weight, as well as various other factors, such as your sex, age, height, current weight, activity level, and metabolic health.")
st.write("Many websites and apps can help you track your calorie intake. You can try using a calorie counter or tracker for at least a few days to see the amount of calories, carbs, protein, fat, fiber, vitamins, and minerals you’re eating.")
st.write("That said, working with a registered dietitian (RD) can also help you gain, maintain, or lose weight while ensuring that your nutrient needs are being met.")
st.sidebar.success("Walk with us on your own journey!")
v_spacer(2,sb=True)
st.sidebar.subheader("Your Fitness Journey!")
st.sidebar.write("Here we can start off with your baseline and give you something to work on. With our calculators based on the latest research and science you will understand your body like you never did before.")
st.sidebar.write("So grab a measuring table and weighing scale! And don't worry about the units, we've got all of that covered for you.")
