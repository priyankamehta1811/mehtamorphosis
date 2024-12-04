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


st.title(":books: Publications!")
# Link to the publications page from the homepage
st.link_button("Go to Google Scholar", "https://scholar.google.com/citations?user=W27to54AAAAJ&hl=en")
    

# Inline CSS for the Streamlit app
st.markdown("""
<style>
    /* General Styling for the Streamlit App */
    body {
        background-color: #111;
        color: #fff;
        font-family: 'Arial', sans-serif;
    }

    .main-header {
        color: #f5f5f5;
        font-size: 2.5em;
        text-align: center;
        margin-top: 20px;
    }

    a {
        color: #1e90ff;
        text-decoration: none;
    }

    a:hover {
        text-decoration: underline;
    }

    /* Custom book-like styling */
    .container {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }

    /* Adding animation and effects */
    @keyframes flashlight {
        0%, 9% {
            opacity: 0;
            clip-path: circle(150px at 45% 10%);
        }
        10%, 15%, 85% {
            opacity: 1;
        }
        50% {
            clip-path: circle(150px at 60% 20%);
        }
        54%, 100% {
            clip-path: circle(150px at 55% 92%);
        }
        88%, 100% {
            opacity: 0;
        }
    }

    @keyframes eyes {
        0%, 52% {
            opacity: 0;
        }
        53%, 87% {
            opacity: 1;
        }
        64% {
            transform: scaleY(1);
        }
        67% {
            transform: scaleY(0);
        }
        70% {
            transform: scaleY(1);
        }
        88%, 100% {
            opacity: 0;
        }
    }
</style>
""", unsafe_allow_html=True)


# Example of publications with links
st.markdown("Here are some of my publications over the years:")
st.markdown(""" #### **_2024_** """)
st.markdown("1)  Suppressed transcript diversity and immune response in COVID-19 ICU patients: a longitudinal study. _Life Science Alliance_")
st.markdown("[![1](https://www.life-science-alliance.org/content/lsa/7/1/e202302305/F1.large.jpg)](https://www.life-science-alliance.org/content/7/1/e202302305)")
# Add more publications similarly as needed
st.markdown("2) Whole Transcriptome Analysis (WTA) and Surface markers expression (AbSeq) in Immune Cells of COVID-19 Patients and Recovered captured through Single Cell Genomics. _Frontiers in Medicine_")
st.markdown("[![2](https://www.frontiersin.org/files/Articles/1297001/fmed-11-1297001-HTML-r1/image_m/fmed-11-1297001-g003.jpg)](https://doi.org/10.3389/fmed.2024.1297001)")
# Add more publications similarly as needed
st.markdown("3) Cell-specific housekeeping role of lncRNAs in COVID-19-infected and recovered patients. _NAR Genomics and Bioinformatics_")
st.markdown("[![3](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/nargab/6/1/10.1093_nargab_lqae023/1/lqae023figgra1.jpeg?Expires=1736228488&Signature=WJqDQ6s0C~j2MNUeEJC5VpPeD9OXxb4lE6kX5msQbTJ4H~1l9xmPRG4NxQMubvlCl-ICAO0djMIdTRqw0-9ghqf90AX-DRnbXRK5P6nrWy2ZD7jUftahhosNW~C5AYkJqfLDz~gLgDh3wiSGXS8NRCxZCzKlWi4b--td7HDoUCxu8jq8cr0rcNvPq6jo6wfGgNMuGhOxfI0aoeoWwHtTCuW2O9QxiD6YeMBonzl1yyaqgYg5tBZCaplflYBUh3otdhvi040BqwStma47WELTe6NWIEFeTnTEp5MPhgGwqIAspUoQJE7sDoZSntqy2mLXmxAJF2H9R1~RTO~5ZkG2Xw__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA)]( https://doi.org/10.1093/nargab/lqae023)")
# Add more publications similarly as needed
st.markdown("4)  RNA editing in host lncRNAs as potential modulator in SARS-CoV-2 variants-host immune response dynamics _iScience_")
st.markdown("[![4](https://ars.els-cdn.com/content/image/1-s2.0-S258900422401068X-fx1.jpg)](https://www.sciencedirect.com/science/article/pii/S258900422401068X)")
# Add more publications similarly as needed

