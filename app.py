import streamlit as st
from Contatct.Contact import contact_page
from Home.home import home_page
from Projects.Projects import projects_page
from Skills.skills import skills_page
from project_dashboard.project_dashboard import papers_page
def main():
    st.set_page_config(
        page_title="My Portfolio",
        page_icon=":briefcase:",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Sidebar Navigation with enhanced UI
    st.sidebar.title(f"Navigation - {st.session_state.get('current_page', 'Home')}")
    nav_options = {
        "🏠 Home": home_page,
        "💼 Projects": projects_page,
        "📚 Papers": papers_page,
        "🛠️ Skills": skills_page,
        "📧 Contact": contact_page
    }
    nav_choice = st.sidebar.radio("Select a page", list(nav_options.keys()), key="navigation")

    # Highlight active page in the sidebar
    st.markdown(
        f"""
        <style>
        .sidebar .stRadio [data-baseweb="radio"] {{
            background-color: #f0f0f5;
            border-radius: 10px;
            margin-bottom: 10px;
        }}
        .sidebar .stRadio [data-baseweb="radio"]:hover {{
            background-color: #e0e0eb;
        }}
        .sidebar .stRadio [data-baseweb="radio"].checked {{
            background-color: #1E90FF;
            color: white;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Set the current page to session state
    st.session_state['current_page'] = nav_choice.replace('🏠 ', '').replace('💼 ', '').replace('📚' , '').replace('🛠️ ', '').replace('📧 ', '')

    # Add a loading spinner when switching pages
    with st.spinner(f"Loading {st.session_state['current_page']}..."):
        try:
            # Call the selected page function
            nav_options[nav_choice]()
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()