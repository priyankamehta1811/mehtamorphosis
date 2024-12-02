import streamlit as st
# Function to display the contact form

st.header(":mailbox: Get In Touch With Me!")

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
st.write("")
st.markdown("<div class='main-header'>Contact</div>", unsafe_allow_html=True)
st.markdown("Feel free to reach out for collaborations or queries:")
st.write("- **Email**: priyanka.m@igib.in")
st.write("- **GitHub**: [priyankamehta1811](https://github.com/priyankamehta1811)")
st.write("- **LinkedIn**: [priyankamehta1811](https://www.linkedin.com/in/priyankamehta1811/)")

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
