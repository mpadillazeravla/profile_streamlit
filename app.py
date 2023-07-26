from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Streamlit prueba" , page_icon=":globe_with_meridians:" , layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

# USE CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>" , unsafe_allow_html=True)

local_css("style/style.css")

#------ MULTIMEDIA ---------------#
lottie_animation_code = load_lottieurl("https://lottie.host/52ea38b1-f6fd-4205-ab4a-d64aaf1b00be/iam9wQtwBW.json")
img_profile = Image.open("images/foto_perfil.jpg")
img_hackaton = Image.open("images/logoHackatonWorld.jpg")
img_bikemate = Image.open("images/bikemateScreenshot.png")
img_powerapps = Image.open("images/powerapps.png")

# -------------- MAP ------------ #
# center on Liberty Bell, add marker
m = folium.Map(location=[36.7201600, -4.4203400], zoom_start=16)
folium.Marker(
    [36.7201600, -4.4203400], popup="Malaga", tooltip="Malaga"
).add_to(m)


#-------- SIDEBAR ---------------#
with st.sidebar:
    st.markdown('<a href="http://localhost:8501/#hi-i-am-miguel" target="_self">Greetings</a>', unsafe_allow_html=True)
    st.markdown('<a href="http://localhost:8501/#what-i-do" target="_self">What I do</a>', unsafe_allow_html=True)
    st.markdown('<a href="http://localhost:8501/#my-favorite-projects" target="_self">Projects</a>', unsafe_allow_html=True)
    st.markdown('<a href="http://localhost:8501/#get-in-touch-with-me" target="_self">Contact</a>', unsafe_allow_html=True)

#----- HEADER SECTION --------#
with st.container():
    greeting = st.subheader("Hi, I am Miguel :wave:") 
    st.image(img_profile, width=120)
    st.title("Junior Full Stack Dev")
    st.write("I live here")
    st_data = st_folium(m, width=400 , height=300)
    st.write("I am a Python passionate working to achieve new levels and experimenting with some different tools")
    st.write("[More info >](https://www.linkedin.com/in/padilla-alvarez/)")
    st.write("##")
    st.write("Updating content...")


#----- WHAT I DO --------#
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Full Stack Developer and Certified Scrum Master (PSM I by Scrum.org) with more than 10 years of experience in retail.
                        
            Always learning.
            
            Interested in:
            - Python
            - Scrum
            - React
            """
        )
        st.write("[More info >](https://www.linkedin.com/in/padilla-alvarez/)")

    with right_column:
        st.lottie(lottie_animation_code ,height=500 , key = "coder")

#---------- PROJECTS -------------#
with st.container():
    st.write("---")
    st.header("My Favorite Projects")
    st.write("##")
    image_column , text_column= st.columns([1 ,  2])
    with image_column:
        tab1, tab2, tab3 = st.tabs(["Bikemate", "Hackaton", "Powerapps"])

        with tab1:
            st.header("Bikemate, a python flask and react app")
            st.image(img_bikemate)

        with tab2:
            st.header("A wordpress web for a hackaton")
            st.image(img_hackaton)

        with tab3:
            st.header("A powerapp app for internal use in my company")
            st.image(img_powerapps)

    with text_column:
        st.subheader("Multidisciplinary projects")
        st.write(
            """
            I'm working in several different projects with different technologies, like:
            - Wordpress
            - Powerapps
            - Powerautomate
            - Python 
            - Flutter
            """
        )
        st.markdown("[My full profile...](https://www.linkedin.com/in/padilla-alvarez/)")

#---------- CONTACT -------------#
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="9940102e79f166e1a277bda30e5588b9" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
    </form>
    """

    left_column , right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()