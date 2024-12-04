import streamlit as st
# Function to display the contact form

# Add custom CSS
custom_css = """
<style>
/* Import Google Font */
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');

/* Apply font globally */
html, body, [class*="css"] {
  font-family: 'Orbitron', sans-serif;
  color: white;
}

.block-container
{
    padding-top: 4rem;
    padding-bottom: 2rem;
}
  
/* Background */
[data-testid="stSidebar"] {
  background: linear-gradient(-45deg, #322C2B, #003C43, #D20062);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
  font-family: 'Orbitron', sans-serif;
  margin: 0;
}

/* Background */
body,[data-testid="stAppViewContainer"],[data-testid="stHeader"] {
  background: linear-gradient(-45deg, #322C2B, #003C43, #640D6B);
  background-size: 400% 400%;
  animation: gradient 15s ease infinite;
  font-family: 'Orbitron', sans-serif;
  margin: 0;
}

@keyframes gradient {
    0% {
      background-position: 0% 50%;
    }
    50% {
      background-position: 100% 50%;
    }
    100% {
      background-position: 0% 50%;
    }
  }

/* Sidebar Navigation */
[data-testid="stSidebarNav"] {
  font-family: 'Orbitron', sans-serif !important;
  color: #ff007f !important; /* Change font color */
}

/* Sidebar Navigation Links */
[data-testid="stSidebarNav"] a {
  color: #ff007f !important; /* Link color */
  text-shadow: 0px 0px 3px #ff007f;
  font-size: 16px;
}

/* Hover effect for navigation links */
[data-testid="stSidebarNav"] a:hover {
  color: #00ffe7 !important;
  text-shadow: 0px 0px 5px #00ffe7;
  transition: all 0.3s ease-in-out;
}

/* Background for sidebar */
.css-1l02zno { 
  background: linear-gradient(270deg, #003062, #005678, #ff2a6d, #24243e) !important;
  color: white;
}

/* Scrollbar Styling */
.sidebar ::-webkit-scrollbar {
    width: 10px;
}
.sidebar ::-webkit-scrollbar-thumb {
    background: #ff007f;
    border-radius: 10px;
}

/* Scrollbar */
::-webkit-scrollbar {
  width: 10px;
  
}
::-webkit-scrollbar-thumb {
  background: #ff007f;
  border-radius: 10px;
}

/* Headers */
h1, h2, h3, h4, h5, h6 {
  font-family: 'Orbitron', sans-serif ;
  color: #00ffe7;
  text-shadow: 0px 0px 5px #00ffe7, 0px 0px 20px #00ffe7;
  text-align: center;
}

/* Paragraphs */
p {
  color: #f7f7f7;
  text-shadow: 0px 0px 3px #ffffff;
}

/* Links */
a {
  color: #ff007f;
  text-decoration: none;
  text-shadow: 0px 0px 1px #ff007f;
}
a:hover {
  color: #00ffe7;
  text-shadow: 0px 0px 1px #00ffe7;
}


/* Sidebar Styling */
.sidebar .sidebar-content {
    background: linear-gradient(270deg, #003062, #005678, #ff2a6d);
    padding: 20px;
    color: white;
    font-family: 'Orbitron', sans-serif;
    box-shadow: 5px 0px 15px rgba(0, 0, 0, 0.3);
    border-radius: 10px;
}


/* Inputs */
input, textarea {
  background-color: #24243e;
  color: white;
  border: 1px solid #00ffe7;
  border-radius: 5px;
  padding: 10px;
}

</style>
"""
# Inject the CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

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
