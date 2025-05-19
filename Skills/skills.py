import streamlit as st
import plotly.graph_objects as go
import pandas as pd


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

def plot_radar_chart(skills_data):
    fig = go.Figure(data=go.Scatterpolar(
        r=skills_data['Proficiency'],
        theta=skills_data['Skill'],
        fill='toself',
        line_color='#1E90FF'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100], showticklabels=True),
            angularaxis=dict(
                tickmode='array',
                tickvals=skills_data['Skill'],
                tickfont=dict(color='rgb(60, 179, 113)',
                              size=16 ,
                              family="Arial Black, sans-serif")  # Set skill labels to green
            ),
            bgcolor='rgba(255, 255, 255, 0.8)'
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return fig

def skills_page():
    add_bg_from_url()

    st.markdown("""
    <style>
    .main-title {font-size:36px !important; font-weight: bold; color: #3CB371; margin-bottom: 20px; text-align: center;}
    .big-font {font-size:30px !important; font-weight: bold; color: #1E90FF; margin-top: 30px;}
    .skill-category {background-color: rgba(240, 248, 255, 0.9); padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);}
    .skill-bar {height: 25px; margin-bottom: 10px; background-color: #E6E6FA; border-radius: 5px; overflow: hidden;}
    .skill-progress {height: 100%; background-color: #1E90FF; border-radius: 5px; text-align: right; color: white; padding-right: 5px; line-height: 25px;}
    .streamlit-expanderHeader {
        background-color: #1E90FF;
        color: white !important;
        border-radius: 5px;
        padding: 5px 10px;
    }
    .streamlit-expanderContent {
        background-color: rgba(255, 255, 255, 0.9);
        border-radius: 0 0 5px 5px;
    }
    p, li {
        color: #333333;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-title'>My Professional Skills</h1>", unsafe_allow_html=True)
    st.write("Explore my technical expertise and professional achievements.")

    # Technical Skills with radar chart
    st.markdown("<p class='big-font'>Technical Proficiency Overview</p>", unsafe_allow_html=True)
    skills_data = pd.DataFrame({
        "Skill": ["Data Analysis", "Machine Learning", "Statistical Analysis", "Deep Learning", 
                  "Time Series Analysis", "Data Engineering", "Data Visualization"],
        "Proficiency": [95, 90, 90, 85, 85, 80, 90]
    })

    fig = plot_radar_chart(skills_data)
    st.plotly_chart(fig, use_container_width=True)

    # Detailed skills breakdown
    st.markdown("<p class='big-font'>Detailed Skills Breakdown</p>", unsafe_allow_html=True)

    skill_categories = {
        "Data Science & Analytics": [
            ("Exploratory Data Analysis", 95),
            ("Data Cleaning", 95),
            ("Feature Engineering", 90),
            ("Statistical Inference", 90),
            ("Hypothesis Testing", 85)
        ],
        "Machine Learning & Deep Learning": [
            ("Classification", 90),
            ("Regression", 90),
            ("Time Series Prediction", 85),
            ("CNN", 85),
            ("GAN", 80),
            ("Model Evaluation", 95)
        ],
        "Data Engineering & Tools": [
            ("Data Pipelines", 85),
            ("SQL", 90),
            ("Python Libraries", 95),
            ("Time Series Processing", 85),
            ("Version Control", 80)
        ],
        "Visualization & Libraries": [
            ("Matplotlib", 90),
            ("Seaborn", 90),
            ("Plotly", 85),
            ("Jupyter Notebooks", 90)
        ]
    }

    for category, skills in skill_categories.items():
        with st.expander(category, expanded=True):
            for skill, proficiency in skills:
                st.markdown(f"""
                <div class="skill-bar">
                    <div class="skill-progress" style="width: {proficiency}%">
                        {skill} - {proficiency}%
                    </div>
                </div>
                """, unsafe_allow_html=True)

    # Certifications and Achievements
    st.markdown("<p class='big-font'>Certifications & Achievements</p>", unsafe_allow_html=True)

    cert_data = {
        "Professional Certifications": [
            "🏆 Advanced Data Science Certification",
            "🏅 Machine Learning Specialist Credential",
            "🎖️ Time Series Analysis Professional Certification"
        ],
        "Awards & Recognition": [
            "🥇 Best Data Science Project, Industry Innovation Challenge",
            "🏆 Advanced Machine Learning Research Award",
            "📚 Published Research: Machine Learning Applications in Complex Data Analysis"
        ]
    }

    for title, items in cert_data.items():
        with st.expander(title, expanded=True):
            for item in items:
                st.markdown(f"- {item}")

    # Call-to-action
    st.markdown("---")
    st.markdown("<h3 style='text-align: center; color: #1E90FF;'>Let's Connect!</h3>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align: center; margin-top: 50px;">
            <p style='text-align: center; color: #333333;'>Interested in collaborating or learning more about my skills? Feel free to reach out!</p>
            <a href="mailto:your.email@example.com" style="background-color: #1E90FF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Contact Me</a>
        </div>
        """, unsafe_allow_html=True)


if __name__ == "__main__":
    skills_page()