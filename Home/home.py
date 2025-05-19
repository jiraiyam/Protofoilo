import streamlit as st
from PIL import Image
import base64


def add_bg_from_url():
    st.markdown(
        f"""
         <style>
         .stApp {{
             background-image: url("https://img.freepik.com/free-vector/white-abstract-background_23-2148806276.jpg?w=1380&t=st=1704616465~exp=1704617065~hmac=9435b372ddd03aee15f44dd4f43c0833adfb9a0a817ed2d1f7a6a52c2b3c3c24");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )


def home_page():
    add_bg_from_url()

    # Custom CSS for better formatting
    st.markdown("""
    <style>
    .big-font {
        font-size: 50px !important;
        font-weight: bold;
        color: #1E90FF;
        text-align: center;
    }
    .medium-font {
        font-size: 30px !important;
        font-weight: bold;
        color: #3CB371;
    }
    .normal-font {
        font-size: 20px !important;
        color: #333333;
    }
    .highlight {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title with a warm welcome
    st.markdown('<p class="big-font">🌟 Welcome to My Portfolio</p>', unsafe_allow_html=True)

    # Two-column layout for introduction and profile picture
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("""
        <div class="highlight normal-font">
        Hello! I'm thrilled to have you here. My portfolio showcases the projects I've worked on and the skills I've honed over time. 
        Explore my work, learn more about my journey, and feel free to reach out!
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "Home/1.jpg", 
            width=200, 
            caption="Mahmoud Elshabrawy")

    # About Me section with more detailed content
    st.markdown('<p class="medium-font">About Me</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="normal-font">
    My name is <b>Mahmoud Elshabrawy </b>, and I am a passionate AI Engineer. With a background in Computer Science, 
    I have developed a deep interest in Machine Learning and Data Science. Whether it's working on AI projects, developing innovative solutions, 
    or exploring new technologies, I am always eager to learn and grow.
    </div>
    """, unsafe_allow_html=True)

    # Expertise section with icons
    st.markdown('<p class="medium-font">My Expertise</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="highlight normal-font">
        🔧 <b>Machine Learning:</b> Developing predictive models and algorithms.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="highlight normal-font">
        📊 <b>Data Science:</b> Data-driven insights and advanced analytics.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="highlight normal-font">
        🎨 <b>Data Visualization:</b> Creating insightful and interactive dashboards.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="highlight normal-font">
        🧠 <b>Natural Language Processing:</b> Analyzing and understanding text data.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="highlight normal-font">
        💻 <b>Software Development:</b> Building robust and scalable applications.
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="highlight normal-font">
        ⚙️ <b>Optimization Algorithms:</b> Enhancing solutions using metaheuristic methods.
        </div>
        """, unsafe_allow_html=True)

    # What Drives Me section
    st.markdown('<p class="medium-font">What Drives Me</p>', unsafe_allow_html=True)
    st.markdown("""
    <div class="normal-font">
    I believe in the power of technology to solve real-world problems and improve lives. My work is driven by a desire to make an impact and contribute to meaningful projects.
    </div>
    """, unsafe_allow_html=True)

    # Call to action encouraging exploration
    st.markdown("""
    <div class="highlight normal-font">
    I'm excited to share my work with you. Take a look around, check out my projects, and let me know what you think!
    </div>
    """, unsafe_allow_html=True)

    # Adding buttons that link to different sections
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div style="text-align: center; margin-top: 50px;">
            <p class="project-description">Check out all my key projects.</p>
            <a href="#projects-section" style="background-color: #1E90FF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Explore My Projects</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div style="text-align: center; margin-top: 50px;">
            <p class="project-description">Explore my range of technical and soft skills.</p>
            <a href="#skills-section" style="background-color: #1E90FF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">View My Skills</a>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div style="text-align: center; margin-top: 50px;">
            <p class="project-description">Interested in collaborating or learning more about my projects?</p>
            <a href="mailto:your.email@example.com" style="background-color: #1E90FF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Get in Touch</a>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    home_page()