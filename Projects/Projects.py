import streamlit as st
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


def projects_page():
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
    .project-title {
        font-size: 24px !important;
        font-weight: bold;
        color: #3CB371;
    }
    .project-description {
        font-size: 18px !important;
        color: #333333;
    }
    .tech-stack {
        font-size: 16px !important;
        color: black;
    }
    .project-card {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<p class="big-font">My Projects</p>', unsafe_allow_html=True)

    # Project data
    projects = [
        {
            "title": "AI-Powered Education Recommendation System",
            "description": "Developed an advanced machine learning recommendation system that uses collaborative filtering and deep learning algorithms to provide personalized educational content suggestions. The system analyzes learning patterns, student performance, and content metadata to generate highly accurate recommendations.",
            "tech_stack": ["Python", "TensorFlow", "Scikit-learn", "Pandas", "Streamlit"],
            "image": "https://img.freepik.com/free-vector/artificial-intelligence-concept-illustration_114360-7000.jpg?w=826&t=st=1704617442~exp=1704618042~hmac=4f0e487614fb5b5c6f4b3be36c80e8eea61281cffef0a35b0e274d7df8be2d7c",
            "key_features": [
                "Personalized learning path generation",
                "Performance prediction",
                "Content relevance scoring",
                "Machine learning model interpretability"
            ]
        },
        {
            "title": "Natural Language Processing Intelligent Chatbot",
            "description": "Created an advanced NLP chatbot using state-of-the-art language models and deep learning techniques. The chatbot can understand context, intent, and sentiment, providing intelligent and contextually relevant responses across multiple domains.",
            "tech_stack": ["Python", "NLTK", "spaCy", "Transformers", "PyTorch"],
            "image": "https://img.freepik.com/free-vector/chat-bot-concept-illustration_114360-5522.jpg?w=826&t=st=1704617525~exp=1704618125~hmac=df203a9f9f731ddca5b25441fc47a04cfc7bd02000ed19809b45f61d14f0d6db",
            "key_features": [
                "Multi-intent recognition",
                "Contextual understanding",
                "Sentiment analysis",
                "Dynamic response generation"
            ]
        },
        {
            "title": "Computer Vision Disease Detection System",
            "description": "Developed a cutting-edge deep learning model for medical image analysis, capable of detecting and classifying various diseases from medical imaging data. The system uses convolutional neural networks (CNNs) to provide accurate and rapid diagnostic insights.",
            "tech_stack": ["Python", "TensorFlow", "Keras", "OpenCV", "NumPy"],
            "image": "https://img.freepik.com/free-vector/medical-technology-concept_23-2148497943.jpg",
            "key_features": [
                "Multi-disease classification",
                "High accuracy image processing",
                "Transfer learning implementation",
                "Explainable AI techniques"
            ]
        }
    ]

    # Display projects
    for project in projects:
        with st.container():
            st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
            col1, col2 = st.columns([1, 2])

            with col1:
                st.image(project['image'], width=200)

            with col2:
                st.markdown(f'<p class="project-title">{project["title"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="project-description">{project["description"]}</p>', unsafe_allow_html=True)
                st.markdown(f'<p class="tech-stack">Tech Stack: {", ".join(project["tech_stack"])}</p>',
                            unsafe_allow_html=True)
                
                # Add key features
                st.markdown("<p class='tech-stack'>Key Features:</p>", unsafe_allow_html=True)
                for feature in project.get('key_features', []):
                    st.markdown(f"- <span style='color: black;'>{feature}</span>", unsafe_allow_html=True)

            st.markdown('</div>', unsafe_allow_html=True)

    # Add a section for other projects or open source contributions
    st.markdown('<p class="project-title">Other Projects & Contributions</p>', unsafe_allow_html=True)
    st.markdown("""
    <ul class="project-description">
        <li>Contributed to open-source project XYZ: Implemented feature ABC, improving performance by 25%</li>
        <li>Developed a command-line tool for automating data preprocessing tasks</li>
        <li>Created a series of technical blog posts on machine learning best practices</li>
    </ul>
    """, unsafe_allow_html=True)

    # Call to action
    st.markdown("""
    <div style="text-align: center; margin-top: 50px;">
        <p class="project-description">Interested in collaborating or learning more about my projects?</p>
        <a href="mailto:mahmoudelshabrawy662001@gmail.com" style="background-color: #1E90FF; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold;">Get in Touch</a>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    projects_page()