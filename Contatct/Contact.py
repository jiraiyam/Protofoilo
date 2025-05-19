import streamlit as st
import requests


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


def is_valid_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def contact_page():
    add_bg_from_url()

    # Custom CSS for better formatting and updated color scheme
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
    .contact-form {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .social-links {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }
    .stTextInput > div > div > input {
        background-color: #F0F8FF;
        color: #333333;
        border: 1px solid #1E90FF;
    }
    textarea {
    background-color: #F0F8FF !important;
    color: #333333 !important;
    border: 1px solid #1E90FF !important;
}

    .stTextInput > label,
    .stTextArea > label {
        color: #000000;  !important; /* Change color of "Your Name", "Your Email", and "Your Message as text of heads titles " */
    }
    .stButton > button {
        background-color: #1E90FF;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
    }
    .stExpander {
        background-color: #F0F8FF !important;  /* Make FAQ a button */
        color: green !important;
        padding: 10px !important;
        font-weight: bold !important;
        border-radius: 5px !important;
    }
    .contact-header {
        background-color: #F0F8FF;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .contact-header img {
        width: 100px;
        height: 100px;
        margin-right: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    # New header with a lighter theme and email icon
    st.markdown("""
    <div class="contact-header">
        <img src="https://img.icons8.com/clouds/100/000000/email.png" alt="Email Icon"/>
        <h1 class="big-font">Get in Touch</h1>
    </div>
    """, unsafe_allow_html=True)

    # Two-column layout for contact information and social media
    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<p class="medium-font">Contact Information</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="highlight normal-font">
        📧 Email: mahmoudelshabrawy662001@gmail.com<br>
        📱 Phone: +20 1021857896<br>
        📍 Location: Mansoura, Egypt
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown('<p class="medium-font">Social Media</p>', unsafe_allow_html=True)
        st.markdown("""
        <div class="social-links">
            <a href="https://www.linkedin.com/in/mahmoud-elshabrawy-5616581a7/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
            <a href="https://github.com/jiraiyam" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"></a>
            <a href="https://twitter.com/Mshika231" target="_blank"><img src="https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"></a>
        </div>
        """, unsafe_allow_html=True)

    # Contact form
    st.markdown('<p class="medium-font">Send Me a Message</p>', unsafe_allow_html=True)

    with st.form(key='contact_form', clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message", height=150)
        submit_button = st.form_submit_button(label='Send Message')

        if submit_button:
            if name and email and message:
                if is_valid_email(email):
                    # Here you would typically send an email or save to a database
                    st.success("Thank you! Your message has been sent successfully.")
                    st.balloons()
                else:
                    st.error("Please enter a valid email address.")
            else:
                st.warning("Please fill out all fields before sending.")

    # FAQ Section with button-like style
    st.markdown('<p class="medium-font">Frequently Asked Questions</p>', unsafe_allow_html=True)
    faq_expander = st.expander("Click to view FAQs")
    with faq_expander:
        st.markdown("""
        <div class="normal-font">
        <b>Q: How can I collaborate with you?</b><br>
        A: I'm always open to interesting collaborations! Please reach out via email with your project idea.<br><br>

        <b>Q: Are you available for freelance work?</b><br>
        A: Yes, I am available for select freelance projects. Contact me with details about your project for further discussion.<br><br>

        <b>Q: What's the best way to contact you?</b><br>
        A: The most reliable way to reach me is through email or by filling out the contact form above.
        </div>
        """, unsafe_allow_html=True)

    # Call to action
    st.markdown("""
    <div class="highlight normal-font" style="text-align: center; margin-top: 50px;">
        <p>Looking forward to connecting with you!</p>
        <p>Don't hesitate to reach out for collaborations, questions, or just to say hello.</p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    contact_page()
