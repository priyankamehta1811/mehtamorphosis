import streamlit as st

st.header("🎨 SciART!")

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

/* Center content */
.stApp {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
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

/* Add neon pink glow and drop shadow to images */
img {
  border: 0.1px solid #FFFFFF;
  box-shadow: 0 0 5px #FFFFFF, 0 0 10px #FFFFFF, 0 0 20px #FFFFFF;
  transition: all 0.3s ease;
}

img:hover {
  box-shadow: 0 0 25px #00ffe7, 0 0 50px #00ffe7, 0 0 100px #00ffe7;
}

</style>
"""
# Inject the CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

st.markdown("""##### Explore some of my creative projects:""")
    
# Example of how you could display book covers and descriptions
st.markdown("[![1](https://m.media-amazon.com/images/I/61xw+3TI16L.jpg)](https://shop.elsevier.com/books/genomic-surveillance-and-pandemic-preparedness/pandey/978-0-443-18769-8)")
st.markdown("_*Designed the cover page of Genomic Surveillance and Pandemic Preparedness*_")

# Display an image with Streamlit
st.image("pages/images/covid.jpg")
st.write("3D SARS-CoV-2 particle")
st.image("pages/images/wallpainting.png")
st.write("""The Usual Suspects Parody:  
         A line-up of SARS-CoV-2 Variants of Concern (VoCs)- Alpha, Delta and Omicron. 
         Who done it?""")


st.markdown("<div class='main-header'>Co-Curricular Activities</div>", unsafe_allow_html=True)
st.markdown("Some of my beloved 30 Day Chart Challenges")
    
st.markdown("### Workshops and Seminars")
st.markdown("- **Indo-Vietnam training**: Hands-on Training Workshop on Sequencing Techniques.")
st.markdown("- **Science Communication Seminar**: Presented research findings and communicated complex data effectively.")
    

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
