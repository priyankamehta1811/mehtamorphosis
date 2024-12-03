import streamlit as st
# Function to display the contact form

st.header(":mailbox: Get In Touch With Me!")
st.markdown("Feel free to contact with me:")

contact_form = """
    <form action="https://formsubmit.co/priyanka.m@igib.in" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here"></textarea>
        <button type="submit">Send</button>
    </form>
    """
# Render the contact form in the Contact section
st.markdown(contact_form, unsafe_allow_html=True)

# Additional contact details
st.write("""

         """)


col1, col2, col3 = st.columns([1,1,1])  # Adjust column ratios as needed

with col1:
    st.link_button("My LinkedIn", "https://www.linkedin.com/in/priyankamehta1811/")
        
with col2:
    st.link_button("My GitHub", "https://github.com/priyankamehta1811")

with col3:       
    st.link_button("My Twitter/X", "https://x.com/PriyankaMMehta")

# Use local CSS File
def local_css(file_name):
        with open(file_name, "r") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Load the CSS file (make sure the path is correct)
local_css("pages/style/style_contact.css")


# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>
    © 2024 Priyanka Mehta | Ingen-hope Lab
    </p>
    """,
    unsafe_allow_html=True
)
