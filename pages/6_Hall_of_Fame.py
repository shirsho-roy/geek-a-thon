import streamlit as st
import streamlit_authenticator as stauth
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import altair as alt
from PIL import Image

#Page initialization 
st.set_page_config(
    page_title="Hall of Fame",
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


st.header("Hall of Fame!")
st.write("Welcome to the prestigious Olympics Hall of Fame! Our website is a celebration of sporting greatness, where we pay homage to the legendary athletes who have left an indelible mark on the history of the Olympic Games. Step into a world of unparalleled athleticism, courage, and determination as we showcase the iconic Hall of Famers who have transcended the boundaries of sports and inspired generations to come.")
st.write("**Discover the Legends**: Immerse yourself in the captivating stories of the most exceptional athletes in Olympic history. From the iconic Jesse Owens who defied all odds at the 1936 Berlin Games to the unparalleled dominance of swimmer Michael Phelps, each Hall of Famer has a unique journey that has resonated with audiences worldwide. Explore their triumphs, challenges, and the impact they made both within their sports and beyond.")

v_spacer(3,sb=False)
image1 = Image.open('Assets\Lawrence_Lemieux.webp')
col1, col2 = st.columns([0.75, 0.25])
col2.image(image1, use_column_width=True, caption="Lawrence Lemieux")
with col1:
    st.subheader("10. Lawrence Lemieux, Canada")
    st.write("**Sailing – 1988 (Seoul)** - Winning isn’t everything… even at the Olympics. Lemieux’s sportsmanship and heroism during the 1988 Olympics in Seoul, South Korea, are a testament to the fact that some things are bigger than sports. There are several Olympic events that take place out at sea, and during Lemieux’s qualifying round for a sailing event there was another race taking place on a nearby course. Lemieux was in second place, a position that guaranteed a spot in the medal race, when the wind began to pick up.")
    st.write("Lemieux noticed a boat had capsized and there were men in danger so he veered off course and went to rescue them. The two men on the Singapore team were thrust from their vessel and had suffered injuries as a result. Lemieux scooped them both up and awaited help from a patrol boat. He ended up finishing in 22nd in the qualifying round. Fortunately, his heroism was rewarded, and his second-place position prior to the detour was held for him after the Olympic Committee reviewed the ordeal. In the end he didn’t medal (he was presented Pierre de Coubertin medal for sportsmanship), but the Canadian sailor proved during the 1988 Summer Games that the best moments aren’t always celebrated at the finish line or on the podium.")

v_spacer(3,sb=False)
image2 = Image.open('Assets\Dick-Fosbury2.jpeg')
colo1, colo2 = st.columns([0.25, 0.75])
colo1.image(image2, use_column_width=True, caption="Dick Fosbury")
with colo2:
    st.subheader("9. Dick Fosbury, United States")
    st.write("**High Jump – 1968 (Mexico City)** - It goes without saying that it is an extremely impressive feat to win the gold medal at the Olympics. It is even more impressive when you revolutionize your sport in the process. Anyone born after the 1960s may not realize that the high jump wasn’t always performed with your back facing the bar. Prior to the American’s now infamous “Fosbury Flop” during the 1968 Mexico City Summer Olympics, competitors used to dive over the bar face down. Fosbury wasn’t an elite high jumper with the original technique, so tried something new and different and ended up changing the event forever.")
    st.write("Initially met with skepticism, Fosbury's technique proved to be groundbreaking and incredibly successful. He won the gold medal in the 1968 Olympics, achieving a personal best of 2.24 meters (7 feet 4.25 inches). The Fosbury Flop completely revolutionized high jump competitions worldwide and became the standard technique used by virtually all high jumpers today.")
    st.write("Fosbury's legacy extends beyond his Olympic triumph. He has inspired generations of athletes to think outside the box and challenge conventional norms. His innovative approach not only changed the face of high jump but also symbolizes the spirit of pushing boundaries and embracing change in sports and beyond. Dick Fosbury's name remains etched in Olympic history, and his impact on the world of athletics will forever be remembered and celebrated.")

v_spacer(3,sb=False)
image3 = Image.open('Assets\Rulon_Gardner.jpg')
col11, col22 = st.columns([0.75, 0.25])
col22.image(image3, use_column_width=True, caption="Rulon Gardner")
with col11:
    st.subheader("8. Rulon Gardner, United States")
    st.write("**Wrestling – 2000 (Sydney)** - Gardner’s Olympic achievement wouldn’t be all that special if it wasn’t for his competition. Greco-Roman wrestling legend Alexander Karelin from Russia is considered by many to be the greatest wrestler of all time, and he may deserve a spot on this list more than Gardner. However, in the 2000 Sydney Games Gardner pulled off what many deemed impossible and defeated Karelin for the gold medal. Prior to this match, Karelin had not lost a Greco-Roman wrestling match in 13 years, he hadn’t even allowed an opponent to score a point against him in six years! The three-time defending Olympic gold medalist was a lock against Gardner, who had only competed in one other international tournament in his career. The American-born Gardner’s upset of the Russian powerhouse rivals the “Miracle on Ice” from 1980. In fact, it may be more remarkable.")
    st.write("Beyond his Olympic triumph, Rulon Gardner's wrestling career was filled with achievements. He won multiple World Championship medals and became a revered figure in the wrestling community. Gardner's journey was not without challenges, as he survived a near-fatal snowmobile accident and a plane crash, showcasing his resilience both on and off the mat.")

v_spacer(3,sb=False)
image2 = Image.open('Assets\Bob-Beamon.jpg')
colo1, colo2 = st.columns([0.25, 0.75])
colo1.image(image2, use_column_width=True, caption="Bob Beamon")
with colo2:
    st.subheader("7. Bob Beamon, United States")
    st.write("**Long Jump – 1968 (Mexico City)** - As the old adage goes, “records are made to be broken.” During the 1968 Summer Games in Mexico City this idea really resonated with Beamon. In his case the saying went more to the tune of, “records are made to be obliterated.” In what has since been dubbed the “Leap of the Century,” Beamon broke the long jump world record by almost 22 inches. The measuring equipment set up for the long jump wasn’t extended enough for Beamon, as the Olympic Committee was unprepared for a new world record by close to two feet. Equally impressive to his record was its tenure at the top. After 23 years it was finally broken in 1991, making it the longest standing Olympic record at the time. Beamon’s record became a record itself, how extraordinary is that?")
    st.write("Beamon's jump not only won him the gold medal but also cemented his place in Olympic history. The record he set that day stood for an astonishing 23 years until it was broken in 1991. His extraordinary feat in Mexico City became a symbol of the Olympic spirit, pushing the boundaries of human potential and achieving the seemingly impossible.")

v_spacer(3,sb=False)
image3 = Image.open('Assets\Michael-Phelps.webp')
col11, col22 = st.columns([0.75, 0.25])
col22.image(image3, use_column_width=True, caption="Michael Phelps")
with col11:
    st.subheader("6. Michael Phelps, United States")
    st.write("**Swimming – 2008 (Beijing)** - Michael Phelps is without question the greatest Olympian of all-time. His 18 gold medals are double the next highest mark. Phelps also is swimming very well coming into the upcoming Summer Olympics in Rio De Janeiro, following three individual race victories at the 2015 U.S. National Championships. Regardless of how he fares in his fourth and final Olympics, there is no way he will top his record eight gold medals from the 2008 Summer Games in Beijing. In just one Olympics, Phelps fell one short of the previous all-time Gold medal record.")
    st.write("Michael Phelps's impact on the sport of swimming and the Olympic movement as a whole is immeasurable. His dedication to training, unmatched talent, and remarkable sportsmanship have left an indelible mark on the world of sports. Phelps's name will forever be etched in Olympic history, and his legacy as one of the greatest athletes of all time will continue to inspire generations to come. Beyond his accomplishments in the pool, Michael Phelps has been open about his struggles with mental health issues and has become an advocate for mental health awareness, sharing his experiences to help others.")

v_spacer(3,sb=False)
image2 = Image.open('Assets/U-Bolt.jpg')
colo1, colo2 = st.columns([0.25, 0.75])
colo1.image(image2, use_column_width=True, caption="Usain Bolt")
with colo2:
    st.subheader("5. Usain Bolt, Jamaica")
    st.write("**Track & Field – 2008 (Beijing)** - Usain Bolt, the Fastest Man on Earth, has left an indelible mark on the world of athletics like no other sprinter before him. Born in Trelawny, Jamaica, on August 21, 1986, Bolt burst onto the international scene during the 2008 Beijing Olympics, dazzling spectators with his lightning speed and laid-back charm. Standing at 6 feet 5 inches tall, his towering figure seemed improbable for a sprinter, but Bolt defied all expectations, setting world records in the 100m, 200m, and 4x100m relay, elevating him to a global superstar. His electrifying performances transcended the realm of sports, making him a cultural icon admired by people of all ages and backgrounds. With a personality as vibrant as his track prowess, Bolt's infectious smile and exuberant celebrations endeared him to fans worldwide, turning every race into a spectacle of excitement. Throughout his career, he continued to dominate the Olympic Games, securing triple gold medals in both the 2012 London Olympics and the 2016 Rio de Janeiro Olympics. Usain Bolt's extraordinary talent, combined with his unique charisma, has etched his name in history as a legendary athlete who brought joy and awe to millions, leaving an enduring legacy for generations to come.")
    st.write("Outside of athletics, Bolt has dabbled in various ventures, including charity work and business endeavors. He remains actively involved in promoting sports and supporting young athletes through the Usain Bolt Foundation.")

v_spacer(3,sb=False)
image3 = Image.open('Assets/Jesse-Owens.jpg')
col11, col22 = st.columns([0.75, 0.25])
col22.image(image3, use_column_width=True, caption="Jesse Owens")
with col11:
    st.subheader("4. Jesse Owens, United States")
    st.write("**Track & Field – 1936 (Berlin)** - Owens' talent for sprinting and long jumping became apparent during his high school years in Cleveland, Ohio. He continued to excel at Ohio State University, where he garnered attention for his exceptional speed and jumping ability. Despite facing racial discrimination, both on and off the track, Owens remained undeterred and dedicated to his craft.")
    st.write("In 1936, Owens made history at the Berlin Olympics, which were heavily politicized by Adolf Hitler's Nazi regime. Amidst the backdrop of racial tensions and propaganda promoting Aryan supremacy, Jesse Owens fearlessly stepped onto the track and defied all odds. In a stunning display of athletic prowess, he won four gold medals, triumphing in the 100 meters, 200 meters, long jump, and 4x100 meters relay.")
    st.write("Jesse Owens' indomitable spirit, remarkable athletic talent, and commitment to breaking down barriers have forever etched his name in the annals of history. He remains a symbol of courage, determination, and the power of sports to bring about positive change and betterment.")

v_spacer(3,sb=False)
image2 = Image.open('Assets\Abebe.jpg')
colo1, colo2 = st.columns([0.25, 0.75])
colo1.image(image2, use_column_width=True, caption="Abebe Bikila")
with colo2:
    st.subheader("3. Abebe Bikila, Ethiopia")
    st.write("**Marathon – 1960 (Rome)** - Abebe Bikila, an Ethiopian long-distance runner, left an indelible mark on the world of athletics with his incredible achievements and extraordinary story. Born on August 7, 1932, in the town of Jato, Ethiopia, Bikila rose to prominence at the 1960 Rome Olympics. To the astonishment of the world, he ran the marathon barefoot, becoming the first African to win an Olympic gold medal. Four years later, at the 1964 Tokyo Olympics, Bikila won his second consecutive gold medal in the marathon, setting a new world record. His tenacity, grace, and determination in the face of adversity inspired countless individuals and helped put African long-distance running on the global map. Tragically, Bikila's career was cut short by a car accident in 1969, which left him paralyzed from the waist down. Nevertheless, he remained an enduring symbol of courage and perseverance until his untimely passing in 1973, leaving a legacy that continues to inspire athletes worldwide.")
    st.write("His name will forever be etched in the halls of athletic history, reminding us to run not just for the finish line, but for the joy of the journey and the inspiration we leave in our wake.")

v_spacer(3,sb=False)
image3 = Image.open('Assets\Greg.webp')
col11, col22 = st.columns([0.75, 0.25])
col22.image(image3, use_column_width=True, caption="Greg Louganis")
with col11:
    st.subheader("2. Greg Louganis, United States")
    st.write("**Diving – 1984 (Los Angeles)** - Greg Louganis, an American diving legend, is widely regarded as one of the greatest athletes in the history of the sport. Born on January 29, 1960, in El Cajon, California, Louganis faced numerous challenges throughout his life, including coming to terms with his identity as a gay man in a time when acceptance was limited. However, in the face of adversity, he channeled his energy and passion into diving, and his talent soon became evident. Louganis achieved unprecedented success, winning multiple Olympic gold medals and numerous world championships. His unmatched diving skills were complemented by his artistry and grace on the board. Beyond his accomplishments, Louganis' legacy is further enriched by his courage and openness about his HIV-positive status, becoming an advocate for HIV awareness and acceptance. Greg Louganis' impact extends far beyond the diving pool, as he remains an inspiration to aspiring athletes and an icon for breaking down barriers and promoting inclusion in the world of sports.")
    st.write("Greg Louganis will forever be celebrated as a diving icon and a beacon of hope for a more understanding and empathetic world.")

v_spacer(3,sb=False)
image2 = Image.open('Assets/Nadia.jpg')
colo1, colo2 = st.columns([0.25, 0.75])
colo1.image(image2, use_column_width=True, caption="Nadia Comaneci")
with colo2:
    st.subheader("1. Nadia Comaneci, Romania")
    st.write("**Gymnastics – 1976 (Montreal)** - As mentioned before, Bob Beamon’s outstanding long jump was so shocking that the measuring equipment did not even reach his landing spot. Comaneci’s gymnastic performance in 1976 was even more stunning, so much so that the electronic scoreboard couldn’t register her perfect 10 score. Prior to the 1976 Montreal Summer Olympics no gymnast had ever been awarded a perfect 10 for their routine, Comaneci did it six times. The Romanian phenom was an overnight sensation and remains one of the greatest gymnasts of all-time.")
    st.write(" At the tender age of 14, she astounded the world with her flawless routines, poise, and grace, earning her three gold medals, one silver, and one bronze in Montreal. Her exceptional performance revolutionized the sport, propelling her to international fame and inspiring countless aspiring gymnasts worldwide. Beyond her extraordinary achievements, Nadia Comaneci remains an enduring symbol of determination, talent, and the pursuit of excellence in the world of gymnastics. Her legacy continues to inspire generations of athletes and stands as a testament to the power of hard work and dedication.")
    st.sidebar.success("Welcome to the Hall of Fame! Let's take a walk down the history of the Olympics and refresh ourselves with the best the past has to offer!")