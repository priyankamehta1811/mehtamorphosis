import streamlit as st
st.header(":books: Publications!")

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
st.markdown(""" **_2021_** """)
st.markdown("1) Respiratory co-infections: modulators of SARS-CoV-2 patients’ clinical sub-phenotype. Frontiers in Microbiology")
st.markdown("[![1](https://www.frontiersin.org/files/Articles/653399/fmicb-12-653399-HTML/image_m/fmicb-12-653399-g008.jpg)]( https://doi.org/10.3389/fmicb.2021.653399)")
# Add more publications similarly as needed
st.markdown("2) Clinico-Genomic Analysis Reveals Mutations Associated with COVID-19 Disease Severity: Possible Modulation by RNA Structure.")
st.markdown("[![2](https://www.mdpi.com/pathogens/pathogens-10-01109/article_deploy/html/images/pathogens-10-01109-g008.png)]( https://www.mdpi.com/2076-0817/10/9/1109)")
# Add more publications similarly as needed

# Link to the publications page from the homepage
st.link_button("Go to Google Scholar", "https://scholar.google.com/citations?user=W27to54AAAAJ&hl=en")
    
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