st.markdown(""" #### **_2023_** """)
st.markdown("1)  Deficient Phagocytosis in Circulating Monocytes from Patients with COVID-19-Associated Mucormycosis _mBio_")
st.markdown("[![1](https://journals.asm.org/cms/10.1128/mbio.00590-23/asset/dd932726-dfa1-4252-b709-7cf96a8e396b/assets/images/medium/mbio.00590-23-f001.gif)](https://doi.org/10.1128/mbio.00590-23)")
# Add more publications similarly as needed
st.markdown("2) SARS-CoV-2 infection severity and mortality is modulated by repeat-mediated regulation of alternative splicing _Microbilogy Spectrum_")
st.markdown("[![2](https://journals.asm.org/cms/10.1128/spectrum.01351-23/asset/105439ca-d5fc-4de6-9648-a41ee7bdc481/assets/images/large/spectrum.01351-23.f006.jpg)](https://doi.org/10.1128/spectrum.01351-23)")
# Add more publications similarly as needed
st.markdown("3) Dysregulated metal ion homeostasis underscores non-canonical function of CD8+ T cell during COVID-19 _ Frontiers in Medicine_")
st.markdown("[![3](https://www.frontiersin.org/files/Articles/1282390/fmed-10-1282390-HTML-r1/image_m/fmed-10-1282390-g001.jpg)](https://doi.org/10.3389/fmed.2023.1282390)")
# Add more publications similarly as needed
st.markdown("4)  Single-cell RNA-Seq reveals intracellular microbial diversity within Immune cells during SARS-CoV-2 Infection and Recovery. _iScience_")
st.markdown("[![4](https://www.cell.com/cms/10.1016/j.isci.2023.108357/asset/5497c0a2-ad8c-4465-a1e0-d34a6b7ed503/main.assets/fx1_lrg.jpg)](https://www.cell.com/iscience/fulltext/S2589-0042(23)02434-3)")
# Add more publications similarly as needed


st.markdown(""" #### **_2022_** """)
st.markdown("1)  Clinico-Genomic Analysis Reiterates Mild Symptoms Post-vaccination Breakthrough: Should We Focus on Low-Frequency Mutations? _Frontiers in Microbiology_")
st.markdown("[![1](https://www.frontiersin.org/files/Articles/763169/fmicb-13-763169-HTML/image_m/fmicb-13-763169-g004.jpg)](https://doi.org/10.3389/fmicb.2022.763169)")
# Add more publications similarly as needed
st.markdown("2) Increased Abundance of Achromobacter xylosoxidans and Bacillus cereus in Upper Airway Transcriptionally Active Microbiome of COVID-19 Mortality Patients Indicates Role of Co-Infections in Disease Severity and Outcome _Microbilogy Spectrum_")
st.markdown("[![2](https://journals.asm.org/cms/10.1128/spectrum.02311-21/asset/8d8d41ba-f2d9-424d-8c84-e915be08f19d/assets/images/large/spectrum.02311-21-f008.jpg)](https://doi.org/10.1128/spectrum.02311-21)")
# Add more publications similarly as needed
st.markdown("3) COVID-19 Risk Stratification and Mortality Prediction in Hospitalized Indian Patients: Harnessing clinical data for public health benefits _PLOS One_")
st.markdown("[![3](https://journals.plos.org/plosone/article/figure/image?size=large&id=10.1371/journal.pone.0264785.g001)](https://doi.org/10.1371/journal.pone.0264785)")
# Add more publications similarly as needed
st.markdown("4)  LncRNAs harbouring regulatory motifs within repeat elements modulate immune response towards COVID‐19 disease severity and clinical outcomes _Clinical and Translational Medicine_")
st.markdown("[![4](https://onlinelibrary.wiley.com/cms/asset/4c6258fd-78ee-437f-9036-6aaf7d5ab176/ctm2932-fig-0002-m.png)](https://doi.org/10.1002/ctm2.932)")
# Add more publications similarly as needed
st.markdown("5)   Mutational dynamics across VOCs in International travellers and Community transmission underscores importance of Spike-ACE2 interaction. _Microbiological research_")
st.markdown("[![5](https://ars.els-cdn.com/content/image/1-s2.0-S0944501322001392-gr1.jpg)](https://doi.org/10.1016/j.micres.2022.127099)")
# Add more publications similarly as needed

st.markdown(""" #### **_2021_** """)
st.markdown("1) Respiratory co-infections: modulators of SARS-CoV-2 patients’ clinical sub-phenotype. _Frontiers in Microbiology_")
st.markdown("[![1](https://www.frontiersin.org/files/Articles/653399/fmicb-12-653399-HTML/image_m/fmicb-12-653399-g008.jpg)]( https://doi.org/10.3389/fmicb.2021.653399)")
# Add more publications similarly as needed
st.markdown("2) Plasma Gradient of Soluble Urokinase-Type Plasminogen Activator Receptor Is Linked to Pathogenic Plasma Proteome and Immune Transcriptome and Stratifies Outcomes in Severe COVID-19. _Frontiers in Immunology_")
st.markdown("[![2](https://www.frontiersin.org/files/Articles/738093/fimmu-12-738093-HTML/image_m/fimmu-12-738093-g006.jpg)](https://doi.org/10.3389/fimmu.2021.738093)")
# Add more publications similarly as needed
st.markdown("3) Culture-Independent Exploration of the Hypersaline Ecosystem Indicates the Environment-Specific Microbiome Evolution. _Frontiers in Microbiology_")
st.markdown("[![3](https://www.frontiersin.org/files/Articles/686549/fmicb-12-686549-HTML/image_m/fmicb-12-686549-g005.jpg)](https://doi.org/10.3389/fmicb.2021.686549)")
# Add more publications similarly as needed
st.markdown("4)  Geographical landscape and transmission dynamics of SARS-CoV-2 variants across India: a longitudinal perspective. _Frontiers in Genetics_")
st.markdown("[![4](https://www.frontiersin.org/files/Articles/753648/fgene-12-753648-HTML-r1/image_m/fgene-12-753648-g001.jpg)](https://doi.org/10.3389/fgene.2021.753648)")





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
