import streamlit as st


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
h3 {
  display: flex;
  flex-direction: column;
  align-items: left;
  justify-content: left;
  #height: 100vh;
  text-align: left;
}  

/* Center content */
h4,[data-testid=stElementContainer] {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  #height: 100vh;
  text-align: justify;
}

/* Center content */
.stApp,[data-testid=stDownloadButton]  {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  #height: 100vh;
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
h1,h2 {
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

st.title("🔬 Research")

def load_pdf_button(file_path, button_text="My Resume"):
    with open(file_path, 'rb') as pdf:
        pdf_bytes = pdf.read()
        return st.download_button(button_text, pdf_bytes, file_name="pages/PM_CV_final.pdf")

if __name__ == "__main__":
    load_pdf_button("pages/PM_CV_final.pdf") 

# Function to embed an image
st.image("pages/images/Figure 7.png",  caption="Integrative Clinico-Genomics of Host-Pathogen Interaction")
st.markdown("""## Research Highlights """)

st.markdown("""
My PhD research focuses on understanding how alternative transcript isoforms contribute to differential disease severity and clinical outcomes in infectious disease, including SARS-CoV-2 and Dengue. 
I investigate the impact of disrupted alternative splicing in the host and the adoption of non-canonical transcription mechanisms, such as internal Open Reading Frames (iORFs), 
by viruses, in hospitalised patients. 
Additionally, I am exploring the regulatory factors that govern these alternative isoforms and how they relate to disease progression and severity, 
with the aim of uncovering novel insights into disease pathogenesis. 
""")

st.markdown("""Beyond this, I have been part of different studies such as:""")

# Section 1: Clinico-genomics of SARS-CoV-2
st.write("### 1. Pathogen Genome Architecture")
st.markdown("""
Understanding the evolution and epidemiological patterns of SARS-CoV-2 through clinico-genomics analyses has been a cornerstone in combating the pandemic. 
This research focused on decoding viral mutations across VOCs to map the spread and progression of COVID-19 in India.  **[Click here](https://doi.org/10.1016/j.micres.2022.127099)**
""")

# Section 2: Host-pathogen interactions
st.write("### 2. Host-Pathogen Interactions: Decoding Disease Severity")
st.markdown("""
Using transcriptomic data, I have been part of studies that delved into both the **[coding](https://doi.org/10.1002/ctm2.856)** and **[non-coding](https://doi.org/10.3389/fimmu.2022.1035111)** RNAs, **[alternative splicing](https://www.life-science-alliance.org/content/7/1/e202302305)** events, and **[co-infections](https://doi.org/10.1128/spectrum.02311-21
)**. 
The aim is to unravel the molecular mechanisms underlying disease severity, enabling a deeper understanding of host-pathogen dynamics.
""")

# Section 3: scRNA-seq and microbial investigations
st.write("### 3. scRNA-seq Based Unconventional Investigations at the Cellular Level")
st.markdown("""
Single-cell RNA sequencing offers unparalleled granularity in studying interactions within the host environment. 
I have been part of some unconventional studies that explored **[cell-specific housekeeping role of lncRNAs](https://doi.org/10.1093/nargab/lqae023)** and **[intracellular microbial diversity](https://doi.org/10.1016/j.isci.2023.108357)** within immune cells during SARS-CoV-2 infection and recovery
This research pioneers techniques for exploring scRNA-seq data beyond conventional gene-expression studies.
""")

# Section 4: Metagenomics investigations
st.write("### 4. Metagenomics-Based Investigations")
st.markdown("""
Through metagenomic data analysis, I have collaborated on exploring microbial diversity, functionality, and interactions in **[hypersaline ecosystem](https://doi.org/10.3389/fmicb.2021.686549)** as well as time-dependent modulation of gut microbiome in **[fatty liver disease]( https://doi.org/10.3389/fmicb.2023.1210517)**.
These studies primarily focused on 16S rRNA sequencing and whole-genome sequencing, aiming to advance our understanding of microbial ecosystems.
""")

st.markdown("""---""")
# **Coding Languages Section**
st.markdown("""## Skills """)
st.markdown("""
 """)
st.markdown("""#### Computational """)
# Transparent box style with white text
transparent_box_style = """
<style>
.simple-box {
    background-color: rgba(255, 255, 255, 0.1); /* Transparent box */
    border: 1px solid rgba(255, 255, 255, 0.3); /* Light white border */
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
    text-align: center;
    color: white; /* White text */
}
</style>
"""

# Inject the custom CSS
st.markdown(transparent_box_style, unsafe_allow_html=True)

# Create transparent boxes for each column
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown(
        """
        <div class="simple-box">
            <strong>Coding Languages</strong><br>
            R<br>
            Python
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="simple-box">
            <strong>Scripting</strong><br>
            Shell<br>
            Perl
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="simple-box">
            <strong>Web Development</strong><br>
            HTML & CSS<br>
            Streamlit
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("""
 """)
st.markdown("""#### Genomic Analysis """)

# Transparent box style with white text
transparent_box_style = """
<style>
.simple-box {
    background-color: rgba(255, 255, 255, 0.1); /* Transparent box */
    border: 1px solid rgba(255, 255, 255, 0.3); /* Light white border */
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
    text-align: center;
    color: white; /* White text */
}
</style>
"""

# Inject the custom CSS
st.markdown(transparent_box_style, unsafe_allow_html=True)

# Create transparent boxes for each column
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.markdown(
        """
        <div class="simple-box">
            <strong>Illumina</strong><br>
            Bulk/scRNAseq<br>
            Viral WGS <br>
            16S rRNA
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="simple-box">
            <strong>Oxford Nanopore Tech.</strong><br>
            Human and Viral WGS<br>
            RNAseq
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="simple-box">
            <strong>Element Bioscience</strong><br>
            RNAseq<br>
            </div>
        """,
        unsafe_allow_html=True,
    )


st.markdown("""
---

""")

st.markdown("## Workshops")
st.markdown(" **Indo-Vietnam Hands-on Training Workshop**:")

col1, col2 = st.columns([1,1])  # Adjust column ratios as needed

with col1:
  st.image("pages/images/first.jpg", caption="Compering at 1st INDO-VIETNAM Workshop")
with col2:
  st.image("pages/images/2nd.jpeg", caption="Compering at 2st INDO-VIETNAM Workshop")

st.markdown("## Conferences:")

st.markdown(" **CSIR One Week One Lab (OWOL)**  _Srinagar, India, '24_")
st.markdown("Presenting our lab's work at Univeristy of Kashmir, complete with a bonus of reuniting with an old lab buddy!")
st.image("pages/images/owol.jpg", caption="One Week One Lab Event")

st.markdown(" **29th Annual RNA Society Meeting** _Edinburgh, Scotland, '24_")
st.markdown("Had a fantastic time at the #RNA2024 poster session at the RNASociety meeting in Edinburgh. Amazing opportunity to share my work at RajeshPandeyLab with fellow RNA biologists. Also got exciting new ideas to explore in my own data!")
st.image("pages/images/RNA_society.jpg", caption="RNA Society")


# Usage


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


