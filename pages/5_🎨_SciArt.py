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


st.markdown("### Beyond Academics", unsafe_allow_html=True)
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
st.image("pages/images/brain.jpg", caption="World Brain Day")

st.markdown(""" 
""")
st.markdown("##### 30 Day Chart Challenges:")
st.markdown(""" 
""")
st.markdown("Never too late to give a vintage map a modern makeover! ")
col1, col2= st.columns([1,1])  # Adjust column ratios as needed


with col1:
    st.image("pages/images/before.jpg", caption="2D vintage map")

with col2:
    st.image("pages/images/after.jpg", caption="3D rendering of Vintage map")
    
#st.image("pages/images/bees.jpg", caption="3D rendering of Vintage map")
st.markdown("What's your fitness goal for the Summer?  Consider incorporating #jumpropes (my favorite) into your fitness routine to achieve your summer body goals!  ")
st.markdown("[![4](https://pbs.twimg.com/media/GK3i3kEXUAAroxO?format=jpg&name=4096x4096)](https://x.com/PriyankaMMehta/status/1778326991873134677/photo/1)")

st.markdown("Global Land Cover Changes  Divergent trends in land coverage change between Israel and Korea reflect the complex interplay of socio-economic factors, environmental policies, and land management practices within each country. ")
st.markdown("[![4](https://pbs.twimg.com/media/GKgKBCKbcAAJRT5?format=jpg&name=4096x4096)](https://x.com/PriyankaMMehta/status/1776681104499749278/photo/1)")

st.markdown("Diverging Population Growth Rates amongst top 30 ranked nations.")
st.markdown("[![4](https://pbs.twimg.com/media/GKd9zL3bwAA2nah?format=jpg&name=medium)](https://x.com/PriyankaMMehta/status/1776526905988239414/photo/1)")

st.markdown("COVID-19 mortality data representation between India and other nations like US and UK. ")
st.markdown("[![4](https://pbs.twimg.com/media/FQFQcSzacAQ_nZb?format=jpg&name=large)](https://x.com/PriyankaMMehta/status/1513579458690633729/photo/1)")

st.markdown("Representing migration rate over past 6 decades by region.")
st.markdown("[![4](https://pbs.twimg.com/media/FQFRKWNakAAjdpL?format=jpg&name=large)](https://x.com/PriyankaMMehta/status/1513580210079240192/photo/1)")

st.markdown("Representing Average annual rate of population change by region over 6 decades.")
st.markdown("[![4](https://pbs.twimg.com/media/FQFSN0paMAEt8PR?format=jpg&name=large)](https://x.com/PriyankaMMehta/status/1513581387277746181/photo/1)")


st.markdown("Flowers of India is a go to site to satisfy your curiosity when you run into a beautiful flower during a hike or a morning walk.")
st.markdown("[![4](https://pbs.twimg.com/media/FPhc-HtUcAIiymU?format=jpg&name=4096x4096)](https://x.com/PriyankaMMehta/status/1511059901040136194/photo/1)")   

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
