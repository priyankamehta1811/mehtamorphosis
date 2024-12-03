import streamlit as st

# Set Streamlit page config
st.set_page_config(
    page_title="MehtaMorphosis", #Decoding 
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
  
)

# CSS for your custom dark academia theme
custom_css = """
<style>
* {
  color: white;
}

body, html, #root {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: transparent;
}

#background {
  position: fixed;
  inset: 0;
  width: 100vw;
  height: 100vh;
  z-index: -1;
}

#background::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse, mediumturquoise, darkslateblue);
  filter: url(#grainy);
}

#background::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, .6);
}

#root {
  display: flex;
  align-items: center;
  justify-content: center;
}

.distfx {
  animation: distfx .5s linear infinite;
}

@keyframes distfx {
  0% {
    filter: url("#distfx-0");
  }
  20% {
    filter: url("#distfx-1");
  }
  40% {
    filter: url("#distfx-2");
  }
  60% {
    filter: url("#distfx-3");
  }
  80% {
    filter: url("#distfx-4");
  }
  100% {
    filter: url("#distfx-5");
  }
}
</style>
<div id="background"></div>
"""

# Inject the CSS theme
st.markdown(custom_css, unsafe_allow_html=True)

st.sidebar.success("Select a page above.")


st.markdown("<div class='main-header'>🧬 Welcome to My Academic Portfolio</div>", unsafe_allow_html=True)
st.markdown(
        """
        <p class='sub-header'>
        Explore my research on host-pathogen interactions, focusing on the genomics and transcriptomics of RNA viruses.
        I specialize in uncovering alternative splicing dynamics and their role in viral adaptation and pathogenesis.
        </p>
        """,
        unsafe_allow_html=True
    )
st.image("https://via.placeholder.com/800x300", caption="Host-Pathogen Interactions")


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
