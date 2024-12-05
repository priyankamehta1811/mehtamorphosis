import streamlit as st


# Set Streamlit page config
st.set_page_config(
    page_title="MehtaMorphosis", #Decoding 
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
  
)
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
    padding-top: 2rem;
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
  text-shadow: 0px 0px 10px #ff007f;
}
a:hover {
  color: #00ffe7;
  text-shadow: 0px 0px 15px #00ffe7;
}

/* Buttons */
button {
  background-color: #00ffe7;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  color: black;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s ease;
}
button:hover {
  background-color: #ff007f;
  color: white;
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

# Inject CSS into Streamlit
st.markdown(custom_css, unsafe_allow_html=True)

# App content

st.title("Welcome to MehtaMorphosis")
# Inject the CSS theme
st.markdown(custom_css, unsafe_allow_html=True)

#st.sidebar.success("Select a page above.")


st.markdown("Hi, my name is Priyanka Mehta.")
st.markdown("I'm a bioinformatician and data visualization enthusiast.")
st.markdown(
        """
        <p class='sub-header' style='text-align: justify;'>
        Explore my research on host-pathogen interactions, focusing on the genomics and transcriptomics of RNA viruses.
        Join me in uncovering alternative splicing dynamics and their role in viral adaptation and pathogenesis.
        Through integrative analyses, I aim to uncover novel insights into how these molecular mechanisms influence 
        disease progression and outcomes, contributing to a deeper understanding of host-pathogen biology.
        </p>
        """,
        unsafe_allow_html=True
    )
st.image("pages/images/DALL·E.webp", caption="created using DALL.E")


# Footer
st.markdown(
    """
    <hr>
    <p style='text-align: center;'>
    © 2024 Priyanka Mehta | INGEN-HOPE Lab
    </p>
    """,
    unsafe_allow_html=True
)
