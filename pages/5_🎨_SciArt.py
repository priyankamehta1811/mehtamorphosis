import streamlit as st
import base64

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
st.markdown("_*Book cover design (click on the image)*_")

# Display an image with Streamlit
st.image("pages/images/covid.jpg")
st.write("3D SARS-CoV-2 particle")
st.image("pages/images/wallpainting.png")
st.write("""The Usual Suspects Parody:  
         A line-up of SARS-CoV-2 Variants of Concern (VoCs)- Alpha, Delta and Omicron. 
         Who done it?""")
st.image("pages/images/brain.jpg", caption="World Brain Day")

# Add custom CSS for the flip effect
css = """
<style>
.image-container {
  width: 550px; /* Set the width of the container */
  height: 400px; /* Set the height of the container */
  perspective: 1000px; /* Add perspective for the 3D effect */
  margin: auto;
}

.image-flip {
  width: 100%;
  height: 100%;
  position: relative;
  transform-style: preserve-3d;
  transition: transform 0.6s ease-in-out;
}

.image-container:hover .image-flip {
  transform: rotateY(180deg); /* Rotate the image on hover */
}

.image-flip img {
  width: 100%;
  height: 100%;
  position: absolute;
  backface-visibility: hidden;
}

.image-flip .back {
  transform: rotateY(180deg); /* Flip the back image */
}
</style>
"""
st.markdown(css, unsafe_allow_html=True)

def img_to_base64(img_path):
    with open(img_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


front_base64 = img_to_base64("pages/images/labpost card.jpg")
back_base64 = img_to_base64("pages/images/postcard back.jpg")

st.write("#### Having fun with Biorender")

st.write("**Ingen-hope Lab Post Card Design**")
# Add the HTML structure for the flip effect
html = f"""
<div class="image-container">
  <div class="image-flip">
    <img src="data:image/jpeg;base64,{front_base64}" alt="Front Image" class="front">
    <img src="data:image/jpeg;base64,{back_base64}" alt="Back Image" class="back">
  </div>
</div>
"""

# Display the custom CSS and HTML in Streamlit
st.markdown(html, unsafe_allow_html=True)

# Add some explanatory text
st.write("_Hover over the image above to see it flip!_")

st.write("**Badge Design**")
st.markdown("An apoptotic macrophage, a few loathing friends, a gang of thugs, a few party crashers, a latecomer, and an unsuspecting victim... What will be the end? Can the cell get to eat its last doughnut or will it end with just a drool!")
st.image("pages/images/badge.jpg", caption="BioRenderVISUALIZE2021")


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

st.markdown("Neo(nic) pesticides usage affect bee colonies. The data represents usage of neonic pesticides over two decades across different US regions and their effect on Bees population. ")    
st.image("pages/images/bees.jpg", caption="Beeswarm Chart")

st.markdown("What's your fitness goal for the Summer?  Consider incorporating #jumpropes (my favorite) into your fitness routine to achieve your summer body goals!  ")
st.image("pages/images/day1.jpg", caption="Matrix Plot")

st.markdown("Global Land Cover Changes  Divergent trends in land coverage change between Israel and Korea reflect the complex interplay of socio-economic factors, environmental policies, and land management practices within each country. ")
st.image("pages/images/day3.jpg", caption="Dumbell Chart")

st.markdown("Diverging Population Growth Rates amongst top 30 ranked nations.")
st.image("pages/images/grwoth.jpg", caption="Scatter Plot")

st.markdown("COVID-19 mortality data representation between India and other nations like US and UK. ")
st.image("pages/images/dotplot.jpg", caption="Beeswarm Chart")

st.markdown("Representing migration rate over past 6 decades by region.")
st.image("pages/images/immigration.jpg", caption="Line Plot")

st.markdown("Representing Average annual rate of population change by region over 6 decades.")
st.image("pages/images/excel.jpg", caption="3D Area Plot")

st.markdown("Flowers of India is a go to site to satisfy your curiosity when you run into a beautiful flower during a hike or a morning walk.")
st.image("pages/images/flora.jpg", caption="Radial Bar Chart")

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
