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
  border: 0.1px solid #ff007f;
  box-shadow: 0 0 10px #ff007f, 0 0 20px #ff007f, 0 0 40px #ff007f;
  transition: all 0.3s ease;
}

img:hover {
  box-shadow: 0 0 25px #ff007f, 0 0 50px #ff007f, 0 0 100px #ff007f;
}

</style>
"""
# Inject the CSS into the Streamlit app
st.markdown(custom_css, unsafe_allow_html=True)

st.title("🔬 Research @ IGIB")
st.markdown(
    """
    - **Alternative Splicing in Viral Adaptation**: Investigating how RNA viruses leverage host splicing mechanisms.
    - **Comparative Genomics**: Identifying conserved and unique features in viral genomes.
    - **Host Immune Response**: Studying transcriptional changes in infected cells using multi-omics approaches.
    """
)

import streamlit as st

# Title
st.markdown("# Strengths & Skills")

# Introductory Text
st.markdown("""
I bring a strong interdisciplinary approach, combining computational expertise with a deep understanding of biological systems. Below are the key strengths and skills that define my work in bioinformatics, data analysis, and research.
""")

# **Coding Languages Section**
st.markdown("### Programming Languages & Tools")
st.markdown("""
- **R**: Advanced proficiency in bioinformatics packages and statistical analysis.
- **Python**: Skilled in data manipulation, bioinformatics pipelines, and automation.
- **Perl**: Expertise in processing large-scale biological data.
- **Streamlit**: Development of interactive web applications for data visualization and bioinformatics tools.
- **HTML & CSS**: Basic knowledge for front-end web design, particularly in scientific contexts.
""")

# **Statistical Techniques Section**
st.markdown("### Statistical & Computational Techniques")
st.markdown("""
I utilize a broad range of statistical techniques to analyze genomic and transcriptomic data, ensuring robust insights into complex biological systems.
- **RNA-seq Data Analysis**: Comprehensive analysis of gene expression and splicing patterns.
- **Single-Cell RNA-seq**: Investigating cellular heterogeneity and gene regulatory mechanisms.
- **NGS Data Analysis**: Expertise in processing Nanopore and Illumina platform data for genomic and transcriptomic insights.
- **Metagenomics**: Analysis of 16S rRNA and WGS to study microbial communities and their interactions.
- **Biostatistics**: Advanced statistical modeling for biological data, including regression, hypothesis testing, and survival analysis.
- **Data Visualization**: Creating informative and interactive visualizations to represent complex biological datasets clearly.
""")

# **Bioinformatics Research Techniques**
st.markdown("### Bioinformatics & Genomic Research Techniques")
st.markdown("""
- **Phylogenetic Analysis**: Reconstruction of evolutionary relationships using genomic data.
- **Mutational Analysis**: Investigating genetic variants and their impacts on disease progression and treatment outcomes.
""")




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

def load_pdf_button(file_path, button_text="Resume"):
    with open(file_path, 'rb') as pdf:
        pdf_bytes = pdf.read()
        return st.download_button(button_text, pdf_bytes, file_name="pages/PM_CV_final.pdf")

if __name__ == "__main__":
    load_pdf_button("pages/PM_CV_final.pdf") 
